import random
from  datetime import datetime

class Animal:
    def __init__(self, species:str, name:str, birthYear:int, checkupYear:int, energy:int):
        self.species = species
        self.name = name
        self.birthYear = birthYear
        self.checkupYear = checkupYear
        self.energy = energy
        pass
    def __str__(self):
        return f"{self.species} {self.name} narozen {self.birthYear}, ma {self.energy} % energie."
    
    def play(self):
        usage = random.randint(5,20)
        if self.energy >= usage:
            self.energy -= usage
            return f"{self.species} {self.name} si hral a ubralo mu to {usage} % energie, zbyva mu {self.energy} %"
        else:
            return f"{self.species} {self.name} je moc unaveny, potrebuje {usage} %, ale ma jen {self.energy} %"
        
    def feed(self):
        doplneno = 100 - self.energy
        self.energy = 100
        return f"{self.species} {self.name} se najedl, doplneno {doplneno} % energie"
    def vetCheck(self):
        if self.checkupYear < datetime.now().year:
            return f"{self.species} {self.name} musi k vet - platnost skoncila {self.checkupYear}"
        else:
            return f"{self.species} {self.name} nemusi jit k veterinarovi {self.checkupYear - datetime.now().year} let/rok/roky"

zvire1 = Animal("Zebra", "Mirka", 1999, 2025, 20)
zvire2 = Animal("Zirafa", "Zofka", 2009, 2026, 80)
zvire3 = Animal("Hrosice", "Glorie", 2021, 2024, 40)

print(zvire1)
print(zvire2)
print(zvire3)
print("---" * 20)
print(zvire1.play())
print(zvire2.play())
print(zvire3.play())
print("---" * 20)
print(zvire1.feed())
print(zvire2.feed())
print(zvire3.feed())
print("---" * 20)
print(zvire1.vetCheck())
print(zvire2.vetCheck())
print(zvire3.vetCheck())

class Zoo:
    def __init__(self, name:str):
        self.name = name
        self.animals = []
        pass
    
    def addAnimal(self, animal:Animal):
        self.animals.append(animal)
        return f"Do zoo {self.name} bylo odvezeno zvire {animal.species} {animal.name}"
    
    def showAnimals(self):
        if len(self.animals) == 0:
            print(f"V Zoo {self.name} neni zadne zvire")
        else:
            print(f"Zvirata v ZOO {self.name}")
            for animal in self.animals:
                print("-->", animal)