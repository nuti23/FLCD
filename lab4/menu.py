from input_operation import ReadInput


class Menu:
    def __init__(self):
        self.read_input = ReadInput()
        self.finite_automata = self.read_input.read_file('FA.in')

    def get_states(self):
        print(self.finite_automata.Q)

    def get_alphabet(self):
        print(self.finite_automata.A)

    def get_final_states(self):
        print(self.finite_automata.F)

    def get_initial_state(self):
        print(self.finite_automata.q0)

    def get_transitions(self):
        print(self.finite_automata.delta)

    def is_dfa(self):
        print(self.finite_automata.is_dfa())

    def is_accepted(self):
        sequence = input('Read sequence:')
        print(self.finite_automata.is_accepted(sequence))

    def menu(self):
        print("0) Exit")
        print("1) States")
        print("2) Alphabet")
        print("3) Initial state")
        print("4) Final states")
        print("5) Transitions")
        print("6) Is DFA?")
        print("7) Is accepted?")


    def run(self):
        commands = {'1': self.get_states, '2': self.get_alphabet, '3': self.get_initial_state,
                    '4': self.get_final_states, '5': self.get_transitions, '6': self.is_dfa,
                    '7': self.is_accepted}
        exit = False
        while not exit:
            self.menu()
            print("enter command: ")
            command = input()
            if command in commands.keys():
                commands[command]()
            elif command == '0':
                exit = True
            else:
                print("wrong command! try again")

