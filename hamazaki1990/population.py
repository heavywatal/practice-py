import random
from individual import Individual


class Population:
    def __init__(self, n, mt=0, s=0):
        self._mtfit = 1 + s
        self._mtinds = [Individual(x, self._mtfit) for x in range(int(n*mt))]
        self._wtinds = [Individual(x + int(n*mt)) for x in range(n - int(n*mt))]
        self._inds = self._mtinds + self._wtinds

    def print_ids(self):
        print(self._inds)

    def next_genwf(self):
        n = len(self._inds)
        self._inds = [self._inds[random.randrange(n)] for x in range(n)]

    def next_genmo(self):
        n = len(self._inds)
        self._inds[random.randrange(n)] = self._inds[random.randrange(n)]


p1 = Population(10, 0.3, -0.2)
p1.print_ids()
