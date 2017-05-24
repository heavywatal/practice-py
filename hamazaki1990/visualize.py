import csv
from population import Population


def calculate_mutantfreq(population):
    m_list = population.list_mutation()
    m_count = [0 for x in range(len(m_list[0]))]
    for i in m_list:
        for j in m_list[i]:
            if i[j] != 0:
                m_count[j] += 1
    mutantfreq = [x/len(m_list) for x in m_count]
    return mutantfreq


def change_allelewf(population, generation):
    t = 0
    fixprocess = [[t, population.calculate_mutantfreq()]]
    for x in range(generation):
        t += 1
        population.next_genwf()
        fixprocess.append([t, population.calculate_mutantfreq()])
    return fixprocess


def change_allelemo(population):
    t = 0
    fixprocess = [[t, population.calculate_mutantfreq()]]
    for x in range(20):
        t += 1
        population.next_genmo()
        fixprocess.append([t, population.calculate_mutantfreq()])
    return fixprocess


def output_allelechange(filename, population, function):
    with open(filename, "w", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["generation", "derived_allele_frequency"])
        fixprocess = function(population)
        for x in range(len(fixprocess)):
            writer.writerow(fixprocess[x])


p1_1 = Population(10)
print(p1_1.get_ids())
print(p1_1.get_fitnesses())
print(p1_1.is_not_fixed())

for x in range(10):
    p1_1.next_genwf()
    print(p1_1.get_ids())
    p1_1.get_genotypes()
    p1_1.list_mutation()
    print(p1_1.calculate_mutantfreq())

p1 = Population(10, 0.1, 0.2)
output_allelechange("allelefreqwf.csv", p1, change_allelewf)

p2 = Population(10, 0.1, 0.5)
output_allelechange("allelefreqmo.csv", p2, change_allelemo)
