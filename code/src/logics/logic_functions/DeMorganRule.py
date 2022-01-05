from collections import defaultdict
from logics.logic_functions.Rule import Rule
from logics.senteces.ConnectedExpression import ConnectedExpression


class DeMorganRule(Rule):
    def __init__(self, expression, resulting_expression_1, resulting_expression_2):
        self.name = "De Morgan Law Rule"
        self.applicable = "De Morgan Law Rule"
        self.description = " Transformation rules: Not(A AND B) => (Not A OR Not B) | Not(A OR B) => (Not A AND Not B)"
        self.expression = expression
        self.resulting_expression_1 = resulting_expression_1
        self.resulting_expression_2 = resulting_expression_2

    def get_explanation(self):
        return dict(
            name=self.name,
            description=self.description,
            in_expression=[self.expression.get_string_rep()],
            out_expression=[
                [
                    self.resulting_expression_1.get_string_rep(),
                    self.resulting_expression_2.get_string_rep(),
                ]
            ],
        )

    @staticmethod
    def apply_rule(clause: ConnectedExpression, *args):
        new_clauses = defaultdict(list)

        if type(clause) is not ConnectedExpression:
            return new_clauses, None

        if clause.negated is False:
            return new_clauses, None

        de_morgan = ConnectedExpression(
            not clause.negated,
            clause.left_expression.reverse_expression(),
            clause.right_expression.reverse_expression(),
            "or" if clause.connection_keyword == "and" else "and",
            clause.copy_support(),
            clause.defeasible,
        )

        if clause.connection_keyword == "and":
            new_clauses[0].append(de_morgan.left_expression)
            new_clauses[1].append(de_morgan.right_expression)

        if clause.contains("or"):
            new_clauses[0].append(de_morgan.left_expression)
            new_clauses[0].append(de_morgan.right_expression)

        return (
            new_clauses,
            DeMorganRule(clause, de_morgan.left_expression, de_morgan.right_expression),
        )
