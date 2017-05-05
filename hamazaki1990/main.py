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


class Repeat_wf:
    def __init__(self, repeat, n, mutantrate=0, s=0):
        self._ancestors = n
        result = []
        for x in range(repeat):
            population = Population(n, mutantrate, s)
            result.append(simulate_fixwf(population))
        self._fixtime_wf = [result[x][0] for x in range(len(result))]
        self._fixid_wf = [result[x][1] for x in range(len(result))]

    def get_fixtime_wf(self):
        return self._fixtime_wf

    def ave_fixtime_wf(self):
        print(calculate_ave(self._fixtime_wf))

    def var_fixtime_wf(self):
        print(calculate_var(self._fixtime_wf))

    def get_fixid_wf(self):
        return self._fixid_wf

    def fixprob_wf(self):
        repeat = len(self._fixid_wf)
        fixid = [self._fixid_wf[x].get_id for x in range(repeat)]
        wins = [0 for i in range(self._ancestors)]
        for x in fixid:
            wins[x] += 1
        print(wins)


def repeat_simmo(trials, n, mutantrate=0, s=0):
    # repeat simulation in Moran model
    result = []
    for x in range(trials):
        population = Population(n, mutantrate, s)
        result.append(simulate_fixmo(population))
    return result


p1 = Population(10, 0.1, 0.5)
p1.print_ids()
print(p1._inds.count(1))
print(p1.is_not_fixed())
print(simulate_fixwf(p1))

trial1 = Repeat_wf(5, 10)
print(trial1.get_fixtime_wf())
trial1.ave_fixtime_wf()
trial1.var_fixtime_wf()
print(trial1.get_fixid_wf())
trial1.fixprob_wf()

p2 = Population(10, 0.1, 0.5)
p2.print_ids()
print(p2.is_not_fixed())
print(simulate_fixmo(p2))
print(repeat_simmo(5, 10, 0.1, 0.5))
