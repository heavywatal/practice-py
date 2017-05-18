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


csvfile1 = open("allelechangewf.csv", "w", encoding="utf-8")
writer = csv.writer(csvfile1)
p1 = Population(10, 0.1, 0.5)
fixprocesswf = change_allelewf(p1)
writer.writerow(["generation", "derived_allele_frequency"])
for x in range(len(fixprocesswf)):
    writer.writerow(fixprocesswf[x])

csvfile2 = open("allelechangemo.csv", "w", encoding="utf-8")
writer = csv.writer(csvfile2)
p1 = Population(10, 0.1, 0.5)
fixprocessmo = change_allelemo(p1)
writer.writerow(["generation", "derived_allele_frequency"])
for x in range(len(fixprocessmo)):
    writer.writerow(fixprocessmo[x])
