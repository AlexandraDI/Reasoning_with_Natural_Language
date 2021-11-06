from logics.senteces.Expression import Expression

from typing import Set


class Argument(Expression):
    def __init__(self, exp: Expression, supp: Set[Expression] = set()):
        """
        An argument expression is made up of an expression and a set of
        expressions or other arguments supporting it.

        The meaning of the argument (and its beahviour) is the same of the expression.

        Argument = (support, expression)
        Support = {exp1, exp2, ..., ({exp3, ...}, exp4), ...}

        Args:
            exp (Expression): the expression to wrap.
            supp (Set): set of expressions or arguments supporting :exp:.

        """

        if len(supp) == 0 or supp is None:
            supp = {
                exp,
            }

        self._exp = exp
        self._supp = supp

    @property
    def expression(self) -> Expression:
        """
        Returns:
            Expression supported by this argument
        """
        return self._exp

    @property
    def support(self) -> Set[Expression]:
        """
        Returns:
            Support of this argument
        """
        return self._supp

    @staticmethod
    def from_contradiction(arg1, arg2):
        """
        When there are two contradicting arguments, it is possible to derive a
        new argument supporting a contradiction. The argument of new argument object is
        the union of the arguments of :args1: and :args2:

        Argument1 = (support1, expression)
        Argument2 = (support2, not expression)
        New Argument = (union(support1, suppor2), not)

        Args:
            arg1 (Argument): first argument used to derive a contradiction.
            arg2 (Argument): other argument used to derive a contradiction.

        Returns:
            New argument supporting a contradiction
        """
        # TODO contradiction is None or another expression?
        exp = None
        supp = arg1.support.union(arg2.support)
        return Argument(exp, supp)

    @staticmethod
    def prove_from_contradiction(arg):
        """
        If there is a test argument in the set of arguments that are supporting
        a contradiction, then it is possible to derive a new argument supporting
        that test.

        Argument = ({exp1, exp2, ..., test exp, ...}, not)
        New argument = (minus({exp1, exp2, ..., test exp, ...}, test exp), not test exp)

        Args:
            arg: the argument used to sopport the test

        Returns:
            new argument

        """
        # TODO check if this is correct
        pass

    def __getattr__(self, attr: str):
        """
        Argument is a wrapper for an expression.
        This method expose the interface of the inner expression

        """
        # TODO check if this correct, check abstract methods
        return self._exp.__getattribute__(attr)

    def copy(self):
        """
        Return a copy of the argument.

        Returns:
            Copy of itself.
        """
        exp = self._exp.copy()
        supp = {i.copy() for i in self._supp}
        return Argument(exp, supp)
