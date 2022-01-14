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
        self.expressions = [
            x
            for x in self.all_expressions
            if not (isinstance(x, WhenExpression) and x.defeasible)
        ]

        self.to_be_shown = create_expression(to_be_shown)

        # If it closes then there is a contradiciton
        self.contradiction_in_information = TableauxSolver(
            self.expressions, EMPTY_BASE_EXPRESSION.copy()
        ).proof()

        self.solver = TableauxSolver(self.expressions, self.to_be_shown)
        self.i = 0

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
            self.solver = TableauxSolver(self.all_expressions, self.to_be_shown)

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
