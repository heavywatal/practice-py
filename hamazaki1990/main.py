#!/usr/bin/env python
# -*- coding: utf-8 -*-
from population import Population


def calculate_ave(seq):
    return sum(seq)/len(seq)


def calculate_var(seq):
    ave = calculate_ave(seq)
    sqd = [(seq[x] - ave)**2 for x in range(len(seq))]
    return sum(sqd)/len(seq)


def simulate_fixwf(Population):  # simulate fixation in Wrigft-Fisher model
    time = 0
    while Population.is_not_fixed():
        Population.next_genwf()
        time += 1
    return time, Population._inds[0].get_id()


def simulate_fixmo(Population):   # simulate fixation in Moran model
    time = 0
    while Population.is_not_fixed():
        Population.next_genmo()
        time += 1
    return time, Population._inds[0].get_id()


class Repeater:
    def __init__(self, function, repeat, n, mutantrate=0, s=0):
        result = []
        for x in range(repeat):
            population = Population(n, mutantrate, s)
            result.append(function(population))
        self._fixtime = [result[x][0] for x in range(len(result))]
        fixid = [result[x][1] for x in range(len(result))]
        wins = [0 for i in range(n)]
        for x in fixid:
            wins[x] += 1
        self._fixprob = {i: wins[i]/repeat for i in range(n)}

    def get_fixtime(self):
        return self._fixtime

    def get_fixprob(self):
        return self._fixprob


trial1 = Repeater(simulate_fixwf, 1000, 10, 0.1, -0.05)
print(calculate_ave(trial1.get_fixtime()))
print(calculate_var(trial1.get_fixtime()))
print(trial1.get_fixprob())


trial2 = Repeater(simulate_fixmo, 1000, 10, 0.1, -0.05)
print(calculate_ave(trial2.get_fixtime()))
print(calculate_var(trial2.get_fixtime()))
print(trial2.get_fixprob())
