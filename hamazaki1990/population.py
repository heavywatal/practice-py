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

    def get_ids(self):
        return self._inds

    def get_fitnesses(self):
        fitness = [x.get_fitness() for x in self._inds]
        return fitness

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

    def is_not_fixed(self):
        for x in range(1, len(self._inds)):
            if self._inds[0] != self._inds[x]:
                return True
        else:
            return False

    def mutation_is_not_fixed(self):
        fitness = [x.get_fitness() for x in self._inds]
        for x in range(1, len(fitness)):
            if fitness[0] != fitness[x]:
                return True
        else:
            return False


def main():
    p1_1 = Population(10)
    print(p1_1.get_ids())
    print(p1_1.get_fitnesses())
    print(p1_1.is_not_fixed())
    print(p1_1.mutation_is_not_fixed())

    for x in range(20):
        p1_1.next_genwf()
        print(p1_1.get_ids())
        print(p1_1.get_fitnesses())
    print(p1_1.is_not_fixed())
    print(p1_1.mutation_is_not_fixed())

    p1_2 = Population(10, 0.3, 0.2)
    print(p1_2.get_ids())
    print(p1_2.get_fitnesses())
    print(p1_2.is_not_fixed())
    print(p1_2.mutation_is_not_fixed())

    for x in range(20):
        p1_2.next_genwf()
        print(p1_2.get_ids())
    print(p1_2.get_fitnesses())
    print(p1_2.is_not_fixed())
    print(p1_2.mutation_is_not_fixed())

    p2_1 = Population(10)
    print(p2_1.get_ids())
    print(p2_1.get_fitnesses())

    for x in range(20):
        p2_1.next_genmo()
        print(p2_1.get_ids())
    print(p2_1.get_fitnesses())

    p2_2 = Population(10, 0.3, 0.2)
    print(p2_2.get_ids())
    print(p2_2.get_fitnesses())

    for x in range(20):
        p2_2.next_genmo()
        print(p2_2.get_ids())
    print(p2_2.get_fitnesses())


if __name__ == '__main__':
    main()
