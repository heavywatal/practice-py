class Population:
    def __init__(self, size):
        self._size = size
        self._list = [x for x in range(size)]

    def wholeid(self):
        print(self._list)


p1 = Population(10)
p1.wholeid()
