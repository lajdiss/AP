class Vozidlo:
    def __init__(self, znacka:str, vyroba:int, stavN:int = 100):
        self.znacka = znacka
        self.vyroba = vyroba
        self.stavN = stavN
        pass

    def zvuk_motoru(self):
        return "??"
    
    def info(self):
        return f"Tohle je {self.znacka}, rok vyroby je {self.vyroba}"
    
    def startuje(self):
        if self.stavN > 0:
            return f"Startuje"
        else:
            return f"Nestartuje"

class Auto(Vozidlo):
    def __init__(self, znacka, vyroba, prevodovka, stavN = 100,):
        super().__init__(znacka, vyroba, stavN)
        self.prevodovka = prevodovka

    def info(self):
        return f"Tohle je {self.znacka}, rok vyroby je {self.vyroba}"

    def zvuk_motoru(self):
        return "vruum vruum"
    
    def zatrub(self):
        return "tididi"

class Moped(Vozidlo):
    def __init__(self, znacka, vyroba, ma_slapadla:bool, stavN = 100):
        super().__init__(znacka, vyroba, stavN)
        self.ma_slapadla = ma_slapadla
    
    def zvuk_motoru(self):
        return "TRRRRRRRR"
    
moped = Moped("Jawa", 1990, False, 100)
auto = Auto("skoda", 2008, "Manual", 0)

garaz = [moped, auto]
for vozidlo in garaz:
    print(vozidlo.info())
    print(vozidlo.startuje())