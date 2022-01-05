from logics.Constants import (
    negation_keywords,
    separator,
    base_filler_words,
    prepositions,
)
from logics.senteces.Expression import Expression
from logics.senteces.ParseExceptions import ParseException
from logics.senteces.UnifiableVariable import UnifiableVariable
from utils.Utils import tokenize, create_new_object, check_if_list_in_list


class BaseExpressionWithPreposition(Expression):
    """
    The base expression or ground term.
    Peter plays football ... The chair is furniture .. Peter must have eaten
    """

    def __init__(self, *args):
        # When we have only one input it must be a sentence
        if len(args) <= 2:
            # Call the constructor of the Expression
            super().__init__(*args)

            # Get whether the sentence is negated
            self.negation_word = "not"
            for negation_keyword in negation_keywords:
                if type(negation_keyword) == list:
                    found_index = check_if_list_in_list(negation_keyword, self.tokens)
                    if found_index is not None:
                        self.negation_word = negation_keyword
                        self.negated = True
                        break
                elif negation_keyword in self.tokens:
                    self.negated = True
                    self.negation_word = negation_keyword
                    break

            # Remove the negation keyword
            if self.negated:
                if type(self.negation_word) == list:
                    del self.tokens[found_index : found_index + len(self.negation_word)]
                else:
                    self.tokens.remove(self.negation_word)

            # Go over all possible filler words and add them to the allowed list
            extra_allowed = 0
            number_of_prepositions = 0
            for token in self.tokens:
                if token in base_filler_words:
                    extra_allowed += 1
                if token in prepositions:
                    number_of_prepositions += 1

            # Only allow subject verb object1 preposition object2 terms
            # with the restriction of at most 1 preposition
            if (
                len(self.tokens) - extra_allowed != 5
                and len(self.tokens) - extra_allowed != 4
            ):
                raise ParseException(
                    f"This base expression with preposition is not supported: {self.init_hypo}"
                )
            elif number_of_prepositions > 1 or number_of_prepositions == 0:
                raise ParseException(
                    f"This base expression with preposition is not supported, the number of prepositions is greater or lower than the allowed: {self.init_hypo}"
                )

            # Get the subject verb and objects with their filler words
            start_index = 0
            end_index = 1
            fill_counter = 0
            for token in self.tokens:
                if token in base_filler_words:
                    end_index += 1
                else:
                    if fill_counter == 0:
                        self.subject = separator.join(
                            self.tokens[start_index:end_index]
                        )
                    elif fill_counter == 1:
                        self.verb = separator.join(self.tokens[start_index:end_index])
                    elif fill_counter == 2:
                        self.object1 = separator.join(
                            self.tokens[start_index:end_index]
                        )
                    elif fill_counter == 3:
                        self.preposition = separator.join(
                            self.tokens[start_index:end_index]
                        )
                    elif fill_counter == 4:
                        self.object2 = separator.join(
                            self.tokens[start_index:end_index]
                        )
                    fill_counter += 1
                    start_index = end_index
                    end_index = start_index + 1
            if len(self.tokens) - extra_allowed == 4:
                self.object2 = ""
        else:
            # Copy constructor
            self.count_id()
            self.negated = args[0]
            self.negation_word = args[1]
            self.subject = args[2]
            self.verb = args[3]
            self.object1 = args[4]
            self.preposition = args[5]
            self.object2 = args[6]
            self.support = args[7]
            self.defeasible = args[8]

        self.tokenize_expression()

    def tokenize_expression(self):
        """
        Create the tokens of the expression based on detected elements
        """
        if self.negated:
            if type(self.negation_word) == list:
                self.tokens = tokenize(
                    f"{self.subject} {separator.join(self.negation_word)} {self.verb} {self.object1} {self.preposition} {self.object2}"
                )
            elif "do" in self.negation_word:
                self.tokens = tokenize(
                    f"{self.subject} {self.negation_word} {self.verb} {self.object1} {self.preposition} {self.object2}"
                )
            else:
                self.tokens = tokenize(
                    f"{self.subject} {self.verb} {self.negation_word} {self.object1} {self.preposition} {self.object2}"
                )
        else:
            self.tokens = tokenize(
                f"{self.subject} {self.verb} {self.object1} {self.preposition} {self.object2}"
            )

    def reverse_expression(self):
        """
        Function that flips the negated bit
        :return: The hypothesis reversed
        """
        return BaseExpressionWithPreposition(
            not self.negated,
            self.negation_word,
            self.subject,
            self.verb,
            self.object1,
            self.preposition,
            self.object2,
            self.copy_support(),
            self.defeasible,
        )

    def replace_variable(self, replace, replace_with):
        """
        Replace the subject or object if they match the to be replaced variable
        :param replace:      To be replaced with variable
        :param replace_with: The Variable it needs to be replaced with
        :return: A new expression with the replaced variables
        """
        new_base_expression = self.copy()
        if new_base_expression.subject == replace:
            new_base_expression.subject = replace_with
        if new_base_expression.object1 == replace:
            new_base_expression.object1 = replace_with
        if new_base_expression.object2 == replace:
            new_base_expression.object2 = replace_with
        new_base_expression.tokenize_expression()
        return new_base_expression

    def is_contradiction_of(self, clause, list_of_new_objects):
        """
        Get whether the given clause is a contradiction of this clause
        :param clause:               The comparative clause
        :param list_of_new_objects:  List of new objects in case we need to create a new one
        :return: True and the unification replacements if it is a tautologie otherwise False
        """
        # Base expression with preposition only match base expression with preposition
        if type(clause) is not BaseExpressionWithPreposition:
            return False, None

        # If the negation is equal cant be the opposite
        if clause.negated == self.negated:
            return False, None

        unification_replacements = []

        # Check whether the object or subject is unified variable and replace it respectively
        for variable, comp_var in [
            (self.object2, clause.object2),
            (self.preposition, clause.preposition),
            (self.object1, clause.object1),
            (self.subject, clause.subject),
        ]:
            if type(variable) == UnifiableVariable:
                if type(comp_var) == UnifiableVariable:
                    # When both are unified variables you have to introduce a new variable
                    new_object = create_new_object(list_of_new_objects)
                    unification_replacements.append((new_object, variable))
                    unification_replacements.append((new_object, comp_var))
                else:
                    # Only one then replace with opposite
                    unification_replacements.append((comp_var, variable))
            else:
                if type(comp_var) == UnifiableVariable:
                    # Only one then replace with opposite
                    unification_replacements.append((variable, comp_var))
                else:
                    # None are unified variables so just compare the vars
                    if variable != comp_var:
                        return False, None

        # Everything fine so far check for the verb
        if self.verb != clause.verb:
            return False, None

        # It is a match.. replace the unification variables
        return True, unification_replacements

    def get_string_rep(self):
        """
        Splice the subject, verb and object together with the negation word
        :return: The string representation of the expression
        """
        return separator.join(self.tokens)

    def copy(self):
        """
        Copy function that calls the copy constructor for a new clean object
        :return: The new object
        """
        return BaseExpressionWithPreposition(
            self.negated,
            self.negation_word,
            self.subject,
            self.verb,
            self.object1,
            self.preposition,
            self.object2,
            self.copy_support(),
            self.defeasible,
        )
