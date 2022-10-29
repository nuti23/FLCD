
class ProgramInternalForm:
    def __init__(self):
        self.tokens = []

    def add(self, token, index):
        self.tokens.append((token, index))

    def __str__(self):
        out = ''
        for token in self.tokens:
            out = out + "index: " + str(token[1]) + "   token: " + str(token[0]) + "\n"
        return out
