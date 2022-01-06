from logics.senteces.Expression import Expression
from logics.Constants import iff_keywords, separator, complete_negation
from logics.senteces.ParseExceptions import ParseException
from utils.Utils import tokenize


class IffExpression(Expression):
    def __init__(self, *args):
        if len(args) <= 2:
            super().__init__(*args)

            self.left_expression = None
            self.right_expression = None
            self.connection_keyword = None

            # Go over each connection key word
            for iff_keyword in iff_keywords:
                # Go over each word and create expression split by keyword
                keyword_tokens = iff_keyword.split(" ")
                if contains_sub_array(self.tokens, keyword_tokens):
                    from logics.senteces.Helper import create_expression

                    keyword_begin_idx = self.tokens.index(keyword_tokens[0])
                    keyword_end_idx = keyword_begin_idx + len(keyword_tokens)
                    # Create the expressions from the left and right tokens
                    self.left_expression = create_expression(
                        separator.join(self.tokens[:keyword_begin_idx]),
                        self.copy_support(),
                    )
                    self.right_expression = create_expression(
                        separator.join(self.tokens[keyword_end_idx:]),
                        self.copy_support(),
                    )
                    self.connection_keyword = iff_keyword
                    break

            if self.connection_keyword is None:
                raise ParseException("If and only if without a keyword")
        else:
            # Copy constructor
            self.count_id()
            self.negated = args[0]
            self.left_expression = args[1]
            self.right_expression = args[2]
            self.connection_keyword = args[3]
            self.support = args[4]
            self.defeasible = args[5]
            self.defeasible_keyword = args[6]
            self.tokenize_expression()

    def tokenize_expression(self):
        """
        Create the tokens of the expression based on detected elements
        """
        self.tokens = tokenize(self.get_string_rep())

    def get_string_rep(self, include_defeasible=False):
        """
        Splice expression back together with the negation word
        :return: The string representation of the expression
        """
        str = f'{(complete_negation + " ") if self.negated else ""}{self.left_expression.get_string_rep()} {self.connection_keyword} {self.right_expression.get_string_rep()}'

        return (self.defeasible_keyword + " "
                if self.defeasible and include_defeasible
                else "") + str

    def reverse_expression(self):
        """
        Function that flips the negated bit
        :return: The hypothesis reversed
        """
        return IffExpression(
            not self.negated,
            self.left_expression,
            self.right_expression,
            self.connection_keyword,
            self.copy_support(),
            self.defeasible,
            self.defeasible_keyword
        )

    def copy(self):
        """
        Copy function that calls the copy constructor for a new clean object
        :return: The new object
        """
        return IffExpression(
            self.negated,
            self.left_expression,
            self.right_expression,
            self.connection_keyword,
            self.copy_support(),
            self.defeasible,
            self.defeasible_keyword
        )

    def replace_variable(self, replace, replace_with):
        pass


def contains_sub_array(array, subarray):
    return [
        x
        for x in range(len(array) - len(subarray) + 1)
        if array[x: x + len(subarray)] == subarray
    ]
