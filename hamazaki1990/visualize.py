import pandas as pd
from population import Population


def calculate_ave(seq):
    return sum(seq)/len(seq)


def calculate_var(seq):
    ave = calculate_ave(seq)
    sqd = [(seq[x] - ave)**2 for x in range(len(seq))]
    return sum(sqd)/len(seq)


def change_allelewf(Population):  # simulate fixation in Wrigft-Fisher model
    time = 0
    while Population.is_not_fixed():
        Population.next_genwf()
        Population.print_ids()
        time += 1
    else:
        winner_id = Population._inds[0]
        return time, winner_id


def simulate_fixmo(Population):   # simulate fixation in Moran model
    time = 0
    while Population.is_not_fixed():
        Population.next_genmo()
        time += 1
    else:
        winner_id = Population._inds[0]
        return time, winner_id


p1 = Population(10)
data = list(change_allelewf(p1))
data.to_csv()
