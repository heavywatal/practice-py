#!/usr/bin/env python
# -*- coding: utf-8 -*-
from population import Population


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


class Repeat_simwf:
    def __init__(self, trials, n, mutantrate=0, s=0):
        self._firstinds = n
        result = []
        for x in range(trials):
            population = Population(n, mutantrate, s)
            result.append(simulate_fixwf(population))
        self._fixtime_wf = [result[x][0] for x in range(len(result))]
        self._fixid_wf = [result[x][1] for x in range(len(result))]

    def get_fixtime_wf(self):
        return self._fixtime_wf

    def ave_fixtime_wf(self):
        average = sum(self._fixtime_wf)/len(self._fixtime_wf)
        print(average)

    def var_fixtime_wf(self):
        trials = len(self._fixtime_wf)
        a = sum(self._fixtime_wf)/trials
        sqd = [(self._fixtime_wf[x] - a)**2 for x in range(trials)]
        variance = sum(sqd)/trials
        print(variance)

    def get_fixid_wf(self):
        return self._fixid_wf

    def fixprob_wf(self):
        n = self._firstinds
        trials = len(self._fixid_wf)
        fixid = self._fixid_wf
        fixprob = {x: fixid.count(x)/trials for x in range(n)}
        print(fixprob)


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

trial1 = Repeat_simwf(5, 10)
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
