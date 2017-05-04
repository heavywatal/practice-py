#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""main
"""
import sys
import csv
from population import Population


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-n', '--popsize', type=int, default=6)
    parser.add_argument('-q', '--initfreq', type=int, default=1)
    parser.add_argument('-s', '--effect', type=float, default=0.0)
    parser.add_argument('-m', '--model', choices=['w', 'm'], default='w')
    parser.add_argument('--fixation', choices=['type', 'id'], default='type')
    parser.add_argument('--temporal', action='store_true')
    parser.add_argument('nrep', nargs='?', type=int, default=1)
    args = parser.parse_args()

    for i in range(args.nrep):
        population = Population(args.popsize, args.initfreq, args.effect,
                                args.model, args.fixation)
        population.evolve_until_fixation(args.verbose)
        if args.temporal:
            writer = csv.writer(sys.stdout)
            writer.writerow(population.allele_freqs)
        else:
            population.print_fixation()


if __name__ == '__main__':
    main()
