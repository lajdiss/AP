class Robot:
    def __init__(self, oznaceni:str, baterie:int, ukol:str = "nicit"):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        pass
    def zvuk(self):
        return "bipu-ditu"
    def diagnostika(self):
        return f"oznaceni {self.oznaceni}, mam {self.baterie} procent"
    def ukol(self):
        return f"muj aktivni ukol je {self.ukol}"
    def zadej_ukol(self, Nukol:str):
        self.ukol = Nukol
        return f"muj novy ukol je {Nukol}"
robot = Robot("bum", 12) 

print(robot.diagnostika())
print(robot.zadej_ukol("nabit se"))
    