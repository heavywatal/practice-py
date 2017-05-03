#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    cnt = 0
    while get_heterogeneity(Population):
        Population.next_genwf()
        Population.print_ids()
        cnt += 1
    else:
        print(cnt)


def simulate_fixmo(Population):
    cnt = 0
    while get_heterogeneity(Population):
        Population.next_genmo()
        Population.print_ids()
        cnt += 1
    else:
        print(cnt)


p = Population(5)
p.print_ids()
print(get_heterogeneity(p))
cnt = 1
while get_heterogeneity(p):
    p.next_genwf()
    p.print_ids()
    print(get_heterogeneity(p))
    print(cnt)
    cnt += 1
winner = p._inds[0]
print(winner.get_id())

p1 = Population(5)
p1.print_ids()
print(get_heterogeneity(p1))
simulate_fixwf(p1)


p2 = Population(5)
p2.print_ids()
print(get_heterogeneity(p2))
simulate_fixmo(p2)
