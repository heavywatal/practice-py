from individual import Individual


class Population:
    def __init__(self, size):
        self._individuals = [Individual(x) for x in range(size)]

    def print_ids(self):
        print(self._individuals)


p1 = Population(10)
print(p1._individuals)
p1.print_ids
