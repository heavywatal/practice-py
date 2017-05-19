import csv
from population import Population


def change_allelewf(population):
    t = 0
    fixprocess = [[t, population.get_mutantfreq()]]
    while population.mutation_is_not_fixed():
        t += 1
        population.next_genwf()
        fixprocess.append([t, population.get_mutantfreq()])
    return fixprocess


def change_allelemo(population):
    t = 0
    fixprocess = [[t, population.get_mutantfreq()]]
    while population.mutation_is_not_fixed():
        t += 1
        population.next_genmo()
        fixprocess.append([t, population.get_mutantfreq()])
    return fixprocess


def output_allelechange(filename, population, function):
    with open(filename, "w", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["generation", "derived_allele_frequency"])
        fixprocess = function(population)
        for x in range(len(fixprocess)):
            writer.writerow(fixprocess[x])


p1 = Population(10, 0.1, 0.2)
output_allelechange("allelefreqwf.csv", p1, change_allelewf)

p2 = Population(10, 0.1, 0.5)
output_allelechange("allelefreqmo.csv", p2, change_allelemo)
