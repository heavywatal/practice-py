import random
from individual import Individual


class Population:
    def __init__(self, size):
        self._inds = [Individual(x) for x in range(size)]

    def print_ids(self):
        print(self._inds)

    def next_generation(self):
        size = len(self._inds)
        self._inds = [self._inds[random.randrange(size)] for x in range(size)]


p = Population(10)

for t in range(20):
    p.print_ids()
    p.next_generation()
