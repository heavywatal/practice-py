class Individual:
    def __init__(self, n):
        self._id = n


i1 = Individual(1)
i2 = Individual(2)

print(i1._id)
print(i2._id)

m = 5
for x in range(1, m + 1):
    ix = Individual(x)
    print(ix._id)
