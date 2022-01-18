from logics.senteces.Expression import Expression
from logics.TableauxSolver import TableauxSolver
from logics.senteces.Helper import create_expression
from logics.senteces.WhenExpression import WhenExpression
from logics.senteces.BaseExpression import EMPTY_BASE_EXPRESSION


class DefeasibleTableauxSolver:
    """
    Wrapper class for the tableaux solver that parses the
    expressions and calls the solver
    """

    def __init__(self, clauses, to_be_shown, reason_by_cases=False):
        Expression.id_counter = 0
        self.all_expressions = [
            create_expression(clause) for clause in clauses if len(clause) != 0
        ]
        self.solvers = []
        self.reason_by_cases = reason_by_cases
        # self.defeasible_expressions = [x for x in self.all_expressions if
        # ( isinstance(x, WhenExpression) and x.defeasible)]
        self.defeasible_expressions = [x for x in self.all_expressions if x.defeasible]
        self.expressions = [x for x in self.all_expressions if not x.defeasible]
        self.defeated_defeasible_expressions = []
        self.defeated_defeasible_trees = []
        self.contradiction_in_information = False
        self.to_be_shown = create_expression(to_be_shown)
        self.contradicting_information = []
        self.contradiction_resolved = True

        # If it closes then there is a contradiciton
        if not self.reason_by_cases:
            self.tableau_for_checking_contradiction = TableauxSolver(
                self.expressions, EMPTY_BASE_EXPRESSION.copy()
            )
            self.contradiction_in_information = self.tableau_for_checking_contradiction.proof()
            self.contradicting_information = [self.tableau_for_checking_contradiction.closing_arguments]
            if self.contradicting_information:
                self.contradiction_resolved = False
        else:
            self.remove_defeated_contradictions()

        self.solver = TableauxSolver(self.expressions, self.to_be_shown)
        self.i = 0

    def remove_defeated_contradictions(self):
        self.tableau_for_checking_contradiction = TableauxSolver(
            self.expressions + self.defeasible_expressions, EMPTY_BASE_EXPRESSION.copy()
        )
        contradicted_now = self.tableau_for_checking_contradiction.proof()
        self.contradiction_in_information = contradicted_now or self.contradiction_in_information

        if not contradicted_now:
            self.contradiction_resolved = True

        if contradicted_now:
            if len(self.defeasible_expressions) != 0:
                supports = self.tableau_for_checking_contradiction.closing_arguments
                for support in supports:
                    if support.defeasible:
                        self.defeasible_expressions.remove(support)
                        defeated = support.copy()
                        defeated.support = supports.copy()
                        self.defeated_defeasible_expressions.append(defeated)
                        self.defeated_defeasible_trees.append(
                            self.tableau_for_checking_contradiction.solve_tree.create_file())
                        self.contradicting_information.append(list(supports))
                        self.remove_defeated_contradictions()
                        return

                self.contradiction_resolved = False
                self.contradicting_information = self.contradicting_information.append(
                    self.tableau_for_checking_contradiction.closing_arguments)
            else:
                self.contradicting_information = self.contradicting_information.append(
                    self.tableau_for_checking_contradiction.closing_arguments)
                self.contradiction_resolved = False



    def expand_defeasible_rules(self):

        # adding all conclusions from defeasible information
        for defeasible in self.defeasible_expressions:
            # If it is a def. when exp. we have to prove the premise
            # Otherwise, we check that the negation of the expression does not hold
            proved = False

            # Try to add the expression
            if isinstance(defeasible, WhenExpression):
                # Prove the premise
                solver = TableauxSolver(self.expressions, defeasible.premise.copy())
                solver.proof()
                proved = solver.all_branches_closed
                # solver.solve_tree.save_pdf(f"image_{self.i}.pdf", "pdf")
                expression = defeasible.conclusion.copy()
                # expression.support = set(
                #     [x for x in solver.closing_arguments if not x.test]
                # )
            else:
                # Check the the negation of the expression does not hold
                solver = TableauxSolver(
                    self.expressions, defeasible.reverse_expression()
                )
                proved = not solver.proof()
                # solver.solve_tree.save_pdf(f"image_{self.i}.pdf", "pdf")
                expression = defeasible.copy()

            expression.support = set(
                [x for x in solver.closing_arguments if not x.test]
            )

            if proved:
                # print(solver.solve_tree.create_file())

                self.solvers.append(solver)

                self.i += 1
                defeasibleCopy = defeasible.copy()
                defeasibleCopy.is_support = True

                # print(solver.closing_arguments)
                # for arg in solver.closing_arguments:
                #     print(arg)
                #     print(arg.test)
                expression.support.add(defeasibleCopy)
                self.expressions.append(expression)
                self.defeasible_expressions.remove(defeasible)
                self.expand_defeasible_rules()
                return

    def solve(self):
        # TODO expand the def. exps one by one

        if not self.reason_by_cases:
            self.expand_defeasible_rules()
            self.solver = TableauxSolver(self.expressions, self.to_be_shown)
        else:
            self.solver = TableauxSolver(self.expressions + self.defeasible_expressions, self.to_be_shown)

        proofed = self.solver.proof()
        self.solvers.append(self.solver)
        return proofed

    def get_applied_rules(self):
        return [solver.applied_rules for solver in self.solvers]

    def tableaux_is_closed(self):
        return self.solver.all_branches_closed

    def get_dot_graph(self):

        return [solver.solve_tree.create_file() for solver in self.solvers]

    def get_support(self):
        return self.solver.closing_arguments

    def get_all_supports(self):
        return [solver.closing_arguments for solver in self.solvers]

    def get_all_tableaus(self):
        return self.solvers

    def get_defeated_defeasible_expressions(self):
        return self.defeated_defeasible_expressions

    def get_contradiction_information(self):
        return self.contradicting_information

    def is_contradiction_resolved(self):
        return self.contradiction_resolved

    def contradicting_graph(self):
        if self.reason_by_cases:
            if self.contradiction_resolved:
                return self.defeated_defeasible_trees
            return self.defeated_defeasible_trees + [self.tableau_for_checking_contradiction.solve_tree.create_file()]
        return [self.tableau_for_checking_contradiction.solve_tree.create_file()]

    def is_contradiction_in_information(self):
        return self.contradiction_in_information
