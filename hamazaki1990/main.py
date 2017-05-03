#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from individual import Individual
from population import Population


def get_heterogeneity(Population):
    Population_ids = [x.get_id() for x in Population._inds]
    for x in range(1, len(Population_ids)):
        if Population_ids[0] != Population_ids[x]:
            return True
            break
    else:
        return False


def simulate_fixwf(Population):
    cnt = 1
    while get_heterogeneity(Population):
        Population = Population.next_genwf()
        cnt += 1
        print(Population._inds)
    else:
        print(cnt)


p1 = Population(5)
p1.print_ids()
print(get_heterogeneity(p1))
simulate_fixwf(p1)
