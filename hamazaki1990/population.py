import random
from individual import Individual


class Population:
    def __init__(self, size):
        self._inds = [Individual(x) for x in range(size)]

    def print_ids(self):
        print(self._inds)

    def next_genwf(self):
        n = len(self._inds)
        self._inds = [self._inds[random.randrange(n)] for x in range(n)]

    def next_genmo(self):
        n = len(self._inds)
        self._inds[random.randrange(n)] = self._inds[random.randrange(n)]


p1 = Population(10)

for t in range(20):
    p1.print_ids()
    p1.next_genwf()

p2 = Population(10)

for t in range(20):
    p2.print_ids()
    p2.next_genmo()
