import random
from individual import Individual


class Population:
    def __init__(self, size, mt=0, s=0):
        self._mfit = 1 + s
        self._wnum = int(size*(1-mt))
        self._mnum = int(size*mt)
        self._minds = [Individual(x, self._mfit) for x in range(self._mnum)]
        self._winds = [Individual(x + self._mnum) for x in range(self._wnum)]
        self._inds = self._minds + self._winds

    def print_ids(self):
        print(self._inds)

    def print_fitness(self):
        fit = [x.get_fitness() for x in self._inds]
        print(fit)

    def next_genwf(self):
        n = len(self._inds)
        self._inds = [self._inds[random.randrange(n)] for x in range(n)]

    def next_genmo(self):
        n = len(self._inds)
        self._inds[random.randrange(n)] = self._inds[random.randrange(n)]


p1 = Population(10, 0.3, -0.2)
p1.print_ids()
p1.print_fitness()
