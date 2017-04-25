import random
from individual import Individual


class Population:
    def __init__(self, size):
        self._individuals = [Individual(x) for x in range(size)]

    def print_ids(self):
        print(self._individuals)

    def next_generation(self):
        next_individuals = []
        size = len(self._individuals)
        while len(next_individuals) < size:
            next_individuals.append(self._individuals[random.randrange(size)])
        self._individuals = next_individuals


p = Population(10)

for t in range(20):
    p.print_ids()
    p.next_generation()
