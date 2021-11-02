from logics.senteces.Expression import Expression
from logics.Constants import iff_keywords, separator
from logics.senteces.ParseExceptions import ParseException
from utils.Utils import tokenize


class IffExpression(Expression):
    def __init__(self, *args):
        if len(args) == 1:
            super().__init__(args[0])

            self.left_expression = None
            self.right_expression = None
            self.connection_keyword = None

            # Go over each connection key word
            for iff_keyword in iff_keywords:
                # Go over each word and create expression split by keyword
                if iff_keyword in self.tokens:
                    from logics.senteces.Helper import create_expression
                    keyword_idx = self.tokens.index(iff_keyword)
                    # Create the expressions from the left and right tokens
                    self.left_expression = create_expression(separator.join(self.tokens[:keyword_idx]))
                    self.right_expression = create_expression(separator.join(self.tokens[keyword_idx + 1:]))
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
            self.tokenize_expression()

    def tokenize_expression(self):
        """
        Create the tokens of the expression based on detected elements
        """
        self.tokens = tokenize(
            self.get_string_rep()
        )

    def get_string_rep(self):
        """
        Splice expression back together with the negation word
        :return: The string representation of the expression
        """
        return f'{self.left_expression.get_string_rep()} {self.connection_keyword} {self.right_expression.get_string_rep()}'

    def reverse_expression(self):
        """
        Function that flips the negated bit
        :return: The hypothesis reversed
        """
        return IffExpression(
            not self.negated,
            self.left_expression,
            self.right_expression,
            self.connection_keyword
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
            self.connection_keyword
        )

    def replace_variable(self, replace, replace_with):
        pass