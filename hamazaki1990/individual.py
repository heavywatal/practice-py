import random


class Individual:
    def __init__(self, n, f=1.0, mutationrate=0.0):
        self._id = n
        self._fitness = f
        self._genotype = []
        self._mutationrate = mutationrate

    def get_id(self):
        return self._id

    def get_fitness(self):
        return self._fitness

    def get_genotype(self):
        return self._genotype

    def acquire_mutation(self):
        r = random.random()
        next_genotype = self._genotype
        if self._mutationrate > r:
            next_genotype.append(random.random())
        self._genotype = next_genotype

    def __repr__(self):
        return str(self._id)
        return str(self._fitness)
        return str(self._genotype)


def main():
    ind = Individual(42)
    print(ind.get_id())
    print(ind.get_fitness())

    ind2 = Individual(30, 0.8, 1.0)
    print(ind2.get_id())
    print(ind2.get_fitness())
    ind2.acquire_mutation()
    print(ind2.get_genotype())
    ind2.acquire_mutation()
    print(ind2.get_genotype())
    print(ind2.get_id())
    print(ind2.get_fitness())

    ind3 = Individual(0, 1.0, 0.8)
    ind4 = Individual(1, 1.0, 0.8)
    pop = [ind3, ind4]
    print([x.get_genotype() for x in pop])
    [x.acquire_mutation() for x in pop]
    print([x.get_genotype() for x in pop])
    [x.acquire_mutation() for x in pop]
    print([x.get_genotype() for x in pop])


if __name__ == '__main__':
    main()
