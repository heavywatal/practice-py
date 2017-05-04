#! /usr/bin/env python


class Individual:
    def __init__(self, idn):
        self._id = idn


sample1 = Individual(1)
print "sample1 id is", sample1._id
print ("sample1 id is", sample1._id)

sample2 = Individual(2)
print "sample2 id is", sample2._id
