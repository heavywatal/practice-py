#! /usr/local/bin/env python
# -*- coding: utf-8 -*-
import random


class Individual:
    def __init__(self, idn):
        self._id = idn

    @property
    def id(self):
        return(self._id)

    def __repr__(self):
        return(str(self._id))


class Population:
    def __init__(self, population_n):
        self._individuals = []
        for i in range(population_n):
            self._individuals.append(Individual(i))

    def print_id_list(self):
        for individual in self._individuals:
            print(individual.id, end=' ')
        print('')

    def print_id(self):
        print(self._individuals)

    def wright_fisher_model(self):
        next_gen = []
        for pn in range(len(self._individuals)):
            next_gen.append(random.choice(self._individuals))
        self._individuals = sorted(next_gen, key=lambda ind: ind.id)


sample_population = Population(10)
sample_population.print_id()
print("go to next generation")
sample_population.wright_fisher_model()
sample_population.print_id()
print("go to next generation again")
sample_population.wright_fisher_model()
sample_population.print_id()
