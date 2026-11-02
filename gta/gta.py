class NPC:
    def __init__(self, jmeno:str, energie:int):
        self.jmeno = jmeno
        self.energie = energie
        pass

    def predstavse(self):
        return f"Ahoj jmenuju se {self.jmeno}"
    
    def vyraz_na(self, cil):
        if self.energie >= 10:
            self.energie -= 10
            return f"Jdu na cil {cil}. Zbyla mi energie: {self.energie}"
        else:
            return f"{self.jmeno} nema dost energie"
        

    
npc = NPC("Trevor Philips", 10)
print(npc.predstavse())
print(npc.vyraz_na("Praha"))
print(npc.vyraz_na("Brna"))

print("--" * 50)

class Chodec(NPC):
    def __init__(self, jmeno, energie, domovska_ctvrt:str):
        super().__init__(jmeno, energie)
        self.domovska_ctvrt = domovska_ctvrt
        pass

    def predstavse(self):
        return f"Zde chodec {self.jmeno}, hood:{self.domovska_ctvrt}"
    def vyraz_na(self, cil):
        if self.energie >= 30:
            self.energie -=30
            return f"Zahajuji narocny pesi pochod k cili {cil}. Zbyva mi {self.energie} energie"
        else:
            return f"Nemam dost energie"

class Policajt(NPC):
    def __init__(self, jmeno, energie, tasena_zbran:bool = False):
        super().__init__(jmeno, energie)
        self.tasena_zbran = tasena_zbran

    def predstavse(self):
        return f"Tady cajt LSPD {self.jmeno}"
    
    def tas_nebo_skryj_zbran(self):
        self.tasena_zbran = not self.tasena_zbran
        if self.tasena_zbran:
            return f"{self.jmeno}: ON MA ZBRAN"
        else:
            return f"{self.jmeno}: zbran skryta"

class Autobusak(NPC):
    def __init__(self, jmeno, energie):
        super().__init__(jmeno, energie)
        self.cestujici = []

    def naber_cestujici(self, jmeno_cestujiciho:str):
        self.cestujici.append(jmeno_cestujiciho)
        return f"Do autobusu ridice {self.jmeno} nastoupil cestujici: {jmeno_cestujiciho}"
    




npc1 = Chodec("Big Smoke", 35, "Grove Sreet")
print(npc1.vyraz_na("Balas hood"))
print("--" * 50)
npc2 = Policajt("Frank Tenpenny", 100)
print(npc2.tas_nebo_skryj_zbran())
print(npc2.predstavse())
print(npc2.tas_nebo_skryj_zbran())
print("--" * 50)
npc3 = Autobusak("Fanda", 67)
print(npc3.naber_cestujici("Lukáš Mykeš"))
print(npc3.naber_cestujici("Jupert Gong"))
print(npc3.cestujici)
print(npc3.naber_cestujici("Carl Johnson"))
print(npc3.cestujici)
print("--" * 50)

skupina_npc = [npc1, npc2, npc3]
spolecny_cil = "Domov"

for postava in skupina_npc:
    print(postava.predstavse())
    print(postava.vyraz_na(spolecny_cil))
    print("--" * 50)


