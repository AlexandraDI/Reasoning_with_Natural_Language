from typing import List, Optional, Set, Union

from logics.Constants import (
    connection_keywords,
    complete_negation,
    separator,
    de_morgan_expression, defeasible_indicators,
)
from logics.senteces.ParseExceptions import ParseException
from utils.Utils import tokenize
import abc
import warnings


class Expression(metaclass=abc.ABCMeta):
    """
    Expression that is a abstract class of which each expression has to be parent of.

    The expression is an argument, made up of a support and an expressions.
    The support is a set of expressions.


    Argument = (support, expression)
    Support = {exp1, exp2, ..., }

    Args:
        hypothesis: the content of this expressions, either as a string or as a list of tokens
        support: set of expressions that support this one. If it is None then the expression itself is used.
            If it is an empty set then this is considered a normal expression (so without a support)
    """

    id_counter = 0  # The expression counter for each new expression
    support = set()

    def __init__(
        self,
        hypothesis: Union[List[str], str],
        support: Optional[Set["Expression"]] = None,
    ):
        # We just want strings or lists (tokens) nothing else
        if hypothesis is None or (
            type(hypothesis) is not str and type(hypothesis) is not list
        ):
            raise ParseException(
                "A hypothesis needs to be of type string or token list and can't be empty."
            )

        # Get the new id
        self.count_id()

        if type(hypothesis) is str:
            self.init_hypo = hypothesis.lower()  # Only use lower case
            self.init_hypo = self.init_hypo.strip(
                "."
            )  # Remove period at the end of the sentence
            self.tokens: List = tokenize(self.init_hypo)  # Split hypo into tokens
        else:
            self.init_hypo = " ".join(hypothesis)
            self.tokens = hypothesis

        # If the "It is not the case that ..." is used remove it from the tokens
        self.negated = False
        if complete_negation in self.init_hypo:
            self.negated = True
            self.tokens = self.tokens[6:]


        # Get the a plays b or c -> a plays b or a plays c
        self.split_references()

        # Special argument to keep track of expressions we are trying to prove
        self.test = False

        # Setup the support
        if support is None:
            self.support = {self.__class__(hypothesis, {})}
        elif isinstance(support, set):
            self.support = self.copy_support()

    def count_id(self) -> None:
        """
        Creat a new id
        """
        self.id = Expression.id_counter
        Expression.id_counter += 1

    def split_references(self) -> None:
        """
        Splits the sentence that references previous subjects into multiple base tokens
        """


        different_keyword = []
        comma_idx = []
        different_keyword_idx = []
        # print(self.tokens)
        for reference in connection_keywords:
            if reference in self.tokens:
                # in case we have comma we want to split sentences differently
                 if reference == ',':
                    comma_idx.append(self.tokens.index(reference))
                 else:
                    different_keyword.append(reference)
                    different_keyword_idx.append(self.tokens.index(reference))

        if(len(comma_idx) ==1 and len(different_keyword_idx) ==1):

                    reference_idx = comma_idx[0]
                    middle_tokens = self.tokens[reference_idx + 1:different_keyword_idx[0]]
                    right_tokens = self.tokens[different_keyword_idx[0] + 1:]

                    if len(middle_tokens) == 1 and len(right_tokens) == 1:
                        start_idx = 1 if self.tokens[0] == de_morgen_expression else 0
                        base_tokens = self.tokens[start_idx:reference_idx - 1]
                        left_tokens = self.tokens[:reference_idx]

                        self.tokens = left_tokens + [different_keyword[0]] + base_tokens + middle_tokens + [different_keyword[0]] + base_tokens + right_tokens

        elif (len(comma_idx) == 0 and len(different_keyword_idx) == 1):
            reference_idx = different_keyword_idx[0]
            right_tokens = self.tokens[reference_idx + 1:]

            if len(right_tokens) == 1:
                    start_idx = 1 if self.tokens[0] == de_morgan_expression else 0
                    base_tokens = self.tokens[start_idx:reference_idx - 1]
                    left_tokens = self.tokens[:reference_idx]

                    self.tokens = left_tokens + [different_keyword[0]] + base_tokens + right_tokens



    def is_contradiction_of(self, clause, list_of_new_objects):
        return False

    @abc.abstractmethod
    def reverse_expression(self):
        pass

    @abc.abstractmethod
    def replace_variable(self, replace, replace_with):
        pass

    @abc.abstractmethod
    def copy(self) -> "Expression":
        pass

    def copy_support(self) -> Optional[Set["Expression"]]:
        """
        Returns:
            A copy of the support of this expressions
        """
        if self.support is None:
            return None
        return {i.copy() for i in self.support}

    def contains(self, word):
        if word in self.tokens:
            return True
        else:
            return False

    def get_string_rep(self):
        return separator.join(self.tokens)

    def __str__(self):
        return f"{type(self).__name__}(neg={self.negated}, tokens={self.tokens}), support={self.support}"

    def __repr__(self):
        return f"{self.tokens}"

    def __len__(self):
        return len(self.tokens)

    def __eq__(self, other: "Expression") -> bool:
        """
        Args:
            other: expression compared to this one

        Returns:
            Whether the given expression is equivalent to this expression

        Note:
            Check if subclasses have to extend this method.
        """
        # id is unique -> same id same object
        if self.id == other.id:
            return True

        if type(self) != type(other):
            return False

        if self.negated != other.negated:
            return False

        if self.tokens != other.tokens:
            return False
        return True

    def __hash__(self) -> int:
        """
        Returns:
            Hash of the object. This method is needed to use expressions in sets.
        """
        return super().__hash__()

    @staticmethod
    def support_union(exp1: "Expression", exp2: "Expression") -> Set["Expression"]:
        s1 = exp1.copy_support()
        s2 = exp2.copy_support()
        if s1 is None and s2 is None:
            warnings.warn("Support union: the expressions are not argument expressions")
            return None
        if s1 is None:
            return s2
        if s2 is None:
            return s1
        return s1.union(s2)
