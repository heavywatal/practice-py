#! /usr/local/bin/env python


class Individual:
    def __init__(self, idn):
        self._id = idn

    @property
    def id(self):
        return(self._id)


class Population:
    def __init__(self, population_n):
        self._individuals = []
        for i in range(population_n):
            self._individuals.append(Individual(i))

    def print_id_list(self):
        for individual in self._individuals:
            print(individual.id, end=' ')
        print('')


sample_population = Population(10)
sample_population.print_id_list()
