from logics.senteces.Expression import Expression
from logics.TableauxSolver import TableauxSolver
from logics.senteces.Helper import create_expression
from logics.senteces.WhenExpression import WhenExpression


class DefeasibleTableauxSolver:
    """
    Wrapper class for the tableaux solver that parses the
    expressions and calls the solver
    """

    def __init__(self, clauses, to_be_shown):
        Expression.id_counter = 0
        self.all_expressions = [
            create_expression(clause) for clause in clauses if len(clause) != 0
        ]
        # self.defeasible_expressions = [x for x in self.all_expressions if
        # ( isinstance(x, WhenExpression) and x.defeasible)]
        self.defeasible_expressions = [x for x in self.all_expressions if x.defeasible]
        self.expressions = [
            x
            for x in self.all_expressions
            if not (isinstance(x, WhenExpression) and x.defeasible)
        ]
        self.to_be_shown = create_expression(to_be_shown)

        self.solver = TableauxSolver(self.expressions, self.to_be_shown)
        self.i = 0

    def expand_defeasible_rules(self):

        # adding all conclusions from defeasible information
        for defeasible in self.defeasible_expressions:
            # If it is a def. when exp. we have to prove the premise
            # Otherwise, we simply add the rule
            proved = True
            expression = defeasible.copy()
            tmp = expression.copy()
            tmp.is_support = True
            expression.support = {tmp}
            if isinstance(defeasible, WhenExpression):
                solver = TableauxSolver(self.expressions, defeasible.premise.copy())
                solver.proof()
                proved = solver.all_branches_closed
                solver.solve_tree.save_pdf(f"image_{self.i}.pdf", "pdf")
                expression = defeasible.conclusion.copy()
                expression.support = set(
                    [x for x in solver.closing_arguments if not x.test]
                )

            # if solver.all_branches_closed:
            #     # print(solver.solve_tree.create_file())
            #     solver.solve_tree.save_pdf(f"image_{self.i}.pdf", "pdf")
            #     self.i += 1
            #     expression = defeasible.conclusion.copy()
            #     defeasibleCopy = defeasible.copy()
            #     defeasibleCopy.is_support = True
            #     expression.support = set([x for x in solver.closing_arguments if not x.test])
            #     # print(solver.closing_arguments)
            #     # for arg in solver.closing_arguments:
            #     #     print(arg)
            #     #     print(arg.test)
            #     expression.support.add(defeasibleCopy)
            #     self.expressions.append(expression)
            #     self.defeasible_expressions.remove(defeasible)
            #     self.expand_defeasible_rules()
            #     return

            if proved:
                # print(solver.solve_tree.create_file())
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
        self.expand_defeasible_rules()
        self.solver = TableauxSolver(self.expressions, self.to_be_shown)
        return self.solver.proof()

    def get_applied_rules(self):
        return self.solver.applied_rules

    def tableaux_is_closed(self):
        return self.solver.all_branches_closed

    def get_dot_graph(self):
        return self.solver.solve_tree.create_file()
