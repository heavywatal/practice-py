import random
from individual import Individual


def roulettechoice(seq1, seq2):
    r = random.random()
    for a in range(len(seq2)):
        if r < seq2[a]:
            break
    return seq1[a]


class Population:
    def __init__(self, n, mutantrate=0, s=0):
        num_wild = int(n*(1-mutantrate))
        num_mutant = int(n*mutantrate)
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
        s_fit = [sum(fitness[0: x + 1])/sum(fitness) for x in range(size)]
        next_generation = []
        for x in range(size):
            next_generation.append(roulettechoice(self._inds, s_fit))
        self._inds = next_generation

    def next_genmo(self):
        fitness = [x.get_fitness() for x in self._inds]
        size = len(self._inds)
        s_fit = [sum(fitness[0: x + 1])/sum(fitness) for x in range(size)]
        self._inds[random.randrange(size)] = roulettechoice(self._inds, s_fit)


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
