#!/usr/bin/env python
# -*- coding: utf-8 -*-
from population import Population


def get_heterogeneity(Population):  # fixed or not
    Population_ids = [x.get_id() for x in Population._inds]
    for x in range(1, len(Population_ids)):
        if Population_ids[0] != Population_ids[x]:
            return True
            break
    else:
        return False


def simulate_fixwf(Population):  # simulate fixation in Wrigft-Fisher model
    time = 0
    while get_heterogeneity(Population):
        Population.next_genwf()
        time += 1
    else:
        winner_id = Population._inds[0]
        return time, winner_id


def repeat_simwf(trials, n, mutantrate=0, s=0):
    # repeat simulation in Wrigft-Fisher model
    result = []
    for x in range(trials):
        population = Population(n, mutantrate, s)
        result.append(simulate_fixwf(population))
    return result


def simulate_fixmo(Population):   # simulate fixation in Moran model
    time = 0
    while get_heterogeneity(Population):
        Population.next_genmo()
        time += 1
    else:
        winner_id = Population._inds[0]
        return time, winner_id


def repeat_simmo(trials, n, mutantrate=0, s=0):
    # repeat simulation in Moran model
    result = []
    for x in range(trials):
        population = Population(n, mutantrate, s)
        result.append(simulate_fixmo(population))
    return result


p1 = Population(10, 0.1, 0.5)
p1.print_ids()
print(get_heterogeneity(p1))
print(simulate_fixwf(p1))
print(repeat_simwf(5, 10, 0.1, 0.5))

p2 = Population(10, 0.1, 0.5)
p2.print_ids()
print(get_heterogeneity(p2))
print(simulate_fixmo(p2))
print(repeat_simmo(5, 10, 0.1, 0.5))
