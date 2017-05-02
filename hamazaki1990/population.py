import random
from individual import Individual


def roulettechoice(individuals, cumsum_fitness):
    r = random.uniform(0.0, max(cumsum_fitness))
    for i in range(len(cumsum_fitness)):
        if r < cumsum_fitness[i]:
            return individuals[i]


class Population:
    def __init__(self, n, mutantrate=0, s=0):
        num_mutant = int(n * mutantrate)
        mutant_inds = [Individual(x, 1 + s) for x in range(num_mutant)]
        wild_inds = [Individual(x) for x in range(num_mutant, n)]
        self._inds = mutant_inds + wild_inds

    def print_ids(self):
        print(self._inds)

    def print_fitness(self):
        fitness = [x.get_fitness() for x in self._inds]
        print(fitness)

    def next_genwf(self):
        fitness = [x.get_fitness() for x in self._inds]
        size = len(self._inds)
        cumsum_fitness = [sum(fitness[:i]) for i in range(1, size + 1)]
        next_generation = []
        for x in range(size):
            next_generation.append(roulettechoice(self._inds, cumsum_fitness))
        self._inds = next_generation

    def next_genmo(self):
        fitness = [x.get_fitness() for x in self._inds]
        size = len(self._inds)
        cumsum_fitness = [sum(fitness[:i]) for i in range(1, size + 1)]
        i_dying = random.randrange(size)
        self._inds[i_dying] = roulettechoice(self._inds, cumsum_fitness)


p1_1 = Population(10)
p1_1.print_ids()
p1_1.print_fitness()

for x in range(20):
    p1_1.next_genwf()
    p1_1.print_ids()
p1_1.print_fitness()

p1_2 = Population(10, 0.3, 0.2)
p1_2.print_ids()
p1_2.print_fitness()

for x in range(20):
    p1_2.next_genwf()
    p1_2.print_ids()
p1_2.print_fitness()


p2_1 = Population(10)
p2_1.print_ids()
p2_1.print_fitness()

for x in range(20):
    p2_1.next_genmo()
    p2_1.print_ids()
p2_1.print_fitness()

p2_2 = Population(10, 0.3, 0.2)
p2_2.print_ids()
p2_2.print_fitness()

for x in range(20):
    p2_2.next_genmo()
    p2_2.print_ids()
p2_2.print_fitness()
