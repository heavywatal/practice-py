import csv
from population import Population


def get_step(t, mutations):
    t_mutations = []
    for i in mutations:
        t_mutation = [t]
        t_mutation.extend(i)
        t_mutations.append(t_mutation)
    return t_mutations


def change_allelewf(population, generation):
    t = 0
    change_allele = population.mutantfreq_per_site()
    derived_allelefreq = get_step(t, change_allele)
    for x in range(generation):
        t += 1
        population.next_genwf()
        change_allele = population.mutantfreq_per_site()
        next_gen = get_step(t, change_allele)
        derived_allelefreq.extend(next_gen)
    return derived_allelefreq


def change_allelemo(population, generation):
    t = 0
    change_allele = population.mutantfreq_per_site()
    derived_allelefreq = get_step(t, change_allele)
    for x in range(generation):
        t += 1
        population.next_genmo()
        change_allele = population.mutantfreq_per_site()
        next_gen = get_step(t, change_allele)
        derived_allelefreq.extend(next_gen)
    return derived_allelefreq


def output_allelechange(filename, function, population, generation):
    with open(filename, "w", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        freq = function(population, generation)
        col_name = ["step", "locus", "frequency"]
        writer.writerow(col_name)
        for x in range(len(freq)):
            writer.writerow(freq[x])


example = [[0.1, 0.2], [0.2, 0.2], [0.8, 0.1]]
print(example[1])
print(get_step(2, example))

p1_1 = Population(10)
fixprocess1 = change_allelewf(p1_1, 10)
print(fixprocess1)

p1_2 = Population(10)
fixprocess2 = change_allelemo(p1_2, 20)
print(fixprocess2)

p1 = Population(1000)
output_allelechange("allelefreqwf.csv", change_allelewf, p1, 1000)

p2 = Population(1000)
output_allelechange("allelefreqmo.csv", change_allelemo, p2, 1000)
