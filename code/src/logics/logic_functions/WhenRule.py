from collections import defaultdict

from logics.logic_functions.Rule import Rule
from logics.senteces.WhenExpression import WhenExpression


class WhenRule(Rule):
    """
    Class representing the application of the when rule
    It is required for the tool tip
    """

    def __init__(self, expression, resulting_expression_1, resulting_expression_2):
        self.name = 'When Rule'
        self.applicable = 'When Rule'
        if not expression.negated:
            self.description = '(When A then B) = (If A then B) = (Not A OR B) => <br> Create two sibling leaf to the branch containing Not A, B, respectively'
        else:
            self.description = 'NOT (When A then B) = NOT (If A then B) = (A and NOT B) => <br> Add two expressions to the node containing A and NOT B'
        self.expression = expression
        self.resulting_expression_1 = resulting_expression_1
        self.resulting_expression_2 = resulting_expression_2

    def get_explanation(self):
        """
        :return: Create the explanation based on the provided data in the object.
        """
        if not self.expression.negated:
            return dict(
                name = self.name,
                description = self.description,
                basic_in_expression = ["When Expression 1 Then Expression 2"],
                basic_out_expression = [["Expression 1", "Expression 2"]],
                in_expression = [f"{self.expression.get_string_rep()} {'[↝]' if self.expression.defeasible else ''}"],
                out_expression = [
                    [self.resulting_expression_1.get_string_rep(), self.resulting_expression_2.get_string_rep()]],
            )
        else:
            return dict(
                name=self.name,
                description=self.description,
                basic_in_expression=["It is not the case that When Expression 1 Then Expression 2"],
                basic_out_expression=[["Expression 1", "Not Expression 2"]],
                in_expression=[self.expression.get_string_rep()],
                out_expression=[
                    [self.resulting_expression_1.get_string_rep(), self.resulting_expression_2.get_string_rep()]],
            )

    @staticmethod
    def apply_rule(clause: WhenExpression, *args):
        """
        Apply the when rule which when applicable splits the b
        :param clause: The clause to which the rule is applied to
        :param args: The remaining args being the other clauses, list_of_new_objects
        :return: Dictionary containing the branches. Each branch containing a list of created expressions.
        """
        new_clauses = defaultdict(list)

        # Only check is if the expression is the correct type
        if type(clause) is not WhenExpression:
            return new_clauses, None

        left_exp = clause.premise.reverse_expression()
        right_exp = clause.conclusion.copy()

        if clause.negated:
            left_exp = clause.premise.copy()
            right_exp = clause.conclusion.reverse_expression()
            new_clauses[0].append(left_exp)
            new_clauses[0].append(right_exp)
        else:
            # Reverse the when expression
            new_clauses[0].append(left_exp)
            # Copy the not when expression
            new_clauses[1].append(right_exp)

        return new_clauses, WhenRule(clause, left_exp, right_exp)
