from collections import defaultdict

from logics.logic_functions.Rule import Rule
from logics.senteces.UnlessExpression import UnlessExpression


class UnlessRule(Rule):
    """
    Class representing the application of the unless rule
    It is required for the tool tip
    """

    def __init__(self, expression, resulting_expression_1, resulting_expression_2):
        self.name = 'Unless Rule'
        self.applicable = 'Unless Rule'
        self.description = '(Unless A then B) = (If Not A then B) = (A OR B) => <br> Create two sibling leaf to the branch containing A, B, respectively'
        self.expression = expression
        self.resulting_expression_1 = resulting_expression_1
        self.resulting_expression_2 = resulting_expression_2

    def get_explanation(self):
        """
        :return: Create the explanation based on the provided data in the object.
        """
        return dict(
            name = self.name,
            description = self.description,
            basic_in_expression = ["Unless Expression 1 , Expression 2"],
            basic_out_expression = [["Expression 1", "Expression 2"]],
            in_expression = [self.expression.get_string_rep()],
            out_expression = [
                [self.resulting_expression_1.get_string_rep(), self.resulting_expression_2.get_string_rep()]],
        )

    @staticmethod
    def apply_rule(clause: UnlessExpression, *args):
        """
        Apply the unless rule which unless applicable splits the b
        :param clause: The clause to which the rule is applied to
        :param args: The remaining args being the other clauses, list_of_new_objects
        :return: Dictionary containing the branches. Each branch containing a list of created expressions.
        """
        new_clauses = defaultdict(list)

        # Only check is if the expression is the correct type
        if type(clause) is not UnlessExpression:
            return new_clauses, None

        left_exp = clause.premise.copy()
        right_exp = clause.conclusion.copy()

        if clause.negated:
            # Reverse the expressions
            left_exp = clause.premise.reverse_expression()
            right_exp = clause.conclusion.reverse_expression()
            new_clauses[0].append(left_exp)
            new_clauses[0].append(right_exp)
        else:
            # Copy the expression
            new_clauses[0].append(left_exp)
            # Copy the expression
            new_clauses[1].append(right_exp)

        return new_clauses, UnlessRule(clause, left_exp, right_exp)
