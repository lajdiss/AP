class Motorka:
    def __init__(self, znacka:str, stav_nadrze:int, kategorie:str, stojanek:str = "vyklopeny"):
        self.znacka = znacka
        self.stav_nadrze = stav_nadrze
        self.kategorie = kategorie
        self.stojanek = stojanek
        pass

    def plyn(self):
        return "vrum"
    
    def popis_moto(self):
        return f"Tohle je {self.znacka} jeji oznaceni je {self.kategorie}."
    
    def stojanek(self):
        return f"Stojanek je {self.stonajek}"
    
    def zmena_stojanku(self, nStav:str):
        self.stojanek = nStav
        return f" ted je stojanej {nStav}, {self.stojanek()}"
    
    def popojed(self, spotreba:int):
        self.stav_nadrze -=spotreba
        return f"spotrebovalo se {spotreba}, {self.stav_nadrze}. "
    
    def natankuj(self, natankovano:int):
        self.stav_nadrze += natankovano
        return f"natankovalo se {natankovano}, {self.stav_nadrze}"
    
motorka = Motorka("Jawa", 100, "Enduro")

print(motorka.popojed(25))
print(motorka.stav_nadrze)
print(motorka.stav_nadrze)
print(motorka.popojed(25))

    
    