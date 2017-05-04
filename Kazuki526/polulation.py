#! /usr/local/bin/env python


class Population:
    def __init__(self, *population):
        self._individual = population

    def print_id_list(self):
        print(" ".join(self._individual))


pop_a = Population("a", "b", "c", "d")
pop_a.print_id_list()
