class Counter:
    def __init__(self, number = 0):
        self.I = 0
        self.Number = number
    def __str__(self):
        return self.I
    def __iter__(self):
        self.I = 0
        return self
    def __next__(self):
        self.I += 1
        if(self.I > self.Number):
            raise StopIteration
        return self.__str__()

