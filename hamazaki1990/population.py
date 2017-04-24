class Individual:
    def __init__(self, n):
        self._id = n


class Population(Individual):
    def __init__(self, size):
        super().__init__(size)
        self._individuals = [self._id]

    def print_ids(self):
        print(self._individuals)


p1 = Population(10)
print(p1._individuals)
p1.print_ids
