#! /usr/local/bin/env python
# -*- coding: utf-8 -*-
import random


class Individual:
    def __init__(self, idn, fitnes):
        self._id = idn
        self._fit = fitnes

    @property
    def id(self):
        return(self._id)

    @property
    def fit(self):
        return(self._fit)

    def __repr__(self):
        return(str(self._id))


class Population:
    def __init__(self, population_n, *input_fit_ls):
        self._individuals = []

        if (population_n != len(input_fit_ls))and(len(input_fit_ls) != 0):
            print("inputed fitness list length is not equal to populetion num")
            print("so "+str(len(input_fit_ls))+"(inputed fitness list", end='')
            print(" length)/"+str(population_n), end='')
            print(" from the front fitness set to inputed fitnes")
        fit_ls = [1] * population_n
        fit_ls[:len(input_fit_ls)] = input_fit_ls
        for i in range(population_n):
            self._individuals.append(Individual(i, fit_ls[i]))

    def print_id_list(self):
        for individual in self._individuals:
            print(individual.id, end=' ')
        print('')

    def print_id(self):
        print(self._individuals)

    def get_fitls(self):
        fit_ls = []
        for ind in self._individuals:
            fit_ls.append(ind.fit)
        return(fit_ls)

    def wright_fisher_model(self):
        next_gen = random.choices(self._individuals,
                                  weights=self.get_fitls(),
                                  k=len(self._individuals))
        self._individuals = sorted(next_gen, key=lambda ind: ind.id)

    def moran_model(self):
        i_dying = random.randrange(len(self._individuals))
        self._individuals[i_dying] = random.choices(self._individuals,
                                                    weights=self.get_fitls())[0]
        self._individuals.sort(key=lambda ind: ind.id)


print("wright_fisher")
sample_pwf = Population(10, 1.5, 1.5, 1.5, 1.5, 1.5)
sample_pwf.print_id()
print("go to next generation wright_fisher model")
sample_pwf.wright_fisher_model()
sample_pwf.print_id()
print("go to next generation again wright_fisher model")
sample_pwf.wright_fisher_model()
sample_pwf.print_id()

print("\nmoran model")
sample_pm = Population(10, 1.5, 1.5, 1.5, 1.5, 1.5)
sample_pm.print_id()
print("go to next generation moran model")
sample_pm.moran_model()
sample_pm.print_id()
print("go to next generation again moran model")
sample_pm.moran_model()
sample_pm.print_id()
