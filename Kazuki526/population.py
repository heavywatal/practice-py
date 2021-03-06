#! /usr/local/bin/env python
# -*- coding: utf-8 -*-
import random


class Individual:
    def __init__(self, idn, fitness=1):
        self._id = idn
        self._fitness = fitness

    @property
    def id(self):
        return self._id

    @property
    def fitness(self):
        return self._fitness

    def __repr__(self):
        return str(self._id)


class Population:
    def __init__(self, population_n, mutant_n=0, s=0):
        if population_n < mutant_n:
            exit("ERROR: mutant_n larger than population_n")
        self._individuals = []
        for i in range(population_n):
            if i < mutant_n:
                self._individuals.append(Individual(i, 1 + s))
            else:
                self._individuals.append(Individual(i))

    def print_id_list(self):
        for individual in self._individuals:
            print(individual.id, end=' ')
        print('')

    def print_id(self):
        print(self._individuals)

    def get_fitness_list(self):
        fitness_list = []
        for ind in self._individuals:
            fitness_list.append(ind.fitness)
        return fitness_list

    def wright_fisher_model(self):
        next_gen = random.choices(self._individuals,
                                  weights=self.get_fitness_list(),
                                  k=len(self._individuals))
        self._individuals = sorted(next_gen, key=lambda ind: ind.id)

    def moran_model(self):
        i_dying = random.randrange(len(self._individuals))
        born = random.choices(self._individuals,
                              weights=self.get_fitness_list())[0]
        self._individuals[i_dying] = born
        self._individuals.sort(key=lambda ind: ind.id)


print("wright_fisher　(0~4 fitness 1.5)")
sample_pwf = Population(10, 5, 0.5)
sample_pwf.print_id()
print("go to next generation")
sample_pwf.wright_fisher_model()
sample_pwf.print_id()
print("go to next generation again")
sample_pwf.wright_fisher_model()
sample_pwf.print_id()

print("\nmoran model (0~4 fitness 1.5)")
sample_pm = Population(10, 5, 0.5)
sample_pm.print_id()
print("go to next generation")
sample_pm.moran_model()
sample_pm.print_id()
print("go to next generation again")
sample_pm.moran_model()
sample_pm.print_id()
