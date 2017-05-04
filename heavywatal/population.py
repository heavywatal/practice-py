#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Population class
"""
import random
import sys
from individual import Individual


class Population:
    def __init__(self, size, num_mutants=1, s=0, model='w', fixation='type'):
        assert num_mutants < size
        mutants = [Individual(i, 1 + s) for i in range(num_mutants)]
        wildtypes = [Individual(i) for i in range(num_mutants, size)]
        self._individuals = mutants + wildtypes
        self._num_steps = 0
        self._initial_freq = num_mutants
        self._allele_freqs = [num_mutants]

        if model.startswith('w'):
            self.step = self._step_wrightfisher
        elif model.startswith('m'):
            self.step = self._step_moran
        else:
            raise RuntimeError('Unknown model: {}'.format(model))

        if fixation not in ('type', 'id'):
            raise RuntimeError('Unknown value: fixation={}'.format(fixation))
        else:
            self._fixation = fixation

    @property
    def allele_freqs(self):
        return self._allele_freqs

    def __str__(self):
        return str([str(x) for x in self._individuals])

    def __len__(self):
        return len(self._individuals)

    def is_fixed(self):
        if self._fixation == 'type':
            return self._allele_freqs[-1] in (0, len(self))
        id0 = self._individuals[0].id
        for x in self._individuals:
            if x.id != id0:
                return False
        return True

    def evolve_until_fixation(self, verbose=False):
        while not self.is_fixed():
            self.step()
            if verbose:
                sys.stderr.write(str(self) + '\n')

    def print_fixation(self):
        assert self.is_fixed()
        if self._fixation == 'id':
            winner = self._individuals[0].id
        else:
            if self._individuals[0].id < self._initial_freq:
                winner = 'mutant'
            else:
                winner = 'wild'
        print('{}\t{}'.format(winner, self._num_steps))

    def _count_mutants(self):
        count = 0
        for ind in self._individuals:
            if ind._id < self._initial_freq:
                count += 1
        return count

    def _step_wrightfisher(self):
        size = len(self)
        weights = [x.fitness for x in self._individuals]
        self._individuals = random.choices(self._individuals, weights, k=size)
        self._num_steps += 1
        self._allele_freqs.append(self._count_mutants())

    def _step_moran(self):
        weights = [x.fitness for x in self._individuals]
        child = random.choices(self._individuals, weights, k=1)[0]
        i_dying = random.randrange(len(self))
        self._individuals[i_dying] = child
        self._num_steps += 1
        # TODO: verbose re-counting
        self._allele_freqs.append(self._count_mutants())


def main():
    population = Population(6, 3, 0.2)
    print(population)
    print(len(population))
    population.evolve_until_fixation(verbose=True)
    population.print_fixation()
    print(population.allele_freqs)


if __name__ == '__main__':
    main()
