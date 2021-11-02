from collections import defaultdict

from logics.Constants import and_connection_keywords, iff_keywords
from logics.logic_functions.Rule import Rule
from logics.senteces.ConnectedExpression import ConnectedExpression
from logics.senteces.IffExpression import IffExpression
from logics.senteces.WhenExpression import WhenExpression


class IffRule(Rule):
    """
    Class representing the application of the if-and-only-if rule.
    It is required for the tool tip
    """

    def __init__(self, expression, resulting_expression_1, resulting_expression_2):
        self.name = 'If-and-only-if Rule'
        self.applicable = 'Iff Rule'
        self.description = '(A iff B) => add the two if-expressions B if A and A if B to the node'
        self.expression = expression
        self.resulting_expression_1 = resulting_expression_1
        self.resulting_expression_2 = resulting_expression_2

    def get_explanation(self):
        """
        :return: Create the explanation based on the provided data in the object.
        """
        return dict(
            name=self.name,
            description=self.description,
            basic_in_expression=["Expression 1 IFF Expression 2"],
            basic_out_expression=[["Expression 1", "Expression 2"]],
            in_expression=[self.expression.get_string_rep()],
            out_expression=[
                [self.resulting_expression_1.get_string_rep(), self.resulting_expression_2.get_string_rep()]],
        )

    @staticmethod
    def apply_rule(clause: IffExpression, *args):
        """
        Apply the iff-rule
        :param clause: The clause to which the rule is applied to
        :param args: The remaining args being the other clauses, list_of_new_objects
        :return: Dictionary containing the branches. Each branch containing a list of created expressions.
        """
        new_clauses = defaultdict(list)

        # Do application tests
        if type(clause) is not IffExpression:
            return new_clauses, None

        # TODO check if that's correct (clause.negated)
        if clause.connection_keyword not in iff_keywords:
            return new_clauses, None

        left_exp = WhenExpression(
            f"If {clause.left_expression.get_string_rep()} then {clause.right_expression.get_string_rep()}")
        right_exp = WhenExpression(
            f"If {clause.right_expression.get_string_rep()} then {clause.left_expression.get_string_rep()}")

        if clause.negated:
            new_clauses[0] += [left_exp.reverse_expression()]
            new_clauses[1] += [right_exp.reverse_expression()]
        else:
            new_clauses[0] += [left_exp]
            new_clauses[0] += [right_exp]


        # Return the branches and create the rule description
        return new_clauses, IffRule(clause, left_exp, right_exp)
