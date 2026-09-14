class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass
    def zvuk(self):
        return"??"
    def predstav(self):
        return f"ahoj jsem {self.jmeno}, je mi {self.vek}"
    def kdeJsi(self):
        return f"bydlim v {self.misto}"
    
    def bez(self, nMisto:str):
        self.misto = nMisto
        return f"presunul jsem se na {nMisto}. {self.kdeJsi()}"
        
    

zvire = Zvire("Hund", 67)
print(zvire.predstav())
print(zvire.kdeJsi())
print(zvire.zvuk())
print(zvire.bez("obed"))


zvire2 = Zvire("cokl", 0.5,"sklep")
print(zvire2.predstav())
print(zvire.kdeJsi())
