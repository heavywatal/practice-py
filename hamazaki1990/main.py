#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from individual import Individual
from population import Population


def get_heterogeneity(Population):
    for x in Population._inds:
        if Population[0] != Population[x]:
            return True
            break
        else:
            return False


def simulate_fixwf(Population):
    if complete_fixation(Population):



p1 = Population(5)
p1.print_ids
simulate_fixation(p1)
