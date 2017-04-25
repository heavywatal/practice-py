class Individual:
    def __init__(self, n):
        self._id = n

    def get_id(self):
        return self._id


ind = Individual(42)
print(ind.get_id())
