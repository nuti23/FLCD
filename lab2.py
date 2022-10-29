from math import floor


class SymbolTable:

    def __init__(self, size: int):
        self.symbol_table = [[] for _ in range(size)]
        self.size = size
        self.constant = 0.2

    def get_symbolTable(self):
        return self.symbol_table

    def get_string_sum(self, token):
        sum = 0
        for char in token:
            # ord() returns ascii code
            sum += ord(char)
        return sum

    def hash_function(self, token):
        # multiplication method
        # floor() returns int part
        return floor(self.size * (self.get_string_sum(token) * self.constant % 1))

    def get_position(self, token):
        pos = self.hash_function(token)
        index = 0
        for item in self.symbol_table[pos]:
            if item != token:
                index += 1
            else:
                break
        return pos, index

    def is_there(self, token):
        pos = self.hash_function(token)
        if token in self.symbol_table[pos]:
            return True
        else:
            return False

    def add(self, token):
        if self.is_there(token):
            return self.get_position(token)
        pos = self.hash_function(token)
        self.symbol_table[pos].append(token)
        return self.get_position(token)


if __name__ == '__main__':

    symbol_table = SymbolTable(100)
    print(symbol_table.add("var"))
    print(symbol_table.add("a"))
    print(symbol_table.add("_var"))
    print(symbol_table.add("ab"))
    print(symbol_table.add("ba"))




