from finite_automata import FiniteAutomata


class ReadInput:

    def split_line(self, line):
        return line.strip().split(' ')[2:]

    def read_file(self, filename):
        with open(filename) as f:
            Q = self.split_line(f.readline())
            A = self.split_line(f.readline())
            q0 = self.split_line(f.readline())[0]
            F = self.split_line(f.readline())

            f.readline()

            transitions = {}
            for line in f:
                split = line.strip().split('->')
                assignment = split[0].strip().replace('(', '').replace(')', '').split(',')
                source = assignment[0]
                route = assignment[1]
                destination = split[1].strip()

                # print(source + " " + route + " " + destination)

                if (source, route) in transitions.keys():
                    transitions[(source, route)].append(destination)
                else:
                    transitions[(source, route)] = [destination]

            return FiniteAutomata(Q, A, q0, F, transitions)





