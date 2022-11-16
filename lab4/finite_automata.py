
class FiniteAutomata:
    def __init__(self, Q, A, q0, F, S):
        # states
        self.Q = Q
        # alphabet
        self.A = A
        # initial state
        self.q0 = q0
        # final state
        self.F = F
        # transitions
        self.delta = S

    def is_dfa(self):
        print("keys: ")
        for elem in self.delta.keys():
            print(elem, self.delta[elem])
            if len(self.delta[elem]) > 1:
                return False
        return True

    def is_accepted(self, sequence):
        if self.is_dfa():
            current = self.q0
            print("steps: ")
            for symbol in sequence:
                if (current, symbol) in self.delta.keys():
                    current = self.delta[(current, symbol)][0]
                    print(current, symbol)
                else:
                    return False
            return current in self.F
        return False

