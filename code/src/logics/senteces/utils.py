from typing import List

from logics.senteces.BaseExpression import BaseExpression
from logics.senteces.BaseExpressionWithPreposition import BaseExpressionWithPreposition
from logics.senteces.Expression import Expression
from logics.senteces.FunctionExpression import FunctionExpression


def check_for_contradiction(
        hypothesis: BaseExpression, clauses: List[Expression], list_of_new_objects
):
    """
    Helper function that checks for the given hypothesis if there is a contradiction in the created classes
    :param hypothesis:          The expression to check with
    :param clauses:             The list of clauses
    :param list_of_new_objects: If we need to creat a new object in the process
    :return: If branch is closed, the clause it was closed with, the used unification replacements
    """
    # Go over each clause and check whether it is a base or a function expression
    for clause in clauses:
        if clause == hypothesis and not (
                isinstance(clause, (BaseExpression, FunctionExpression)) and not isinstance(clause, (BaseExpressionWithPreposition, FunctionExpression))):
            continue

        # If it is check if it is a contradiction with the hypothesis expression
        is_contradiction, unification_replacements = hypothesis.is_contradiction_of(
            clause, list_of_new_objects
        )
        if is_contradiction:
            return True, clause, unification_replacements
    return False, None, None
