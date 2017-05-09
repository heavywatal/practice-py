import pandas as pd
from population import Population


def calculate_ave(seq):
    return sum(seq)/len(seq)


def calculate_var(seq):
    ave = calculate_ave(seq)
    sqd = [(seq[x] - ave)**2 for x in range(len(seq))]
    return sum(sqd)/len(seq)


def change_allelewf(Population):
    fixprocess = [Population._inds]
    while Population.is_not_fixed():
        Population.next_genwf()
        fixprocess.append(Population._inds)
    return fixprocess


def change_allelemo(Population):
    fixprocess = [Population._inds]
    while Population.is_not_fixed():
        Population.next_genmo()
        fixprocess.append(Population._inds)
    return fixprocess


p1 = Population(10)
data = pd.DataFrame(change_allelewf(p1))
print(data)

p2 = Population(10)
data = pd.DataFrame(change_allelemo(p2))
print(data)
