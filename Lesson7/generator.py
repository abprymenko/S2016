class Generator:
    def __init__(self, number = 0):
        self.Number = number
    def __call__(self, number = 0):
        self.Number = number
        print(f"Number = {self.Number}")
    def __str__(self):
        return f"Number: {self.Number}"
    def Pow(self, powDigit):
        for i in range(1, powDigit + 1):
            yield self.Number ** i