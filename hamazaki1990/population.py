import random
from individual import Individual


def roulettechoice(individuals, cumsum_fitness):
    r = random.uniform(0.0, max(cumsum_fitness))
    for i in range(len(cumsum_fitness)):
        if r < cumsum_fitness[i]:
            return individuals[i]


class Population:
    def __init__(self, n, mutant=0, s=0, mutationrate=0.0):
        num_mutant = int(n * mutant)
        mutant_inds = [Individual(x, 1 + s, mutationrate) for x in range(num_mutant)]
        wild_inds = [Individual(x, 1, mutationrate) for x in range(num_mutant, n)]
        self._inds = mutant_inds + wild_inds

    def get_ids(self):
        return self._inds

    def get_fitnesses(self):
        fitness = [x.get_fitness() for x in self._inds]
        return fitness

    def get_mutantfreq(self):
        fitness = [x.get_fitness() for x in self._inds]
        mutantfreq = 1 - fitness.count(1.0)/len(fitness)
        return mutantfreq

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

    def acquire_mutations(self):
        [x.acquire_mutation() for x in self._inds]
        genotypes = [x.get_genotype() for x in self._inds]
        return genotypes

    def list_mutation(self):
        genotypes = [x.get_genotype() for x in self._inds]
        m_sites = []
        for x in genotypes:
            m_sites.extend(x)
        m_sites = sorted(m_sites)
        m_list = [[0 for x in range(len(m_sites))] for y in range(len(self._inds))]
        for i in range(len(self._inds)):
            for j in range(len(genotypes[i])):
                k = m_sites.index(genotypes[i][j])
                if k != "ValueError":
                    m_list[i][k] += 1
        print(m_list)

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
    print(p1_2.get_mutantfreq())

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

    p3_1 = Population(10, 0, 0, 0.8)
    p3_1.list_mutation()
    print(p3_1.acquire_mutations())
    p3_1.list_mutation()
    print(p3_1.acquire_mutations())
    p3_1.list_mutation()


if __name__ == '__main__':
    main()
