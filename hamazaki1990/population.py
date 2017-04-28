import random
from individual import Individual


class Population:
    def __init__(self, n, mt=0, s=0):
        mfit = 1 + s
        wnum = int(n*(1-mt))
        mnum = int(n*mt)
        self._minds = [Individual(x, mfit) for x in range(mnum)]
        self._winds = [Individual(x + mnum) for x in range(wnum)]
        self._inds = self._minds + self._winds

    def print_ids(self):
        print(self._inds)

    def print_fitness(self):
        fit = [x.get_fitness() for x in self._inds]
        print(fit)

    def next_genwf(self):
        fit = [x.get_fitness() for x in self._inds]
        n = len(self._inds)
        w = sum(fit)
        nextgen = []
        for y in range(n):
            r = random.random()
            for x in range(n):
                if sum(fit[0: x])/w <= r < sum(fit[0: x + 1])/w:
                    nextgen.append(self._inds[x])
        self._inds = nextgen

    def next_genmo(self):
        fit = [x.get_fitness() for x in self._inds]
        n = len(self._inds)
        w = sum(fit)
        for x in range(n):
            if sum(fit[0: x])/w <= random.random() < sum(fit[0: x + 1])/w:
                self._inds[random.randrange(n)] = self._inds[x]


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
