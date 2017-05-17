from decimal import Decimal


class Individual:
    def __init__(self, n, f=1.0):
        self._id = n
        self._fitness = f

    def get_id(self):
        return self._id

    def get_fitness(self):
        return self._fitness

    def __repr__(self):
        return str(self._id)
        return Decimal(self._fitness)


def main():
    ind = Individual(42)
    print(ind.get_id())
    print(ind.get_fitness())


if __name__ == '__main__':
    main()
