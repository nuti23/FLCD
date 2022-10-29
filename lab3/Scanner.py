from TokenClassifier import TokenClassifier
from re import *


class Scanner:
    def __init__(self):
        self.classifier = TokenClassifier()

    def get_operators(self):
        return self.classifier.separators

    def get_separators(self):
        return self.classifier.operators

    def get_reserved_words(self):
        return self.classifier.reservedWords

    def is_identifier(self, token):
        return match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def is_constant(self, token):
        return match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    def is_part_of_operator(self, char):
        for op in self.classifier.operators:
            if char in op:
                return True
        return False

    def get_operator_token(self, line, index):
        token = ''
        while index < len(line) and self.is_part_of_operator(line[index]):
            token += line[index]
            index += 1
        return token, index

    def get_string_token_from_line(self, line, index):
        string = ''
        qoutes = 0
        while index < len(line) and qoutes < 2:
            if line[index] == '\'':
                qoutes += 1
            string += line[index]
            index += 1
        return string, index

    def get_tokens(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.is_part_of_operator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.get_operator_token(line, index)
                tokens.append(token)
                token = ''  # reset token
            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.get_string_token_from_line(line, index)
                tokens.append(token)
                token = ''  # reset token
            elif line[index] in self.classifier.separators:
                if token:
                    tokens.append(token)
                token = line[index]
                index += 1
                tokens.append(token)
                token = ''  # reset token
            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens


