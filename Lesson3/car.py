from human import Human
class Car:
    def __init__(self, brand = None):
        self.Brand = brand
        self.Passengers = list()
        self.Drivers = list()
    def AddHumanToCar(self, human = Human()):
        if(isinstance(human, Human) and human != None):
            if(human.IsDriver):
                self.Drivers.append(human)
            else:
                self.Passengers.append(human)
    def ShowInfo(self, human = Human()):
        if (isinstance(human, Human) and human != None):
            if(human.IsDriver):
                print(f"The driver of the car {self.Brand} is: {human.Name}")
            else:
                print(f"The passenger of the car {self.Brand} is: {human.Name}")
