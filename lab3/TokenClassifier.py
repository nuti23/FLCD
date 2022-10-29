class TokenClassifier:

    def __init__(self):
        self.separators = []
        self.operators = []
        self.reservedWords = []
        self.classify()

    def classify(self) -> None:
        with open('files/token.in', 'r') as f:
            for i in range(14):
                separator = f.readline().strip()
                if separator == "space":
                    separator = " "
                self.separators.append(separator)
            for i in range(20):
                operator = f.readline().strip()
                self.operators.append(operator)
            for i in range(11):
                reserved_word = f.readline().strip()
                self.reservedWords.append(reserved_word)
