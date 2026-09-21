import random
class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass
    def zvuk(self):
        return "??"
    def predstav(self):
        return f"ahoj jsem {self.jmeno}, je mi {self.vek}"
    def kdeJsi(self):
        return f"bydlim v {self.misto}"
    
    def bez(self, nMisto:str):
        self.misto = nMisto
        return f"presunul jsem se na {nMisto}. {self.kdeJsi()}"
    
class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.plemeno = plemeno

    def zvuk(self):
        return"Haf"
    
    def aport(self):
        return f"{self.jmeno} prinesl micek"
    
    def vycesat(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} utekl"
        else:
            return f"{self.jmeno} nechal se vycesat"
        
    def predstav(self):
        return f"{super().predstav()} jsem {self.plemeno}"
    
class Kocka(Zvire):
    def __init__(self, jmeno, vek, barva, misto = "pokoj"):
        super().__init__(jmeno, vek, misto)
        self.barva = barva

    def mnouk(self):
        return"mnau"
    
    def utok(self):
        return f"{self.jmeno} te poskrabala"
    
    def pohladit(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} vrniii"
        else:
            return f"{self.jmeno} nenechala se pohladit skrabla te"
        
class Papousek(Zvire):
    def __init__(self, jmeno, vek, barvaP, misto = "klec"):
        super().__init__(jmeno, vek, misto)
        self.barvaP = barvaP

    def zvuk(self):
        return"Pip, pip, pi pi, pap"
    
    def mluv(self, coRict:str):
        self.opakuj = coRict
        return f"{self.jmeno} opakuj : {coRict}! {coRict}"
    
class Had(Zvire):
    def __init__(self, jmeno, vek, delkaVcm:int, jedovatej:bool, misto = "terarium"):
        super().__init__(jmeno, vek, misto)
        self.delkaVcm = delkaVcm
        self.jedovatej = jedovatej
    
    def zvuk(self):
        return"Tsssssssssssssssss"
    
    def ustknuti(self):
        if self.jedovatej:
            return f"POZOR {self.jmeno} te ustknul a je jednovaty"
        else:
            return f"chill {self.jmeno} te kousnul, ale neni jedovatej"
    
    def predstav(self):
        if self.jedovatej:
            typ = "jedovaty"
        else:
            typ = "skrtic"
        return f"SSssssSSSsssSssSs . . . já jsem {self.jmeno}, merim {self.delkaVcm} a jsem {typ}"
    

        
        
hadík2 = Had("hadice", 2, 5, False)
hadík = Had("hadak", 120, 20, True)
print(hadík.predstav())
print(hadík.ustknuti())

print("-" * 20)
print(hadík2.predstav())
print(hadík2.ustknuti())

print("-" * 20)
    
Papuch = Papousek("Rio", 6, "Modrá")
print(Papuch.zvuk())
print(Papuch.mluv("bla, bla"))

print("-" * 20)
Ementalek = Kocka("Ementalek", 1, "černa")
print(Ementalek.jmeno)
print(Ementalek.mnouk())
print(Ementalek.utok())
print(Ementalek.pohladit())

print("-" * 25)
    
hugo = Pes("Hugo", 5, "pejsek", "výřivka")

print(hugo.jmeno)
print(hugo.zvuk())
print(hugo.predstav())
print(hugo.aport())
print(hugo.vycesat())
print(hugo.kdeJsi())

print("-" * 25)
        
    

zvire = Zvire("Hund", 67)
print(zvire.predstav())
print(zvire.kdeJsi())
print(zvire.zvuk())
print(zvire.bez("obed"))

print("-" * 20)

zvire2 = Zvire("cokl", 0.5,"sklep")
print(zvire2.predstav())
print(zvire.kdeJsi())

print("-" * 20)

zoo = [Papuch, hadík, Ementalek, hugo]

for obyvatel in zoo:
    print(obyvatel.zvuk())
    print(obyvatel.predstav())
    print("-" * 20)