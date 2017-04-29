import random
from individual import Individual


class Population:
    def __init__(self, n, mt=0, s=0):
        num_wild = int(n*(1-mt))
        num_mutant = int(n*mt)
        mutant_inds = [Individual(x, 1 + s) for x in range(num_mutant)]
        wild_inds = [Individual(x + num_mutant) for x in range(num_wild)]
        self._inds = mutant_inds + wild_inds

    def print_ids(self):
        print(self._inds)

    def print_fitness(self):
        fitness = [x.get_fitness() for x in self._inds]
        print(fitness)

    def next_genwf(self):
        fitness = [x.get_fitness() for x in self._inds]
        size = len(self._inds)
        w = sum(fitness)
        next_generation = []
        for y in range(size):
            r = random.random()
            for x in range(size):
                if sum(fitness[0: x])/w <= r < sum(fitness[0: x + 1])/w:
                    next_generation.append(self._inds[x])
        self._inds = next_generation

    def next_genmo(self):
        fit = [x.get_fitness() for x in self._inds]
        size = len(self._inds)
        w = sum(fit)
        for x in range(size):
            if sum(fit[0: x])/w <= random.random() < sum(fit[0: x + 1])/w:
                self._inds[random.randrange(size)] = self._inds[x]


p1 = Population(10, 0.3, 0.2)
p1.print_ids()
p1.print_fitness()

for x in range(20):
    p1.next_genwf()
    p1.print_ids()
p1.print_fitness()

p2 = Population(10, 0.3, 0.2)
p2.print_ids()
p2.print_fitness()

for x in range(20):
    p2.next_genmo()
    p2.print_ids()
p2.print_fitness()
