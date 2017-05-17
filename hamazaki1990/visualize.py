import csv
import pandas as pd
from population import Population


def change_allelewf(population):
    fit_list = population.get_fitnesses()
    fixprocess = [1 - fit_list.count(1.0)/len(fit_list)]
    while population.mutation_is_not_fixed():
        population.next_genwf()
        fit_list = population.get_fitnesses()
        mutantrate = 1 - fit_list.count(1.0)/len(fit_list)
        fixprocess.append(mutantrate)
    return fixprocess


def change_allelemo(population):
    fit_list = population.get_fitnesses()
    fixprocess = [1 - fit_list.count(1.0)/len(fit_list)]
    while population.mutation_is_not_fixed():
        population.next_genmo()
        fit_list = population.get_fitnesses()
        mutantrate = 1 - fit_list.count(1.0)/len(fit_list)
        fixprocess.append(mutantrate)
    return fixprocess


csvfile1 = open("allelechangewf.csv", "w", encoding="utf-8")
writer = csv.writer(csvfile1)
p1 = Population(10, 0.1, 0.5)
writer.writerow(change_allelewf(p1))


p2 = Population(10, 0.1, 0.5)
print(change_allelemo(p2))
