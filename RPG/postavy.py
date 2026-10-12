import random
class Postava:
    def __init__(self, jmeno: str, zdravi: int):
        self.jmeno = jmeno
        self.zdravi = zdravi

    def predstav_se(self):
        print(f"Jsem {self.jmeno} a mám {self.zdravi} životů.")

    predstavSe = predstav_se

    def utok(self):
        return 0


class Rytir(Postava):
    def __init__(self, jmeno: str, zdravi: int, brneni: int):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni

    def utok(self):
        poskozeni = random.randint(10, 20)
        return f"{self.jmeno} sekl mečem a způsobil {poskozeni} poškození!"

    def zablokuj(self):
        return f"{self.jmeno} zablokoval útok štítem a brněním (hodnota brnění: {self.brneni})."


class Mag(Postava):
    def __init__(self, jmeno: str, zdravi: int, mana: int):
        super().__init__(jmeno, zdravi)
        self.mana = mana

    def utok(self):
        if self.mana >= 10:
            self.mana -= 10
            poskozeni = random.randint(25, 40)
            return f"{self.jmeno} seslal mocné kouzlo za {poskozeni} poškození! (Zbývající mana: {self.mana})"
        else:
            return f"{self.jmeno} nemá dostatek many a útočí slabě holí za 5 poškození."


class Lukostrelec(Postava):
    def __init__(self, jmeno: str, zdravi: int, sipy: int):
        super().__init__(jmeno, zdravi)
        self.sipy = sipy

    def utok(self):
        if self.sipy > 0:
            self.sipy -= 1
            poskozeni = random.randint(15, 30)
            return f"{self.jmeno} vystřelil šíp z luku za {poskozeni} poškození! (Zbývající šípy: {self.sipy})"
        else:
            return f"{self.jmeno} nemá žádné šípy a musí útočit dýkou za 5 poškození."

    def dopln_sipy(self, pocet: int):
        self.sipy += pocet
        return f"{self.jmeno} si doplnil {pocet} šípů (nyní má {self.sipy})."



    rytir = Rytir("Artuš", 120, 25)
    mag = Mag("Gandalf", 70, 20)

    druzina = [rytir, mag]

    print("predstaveni")
    for postava in druzina:
        postava.predstav_se()
        print(postava.utok())
        print("-" * 40)