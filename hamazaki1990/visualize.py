import csv
from population import Population


def change_allelewf(population, generation):
    change_allele = [population.calculate_mutantfreq_per_site()]
    for x in range(generation):
        population.next_genwf()
        change_allele.append(population.calculate_mutantfreq_per_site())
    all_mutations = []
    for x in change_allele:
        all_mutations.extend(x.keys())
    all_mutationsites = sorted(list(set(all_mutations)))
    derived_allelefreq = []
    for x in range(generation+1):
        t = [x]
        t.extend([change_allele[x].get(y, 0.0) for y in all_mutationsites])
        derived_allelefreq.append(t)
    return derived_allelefreq


def change_allelemo(population, generation):
    change_allele = [population.calculate_mutantfreq_per_site()]
    for x in range(generation):
        population.next_genmo()
        change_allele.append(population.calculate_mutantfreq_per_site())
    all_mutations = []
    for x in change_allele:
        all_mutations.extend(x.keys())
    all_mutationsites = sorted(list(set(all_mutations)))
    derived_allelefreq = []
    for x in range(generation+1):
        t = [x]
        t.extend([change_allele[x].get(y, 0.0) for y in all_mutationsites])
        derived_allelefreq.append(t)
    return derived_allelefreq


def output_allelechange(filename, function, population, generation):
    with open(filename, "w", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        freq = function(population, generation)
        num = ["allele" + str(i) + "frequency" for i in range(len(freq[0])-1)]
        col_name = ["generation"]
        col_name.extend(num)
        writer.writerow(col_name)
        for x in range(len(freq)):
            writer.writerow(freq[x])


p1_1 = Population(10)
fixprocess1 = change_allelewf(p1_1, 10)
print(fixprocess1)

p1_2 = Population(10)
fixprocess2 = change_allelemo(p1_2, 20)
print(fixprocess2)

p1 = Population(100)
output_allelechange("allelefreqwf.csv", change_allelewf, p1, 100)

p2 = Population(100)
output_allelechange("allelefreqmo.csv", change_allelemo, p2, 100)
