import random
class Postava:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi
        pass
    
    def predstavSe(self):
        return f"{self.jmeno}, {self.zdravi}hp"
    
    def utok(self):
        return f"0"
    
class Rytir(Postava):
    def __init__(self, jmeno, brneni, zdravi):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni
        pass
    
def utok(self):
    zaklad = super().utok()
    sek = random.randint(10, 20)
    return f"Byls seknut o {sek} {zaklad}"

rytir = Rytir("hanz", 20, 10)
print(rytir.utok())