class Individual:
    def __init__(self, n, *f):
        self._id = n
        if f:
            self._fitness = f
        else:
            self._fitness = 1.0

    def get_id(self):
        return self._id

    def get_fitness(self):
        return self._fitness

    def __repr__(self):
        return str(self._id)


ind = Individual(42)
print(ind.get_id())
print(ind.get_fitness())

ind = Individual(30, 0.8)
print(ind.get_id())
print(ind.get_fitness())
