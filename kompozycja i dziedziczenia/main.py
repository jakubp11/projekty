import random

class Pojazd:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.czesci = []
        self.paliwo = 0

    def typ(self):
        return "Pojazd"

    def dodajczesc(self, czesc):
        self.czesci.append(czesc)

    def spalanie(self, km):
        return (self.paliwo * km) / 100

    def zuzycieczesci(self, km):
        zuzycia = {}
        for czesc in self.czesci:
            zuzycia[czesc.nazwa] = czesc.ilepozostalo(km)
        return zuzycia

    def info(self):
        return f"{self.typ()}: {self.marka} {self.model}, {self.rok}"
    def jedz_na_trasie(self, trasa):
        modyfikator_spalania = trasa.modyfikator_spalania()
        modyfikator_zuzycia = trasa.modyfikator_zuzycia()

        dystans = trasa.dystans
        spalanie = self.paliwo_na_100km * modyfikator_spalania * dystans / 100

        print(f"\nJazda po trasie: {trasa.nazwa} ({trasa.typ_trasy}, {dystans} km)")
        print(f"Spalono {spalanie:.2f} litrów paliwa.")

        for czesc in self.czesci:
            zuzycie = dystans * modyfikator_zuzycia
            czesc.zuzyj(zuzycie)
            print(f"{czesc.nazwa} - pozostało {czesc.trwalosc_km - czesc.przejechane_km:.0f} km trwałości")
class Trasa:
    def __init__(self, nazwa, dystans, typ_trasy):
        self.nazwa = nazwa
        self.dystans = dystans
        self.typ_trasy = typ_trasy.lower()  

    def modyfikator_spalania(self):
        if self.typ_trasy == "miasto":
            return 1.2
        elif self.typ_trasy == "autostrada":
            return 0.9
        elif self.typ_trasy == "teren":
            return 1.5
        return 1.0

    def modyfikator_zuzycia(self):
        if self.typ_trasy == "miasto":
            return 1.1
        elif self.typ_trasy == "autostrada":
            return 0.8
        elif self.typ_trasy == "teren":
            return 1.7
        return 1.0

class Czesci:
    def __init__(self, nazwa, trwalosc):
        self.nazwa = nazwa
        self.trwalosc = trwalosc
        self.uzycie = 0

    def zuzyj(self, km):
        self.uzycie += km

    def ilepozostalo(self, km):
        self.zuzyj(km)
        return max(0, self.trwalosc - self.uzycie)

    def __str__(self):
        return f"{self.nazwa} - pozostalo {self.trwalosc - self.uzycie} km"


class Opona(Czesci):
    def __init__(self):
        super().__init__("Opona", 50000)


class Hamulec(Czesci):
    def __init__(self):
        super().__init__("Hamulce", 30000)


class Filtr(Czesci):
    def __init__(self):
        super().__init__("Filtr oleju", 15000)


class Samochod(Pojazd):
    def __init__(self, marka, model, rok):
        super().__init__(marka, model, rok)
        self.paliwo = 7

    def typ(self):
        return "Samochod"


class Motocykl(Pojazd):
    def __init__(self, marka, model, rok):
        super().__init__(marka, model, rok)
        self.paliwo = 4

    def typ(self):
        return "Motocykl"


class Ciezarowka(Pojazd):
    def __init__(self, marka, model, rok):
        super().__init__(marka, model, rok)
        self.paliwo = 15

    def typ(self):
        return "Ciezarowka"


class Fabryka:
    def stworz(self, typ, marka, model, rok):
        if typ == "samochod":
            return Samochod(marka, model, rok)
        if typ == "motocykl":
            return Motocykl(marka, model, rok)
        if typ == "ciezarowka":
            return Ciezarowka(marka, model, rok)
        return None


def menu():
    fabryka = Fabryka()
    print("Wybierz typ pojazdu: samochod, motocykl, ciezarowka")
    typ = input("Typ: ").lower()
    marka = input("Marka: ")
    model = input("Model: ")
    rok = int(input("Rok: "))

    pojazd = fabryka.stworz(typ, marka, model, rok)
    if pojazd == None:
        print("Nieznany typ pojazdu.")
        return

    while True:
        print("\nMenu:")
        print("1. Dodaj czesc")
        print("2. Pokaz info")
        print("3. Symuluj jazde")
        print("4. Wyjdz")
        wybor = input("Wybierz: ")

        if wybor == "1":
            print("Wybierz czesc: opona, hamulec, filtr")
            cz = input("Czesc: ").lower()
            if cz == "opona":
                pojazd.dodajczesc(Opona())
            elif cz == "hamulec":
                pojazd.dodajczesc(Hamulec())
            elif cz == "filtr":
                pojazd.dodajczesc(Filtr())
            else:
                print("Nieznana czesc")
        elif wybor == "2":
            print(pojazd.info())
            for c in pojazd.czesci:
                print(c)
        elif wybor == "3":
            km = int(input("Podaj dystans km: "))
            print(f"Spalanie: {pojazd.spalanie(km)} L")
            for nazwa, ile in pojazd.zuzycieczesci(km).items():
                print(f"{nazwa} - pozostalo {ile} km")
        elif wybor == "4":
            break
        else:
            print("Niepoprawna opcja")


if __name__ == "__main__":
    menu()
