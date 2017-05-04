#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Individual class
"""


class Individual:
    def __init__(self, number=0, fitness=1.0):
        self._id = number
        self._fitness = fitness

    @property
    def id(self):
        return self._id

    @property
    def fitness(self):
        return self._fitness

    def __str__(self):
        return '{}'.format(self.id)


def main():
    individual = Individual(42)
    print(individual)
    print(individual.id)
    print(individual.fitness)


if __name__ == '__main__':
    main()
