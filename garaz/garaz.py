import random
from  datetime import datetime


class Car:
    def __init__(self, brand:str, model:str, year:int, stkYear:int, fuel:int = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.stkYear = stkYear
        self.fuel = fuel
        pass
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - fuel: {self.fuel}"

    def move(self):
        usage = random.randint(5,20)
        if self.fuel >= usage:
            self.fuel -= usage
            return f"{self.brand} {self.model} dojel, sezralo {usage} a zbyva mu {self.fuel}"
        else:
            return f"{self.brand} {self.model} nema dost paliva, potrebuje {usage} paliva, a ma jen {self.fuel}"

    def natankovat(self):
        filled = 100 - self.fuel
        self.fuel = 100
        return f" Do {self.brand} {self.model} natankovano {filled} % paliva"

    def stk(self):
        if self.stkYear < datetime.now().year:
            return f"{self.brand} {self.model} musi na technickou - skoncila {self.stkYear}"
        else:
            return f"{self.brand} {self.model} nemusi na STK, bude muset jit za {self.stkYear - datetime.now().year} let/rok/roky"






car1 = Car("Škoda", "Octavia 3", 2015, 2027, 63)
car2 = Car("Hyundai", "Getz", 2012, 2020, 3)
car3 = Car("Toyota", "Jaris", 2020, 2028, 50)

print(car1)
print(car2)
print(car3)
print("--" * 40)
print(car1.move())
print(car1.move())
print("--" * 40)
print(car2.move())
print(car2.natankovat())
print(car2.move())
print("--" * 40)
print(car3.move())
print(car3.move())
print("--" * 40)

print(car1.stk())
print("--" * 40)
print(car2.stk())
print("--" * 40)
print(car3.stk())
print("--" * 40)

class Garage:
    def __init__(self, name):
        self.name = name
        self.cars = []
        pass

    def addCar(self, car:Car):
        self.cars.append(car)
        return f"Do garaze {self.name} bylo pridano auto {car.brand} {car.model} rok {car.year}"
    
    def showCars(self):
        if len(self.cars) == 0:
            print(f"V garazi {self.name} neni zadne auto")
        else:
            print(f"Auto v garazi : {self.name}")
            for car in self.cars:
                print("-->", car)

    def oldestCar(self):
        if len(self.cars) == 0:
            return None
        theoldest = min(self.cars, key= lambda a: a.year)
        return theoldest

    def avgFuel(self):
        if len(self.cars) == 0:
            return 0
        return sum(car.fuel for car in self.cars)/len(self.cars)

garage = Garage("Housebox")
print(garage.addCar(car1))
print(garage.addCar(car2))
print(garage.addCar(car3))
print("--" * 40)
garage.showCars()
print("-----Nejstarsi auto-------")
oldest = garage.oldestCar()
if oldest:
    print(f"Nejstarsi auto v garazi je {oldest.brand} {oldest.model} {oldest.year}")

print("-------Prumerna hodnota paliva-------")
print(f"{garage.avgFuel():.1f} %")

print("-------Jizda specifickeho auto v garazi---------")
print(garage.cars[2].move())

print("--------Jizda vsech aut v garazi--------")
for car in garage.cars:
    print(car.move())

print("----Hromadna STK-----------")
for car in garage.cars:
    print(car.stk())