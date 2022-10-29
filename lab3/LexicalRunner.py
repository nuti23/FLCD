from ProgamInternalForm import ProgramInternalForm
from Scanner import Scanner
from SymbolTable import SymbolTable


class LexicalRunner:
    def __init__(self):
        self.ST = SymbolTable(10)
        self.PIF = ProgramInternalForm()
        self.scanner = Scanner()

    def run(self, file):
        error_message = ''
        separators = self.scanner.get_separators()
        operators = self.scanner.get_operators()
        reserved_words = self.scanner.get_reserved_words()

        with open(file, 'r') as f:
            line_number = 1
            for line in f:
                tokens = self.scanner.get_tokens(line.strip())
                for i in range(len(tokens)):
                    if tokens[i] in reserved_words + separators + operators:
                        if tokens[i] != ' ':
                            self.PIF.add(tokens[i], 0)
                    elif self.scanner.is_identifier(tokens[i]):
                        id = self.ST.add(tokens[i])
                        self.PIF.add("id", id)
                    elif self.scanner.is_constant(tokens[i]):
                        const = self.ST.add(tokens[i])
                        self.PIF.add("const", const)
                    else:
                        error_message += 'line ' + str(line_number) + ': lexical error at token ' + tokens[i] + "\n"
                line_number += 1

        with open('files/st.out', 'w') as writer:
            writer.write(str(self.ST))
        with open('files/pif.out', 'w') as writer:
            writer.write(str(self.PIF))
        if error_message == '':
            print("Program " + file + ' is lexically correct' + '\n')
        else:
            print("Program " + file + ' is NOT lexically correct: ')
            print(error_message)