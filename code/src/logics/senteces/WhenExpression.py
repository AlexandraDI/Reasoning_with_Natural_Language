import re

from logics.Constants import (
    when_left_regex,
    when_right_regex,
    complete_negation,
    separator,
    defeasible_indicators,
)
from logics.senteces.Expression import Expression
from logics.senteces.ParseExceptions import ParseException
from utils.Utils import tokenize, get_sentences_key_words


class WhenExpression(Expression):
    """
    Class representing the "when Expression then Expression" sentence
    """

    def __init__(self, *args):
        # When we have only one input it must be a sentence
        if len(args) <= 2:
            # Call the constructor of the Expression
            super().__init__(*args)

            self.left_match = None
            self.key_words = None

            # self.defeasible = False
            # self.defeasible_keyword = None
            # for defeasible_indicator in defeasible_indicators:
            #     if self.tokens[0] == defeasible_indicator:
            #         self.defeasible_keyword = defeasible_indicator
            #         self.defeasible = True
            #         self.tokens = self.tokens[1:]
            #         if self.tokens[0] == ",":
            #             self.tokens = self.tokens[1:]

            # Get the string rep with the overall negation removed
            test_sentence = self.get_string_rep(include_defeasible=False)

            # Check whether we have a left when expression or right when expression
            reg_match = None
            for test_reg, is_left in [
                (when_left_regex, True),
                (when_right_regex, False),
            ]:
                reg_match = re.match(test_reg, test_sentence, re.IGNORECASE)
                if reg_match:
                    self.left_match = is_left
                    break

            if reg_match is None:
                raise ParseException(
                    f"No regex match found for the when expression: \n"
                    f"Original sentence: {test_sentence}"
                )

            # Go over each group and get the sentences between the keywords
            sentences, self.key_words = get_sentences_key_words(
                reg_match, test_sentence
            )

            if len(sentences) != 2:
                raise ParseException(
                    f"The when expression doesn't have two sentences"
                    f"Original sentence: {test_sentence}"
                )

            # Get the when expression that needs to be negated if necessary
            from logics.senteces.Helper import create_expression

            if self.left_match:
                self.premise = create_expression(sentences[0], self.copy_support())
                self.conclusion = create_expression(sentences[1], self.copy_support())
            else:
                self.premise = create_expression(sentences[1], self.copy_support())
                self.conclusion = create_expression(sentences[0], self.copy_support())

        else:
            # Copy constructor
            self.count_id()
            self.negated = args[0]
            self.defeasible = args[1]
            self.defeasible_keyword = args[2]
            self.premise = args[3]
            self.conclusion = args[4]
            self.left_match = args[5]
            self.key_words = args[6]
            self.support = args[7]
            self.defeasible = args[8]
            self.tokenize_expression()

    def tokenize_expression(self):
        """
        Create the tokens of the expression based on detected elements
        """
        sentence = f'{"it is not the case that " if self.negated else ""}'
        sentence += (
            f"{self.key_words[0]} {self.premise.get_string_rep()} {self.key_words[1]} {self.conclusion.get_string_rep()}"
            if self.left_match
            else f"{self.conclusion.get_string_rep()} {self.key_words[0]} {self.premise.get_string_rep()}"
        )

        self.tokens = tokenize(sentence)

    def replace_variable(self, replace, replace_with):
        """
        Replace the all variables if they match the to be replaced variable
        :param replace:      To be replaced with variable
        :param replace_with: The Variable it needs to be replaced with
        :return: A new expression with the replaced variables
        """
        new_when_expression = self.copy()
        new_when_expression.premise = new_when_expression.premise.replace_variable(
            replace, replace_with
        )
        new_when_expression.conclusion = new_when_expression.conclusion.replace_variable(
            replace, replace_with
        )
        new_when_expression.tokenize_expression()
        return new_when_expression

    def reverse_expression(self):
        """
        Function that flips the negated bit
        :return: The hypothesis reversed
        """
        return WhenExpression(
            not self.negated,
            self.defeasible,
            self.defeasible_keyword,
            self.premise,
            self.conclusion,
            self.left_match,
            self.key_words,
            self.copy_support(),
            self.defeasible,
        )

    def copy(self):
        """
        Copy function that calls the copy constructor for a new clean object
        :return: The new object
        """
        return WhenExpression(
            self.negated,
            self.defeasible,
            self.defeasible_keyword,
            self.premise,
            self.conclusion,
            self.left_match,
            self.key_words,
            self.copy_support(),
            self.defeasible,
        )

    def get_string_rep(self, include_defeasible=True):
        str = (
            self.defeasible_keyword + " "
            if self.defeasible and include_defeasible
            else ""
        ) + Expression.get_string_rep(self)
        return str
