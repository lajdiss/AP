class Sitove_zarizeni:
    def __init__(self, nazev:str, ip_add:str, online:bool = False):
        self.nazev = nazev
        self.ip_add = ip_add
        self.online = online

    def zmen_stav(self):
        stary = self.online
        self.online = not self.online
        return f"měním {stary} na {self.online}"

    def diagnostika(self):
        return "Spouštím diagnostiku"


class Router(Sitove_zarizeni):
    def __init__(self, nazev:str, ip_add:str, pocet_portu:int, online:bool = False):
        super().__init__(nazev, ip_add, online)
        self.pocet_portu = pocet_portu

    def diagnostika(self):
        zaklad = super().diagnostika()
        return f"{zaklad}  Kontroluji LAN porty"

    def restart_WIFI(self):
        return "restartuju wifi"


class Server(Sitove_zarizeni):
    def __init__(self, nazev:str, ip_add:str, os:str, online:bool = False):
        super().__init__(nazev, ip_add, online)
        self.os = os

    def diagnostika(self):
        zaklad = super().diagnostika()
        return f"{zaklad}  Vytížení CPU"


router = Router("tp-link", "192.168.120.1", 12, True)
server = Server("Home_lab", "192.168.120.10", "Debian", False)

sit = [router, server]
for zarizeni in sit:
    print(zarizeni.zmen_stav())
    print(zarizeni.diagnostika())