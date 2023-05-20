from human import Human
from car import Car
humans = list()
bmw = Car("BMW x6")
andrii = Human("Andrii", True)
ivan = Human("Ivan")
danylo = Human("Danylo")
egor = Human("Egor")
humans.append(andrii)
humans.append(ivan)
humans.append(danylo)
humans.append(egor)
for human in humans:
    bmw.AddHumanToCar(human)
for driver in bmw.Drivers:
    bmw.ShowInfo(driver)
for passenger in bmw.Passengers:
    bmw.ShowInfo(passenger)
