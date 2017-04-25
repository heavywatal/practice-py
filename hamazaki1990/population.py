class Individual:
    def __init__(self, n):
        self._id = n


class Population:
    def __init__(self, size):
        for x in range(size):
            ix = Individual(x)
        self._individuals = [ix]

    def print_ids(self):
        print(self._individuals)


p1 = Population(10)
print(p1._individuals)
p1.print_ids
