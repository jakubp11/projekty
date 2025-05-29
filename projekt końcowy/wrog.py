from postac import Postac
class Wrog():
    def __init__(self, nazwa, hp, dmg, poziom):
        self.nazwa = nazwa
        self.dmg = dmg
        self.hp = hp
        self.poziom = poziom
        self.ekwipunek = []  

    def pokaz_statystyki(self):
        print("---- Wróg ----")
        print(f"Nazwa: {self.nazwa}")
        print(f"Obrażenia: {self.dmg}")
        print(f"HP: {self.hp}")
        print(f"Poziom: {self.poziom}")
        print(f"Ekwipunek: {', '.join(self.ekwipunek) if self.ekwipunek else 'brak'}")
        print("----------------")

    def odejmij_hp(self, ile):
        self.hp -= ile
        if self.hp < 0:
            self.hp = 0
        print(f"{self.nazwa} otrzymał {ile} obrażeń. Pozostało HP: {self.hp}")

    def dodaj_hp(self, ile):
        self.hp += ile
        print(f"{self.nazwa} odzyskał {ile} HP. Aktualne HP: {self.hp}")

    def dodaj_dmg(self, ile):
        self.dmg += ile
        print(f"{self.nazwa} zwiększył obrażenia o {ile}. Aktualne obrażenia: {self.dmg}")

    def dodaj_ekwipunek(self, item):
        self.ekwipunek.append(item)
        print(f"{self.nazwa} zdobył przedmiot: {item}")

    def czy_zyje(self):
        return self.hp > 0