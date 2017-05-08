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
        self._ancestors = [x for x in range(n)]
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
        fixid = [self._fixid_wf[x].get_id() for x in range(repeat)]
        wins = [0 for i in range(len(self._ancestors))]
        for x in fixid:
            wins[x] += 1
        fixprob = {x: wins[x]/repeat for x in range(len(self._ancestors))}
        print(fixprob)


def repeat_simmo(repeat, n, mutantrate=0, s=0):
    # repeat simulation in Moran model
    result = []
    for x in range(repeat):
        population = Population(n, mutantrate, s)
        result.append(simulate_fixmo(population))
    return result


class Repeat_moran:
    def __init__(self, repeat, n, mutantrate=0, s=0):
        self._ancestors = [x for x in range(n)]
        result = []
        for x in range(repeat):
            population = Population(n, mutantrate, s)
            result.append(simulate_fixmo(population))
        self._fixtime_mo = [result[x][0] for x in range(len(result))]
        self._fixid_mo = [result[x][1] for x in range(len(result))]

    def get_fixtime_mo(self):
        return self._fixtime_mo

    def ave_fixtime_mo(self):
        print(calculate_ave(self._fixtime_mo))

    def var_fixtime_mo(self):
        print(calculate_var(self._fixtime_mo))

    def get_fixid_mo(self):
        return self._fixid_mo

    def fixprob_mo(self):
        repeat = len(self._fixid_mo)
        fixid = [self._fixid_mo[x].get_id() for x in range(repeat)]
        wins = [0 for i in range(len(self._ancestors))]
        for x in fixid:
            wins[x] += 1
        fixprob = {x: wins[x]/repeat for x in range(len(self._ancestors))}
        print(fixprob)


trial1 = Repeat_wf(5, 10)
print(trial1.get_fixtime_wf())
trial1.ave_fixtime_wf()
trial1.var_fixtime_wf()
print(trial1.get_fixid_wf())
trial1.fixprob_wf()


trial2 = Repeat_moran(5, 10)
print(trial2.get_fixtime_mo())
trial2.ave_fixtime_mo()
trial2.var_fixtime_mo()
print(trial2.get_fixid_mo())
trial2.fixprob_mo()
