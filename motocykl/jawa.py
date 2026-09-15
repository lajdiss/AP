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
    
    def popojed(self, spotreba):
        self.stav_nadrze = spotreba
        return f"spotrebovalo se {spotreba} "
    
    