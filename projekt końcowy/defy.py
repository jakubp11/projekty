from random import randint, choice
import random
from wrog import Wrog
from postac import Postac
from listy import złom
from listy import itemy
# naprawidz i sprawdzic
def wrogowie():
    wrog = [
        ["Trol Skalisty", randint(13, 17), 20, 1],
        ["Małpa", randint(11, 19), 15, 1],
        ["Korzenna Bestia", randint(15, 20), 20, 1],
        ["Dżunglowy Strażnik", randint(12, 17), 25, 1],
        ["Burzowy Wędrowiec", randint(10, 21), 25, 1],
    ]
    return choice(wrog)

def wrogowie2():
    wrog = [
        ["Morski Gigant", randint(22, 28), 28, 1],
        ["Błękitny Strażnik", randint(10, 16), 22, 1],
        ["Koronowiec Głębin", randint(12, 18), 25, 1],
        ["Faleń Żywiołów", randint(14, 20), 30, 1],
        ["Syrena Wojowniczka", randint(11, 17), 24, 1]
    ]
    return choice(wrog)

def wrogowie3():
    wrog = [
        ["Piekielny Wojownik", randint(14, 20), 30, 1],
        ["Demoniczna Harpia", randint(12, 18), 24, 1],
        ["Cień Chaosu", randint(10, 16), 22, 1],
        ["Ognisty Golem", randint(15, 21), 35, 1],
        ["Upiorny Niszczyciel", randint(16, 22), 40, 1]
    ]
    return choice(wrog)

def wrogowie4():
    wrog = [
        ["Cybernetyczny Tytan", randint(16, 22), 40, 1],
        ["Mechaniczna Małpa", randint(12, 18), 25, 1],
        ["Nano-Bestia", randint(10, 15), 18, 1],
        ["Plazmowy Strażnik", randint(14, 20), 35, 1],
        ["Dronowy Wędrowiec", randint(11, 17), 22, 1]
    ]
    return choice(wrog)

def losuj_przedmiot(wrog, lista_przedmiotow):
    przedmiot = random.choice(lista_przedmiotow)
    wrog.dodaj_ekwipunek(przedmiot)


def atak_wojownika1(gracz, cel):
    obrazenia = gracz.dmg + 10
    cel.odejmij_hp(obrazenia)
    gracz.odejmij_stamine(10)
    print(f"{gracz.imie} (Wojownik) uderza mieczem i zadaje {obrazenia} obrażeń!")

def atak_wojownika2(gracz, cel):
    obrazenia = gracz.dmg + 10
    cel.odejmij_hp(obrazenia)
    gracz.odejmij_stamine(10)
    print(f"{gracz.imie} (Wojownik) tnie mieczem i zadaje {obrazenia} obrażeń!")

def atak_wojownika3(gracz, cel):
    obrazenia = gracz.dmg // 2
    cel.odejmij_hp(obrazenia)
    gracz.odejmij_stamine(5)
    print(f"{gracz.imie} (Wojownik) uderza tarczą i zadaje {obrazenia} obrażeń oraz oszałamia przeciwnika!")


def atak_maga1(gracz, cel):
    if gracz.mana >= 20:
        obrazenia = gracz.dmg + 30
        cel.odejmij_hp(obrazenia)
        gracz.odejmij_mane(20)
        print(f"{gracz.imie} (Mag) rzuca ognistą kulę i zadaje {obrazenia} obrażeń!")
    else:
        print(f"{gracz.imie} nie ma wystarczająco many!")

def atak_maga2(gracz, cel):
    if gracz.mana >= 20:
        obrazenia = gracz.dmg + 30
        cel.odejmij_hp(obrazenia)
        gracz.odejmij_mane(20)
        print(f"{gracz.imie} (Mag) rzuca ognistą kulę i zadaje {obrazenia} obrażeń!")
    else:
        print(f"{gracz.imie} nie ma wystarczająco many!")

def atak_maga3(gracz, cel):
    if gracz.mana >= 35:
        obrazenia = gracz.dmg + 50
        cel.odejmij_hp(obrazenia)
        gracz.odejmij_mane(35)
        print(f"{gracz.imie} (Mag) uderza przeciwnika piorunem, zadając {obrazenia} obrażeń!")
    else:
        print(f"{gracz.imie} nie ma wystarczająco many!")


def atak_zlodzieja1(gracz, cel):
    obrazenia = int(gracz.dmg * 1.5)
    cel.odejmij_hp(obrazenia)
    gracz.odejmij_stamine(5)
    print(f"{gracz.imie} (Złodziej) atakuje z zaskoczenia, zadając {obrazenia} obrażeń!")

def atak_zlodzieja2(gracz, cel):
    obrazenia = int(gracz.dmg * 1.5)
    cel.odejmij_hp(obrazenia)
    gracz.odejmij_stamine(5)
    print(f"{gracz.imie} (Złodziej) wykonuje dzikie cięcie i zadaje {obrazenia} obrażeń!")

def atak_zlodzieja3(gracz, cel):
    obrazenia = gracz.dmg
    cel.odejmij_hp(obrazenia)
    gracz.odejmij_stamine(8)
    print(f"{gracz.imie} (Złodziej) zatruwa ostrze i zadaje {obrazenia} obrażeń oraz podtruwa przeciwnika!")


def atak_nekromanty1(gracz, cel):
    if gracz.mana >= 30:
        obrazenia = gracz.psychika // 2
        cel.odejmij_hp(obrazenia)
        gracz.odejmij_mane(30)
        print(f"{gracz.imie} (Nekromanta) przywołuje dusze i zadaje {obrazenia} obrażeń!")
    else:
        print(f"{gracz.imie} nie ma wystarczająco many!")

def atak_nekromanty2(gracz, cel):
    if gracz.mana >= 30:
        obrazenia = gracz.psychika // 2
        cel.odejmij_hp(obrazenia)
        gracz.odejmij_mane(30)
        print(f"{gracz.imie} (Nekromanta) przywołuje dusze i zadaje {obrazenia} obrażeń!")
    else:
        print(f"{gracz.imie} nie ma wystarczająco many!")

def atak_nekromanty3(gracz, cel):
    if gracz.mana >= 40:
        obrazenia = gracz.psychika
        cel.odejmij_hp(obrazenia)
        gracz.odejmij_mane(40)
        print(f"{gracz.imie} (Nekromanta) rzuca klątwę i zadaje {obrazenia} obrażeń!")
    else:
        print(f"{gracz.imie} nie ma wystarczająco many!")

def atak_berserkera1(gracz, cel):
    obrazenia = gracz.dmg + 50
    gracz.odejmij_hp(15)
    cel.odejmij_hp(obrazenia)
    print(f"{gracz.imie} (Berserker) wpada w szał i zadaje {obrazenia} obrażeń, tracąc 15 HP.")

def atak_berserkera2(gracz, cel):
    obrazenia = gracz.dmg + 50
    gracz.odejmij_hp(15)
    cel.odejmij_hp(obrazenia)
    print(f"{gracz.imie} (Berserker) wpada w szał i zadaje {obrazenia} obrażeń, tracąc 15 HP!")

def atak_berserkera3(gracz, cel):
    obrazenia = gracz.dmg + 20
    gracz.odejmij_hp(5)
    cel.odejmij_hp(obrazenia)
    print(f"{gracz.imie} (Berserker) tratował przeciwnika, zadając {obrazenia} obrażeń i tracąc 5 HP!")

def wykonaj_atak(gracz, cel):
    if not gracz.czy_zyje():
        print(f"{gracz.imie} nie może atakować — jest nieprzytomny!")
        return

    klasa = gracz.klasa_postaci.lower()

    print("\n Dostępne ataki:")
    if klasa == "wojownik":
        print("1  Silne Uderzenie")
        print("2  Przebicie Zbroi")
        print("3  Osłabienie Przeciwnika")
    elif klasa == "mag":
        print("1  Magiczny Pocisk")
        print("2  Fala Energii")
        print("3  Mentalne Wyczerpanie")
    elif klasa == "zlodziej":
        print("1  Cios w Plecy")
        print("2  Szybki Cios")
        print("3  Kradzież Monety")
    elif klasa == "nekromanta":
        print("1  Wysysanie Many")
        print("2  Przeklęta Strzała")
        print("3  Mroczne Osłabienie")
    elif klasa =="berserker":
        print("1 Szał Bitewny")
        print("2  Ciężki Cios")
        print("3  Wściekłość")

    print("4  Użyj przedmiotu z ekwipunku")

    wybor = input(" Wybierz akcję (1-4): ")

    if not wybor.isdigit():
        print(" Nieprawidłowy wybór.")
        return

    wybor = int(wybor)

    if wybor == 4:
        print("\n Ekwipunek:")
        gracz.pokaz_eku()
        indeks = input("Wpisz numer przedmiotu do użycia: ")
        if not indeks.isdigit():
            print(" Nieprawidłowy numer.")
            return
        indeks = int(indeks)
        gracz.uzyj_przedmiotu(indeks)
        return

    if klasa == "wojownik":
        if wybor == 1:
            atak_wojownika1(gracz, cel)
        elif wybor == 2:
            atak_wojownika2(gracz, cel)
        elif wybor == 3:
            atak_wojownika3(gracz, cel)

    elif klasa == "mag":
        if wybor == 1:
            atak_maga1(gracz, cel)
        elif wybor == 2:
            atak_maga2(gracz, cel)
        elif wybor == 3:
            atak_maga3(gracz, cel)

    elif klasa == "zlodziej":
        if wybor == 1:
            atak_zlodzieja1(gracz, cel)
        elif wybor == 2:
            atak_zlodzieja2(gracz, cel)
        elif wybor == 3:
            atak_zlodzieja3(gracz, cel)

    elif klasa == "nekromanta":
        if wybor == 1:
            atak_nekromanty1(gracz, cel)
        elif wybor == 2:
            atak_nekromanty2(gracz, cel)
        elif wybor == 3:
            atak_nekromanty3(gracz, cel)

    elif klasa == "berserker":
        if wybor == 1:
            atak_berserkera1(gracz, cel)
        elif wybor == 2:
            atak_berserkera2(gracz, cel)
        elif wybor == 3:
            atak_berserkera3(gracz, cel)

    else:
        print(" Nieznana klasa postaci lub atak niedostępny.")

def atak_wrog1(cel, gracz):
    gracz.odejmij_mane(15)
    gracz.odejmij_psychike(15)
    print(f"{cel.nazwa} patrzy zatrutym wzrokiem – {gracz.imie} traci 15 many i 15 psychiki!")

def atak_wrog2(cel, gracz):
    obrazenia = cel.dmg + 5
    gracz.odejmij_hp(obrazenia)
    gracz.odejmij_stamine(10)
    print(f"{cel.nazwa} uderza pazurem i zadaje {obrazenia} obrażeń! {gracz.imie} traci także 10 punktów wytrzymałości.")

def atak_wrog3(cel, gracz):
    gracz.odejmij_psychike(20)
    print(f"{cel.nazwa} wydaje przerażający okrzyk! {gracz.imie} traci 20 punktów psychiki!")

def atak_wrog4(cel, gracz):
    obrazenia = 5
    gracz.odejmij_hp(obrazenia)
    gracz.odejmij_psychike(10)
    print(f"{cel.nazwa} zadaje {obrazenia} obrażeń i zatruwa {gracz.imie}, obniżając psychikę o 10!")

def atak_wrog5(cel, gracz):
    obrazenia = cel.dmg
    gracz.odejmij_hp(obrazenia)
    print(f"{cel.nazwa} gryzie {gracz.imie} i zadaje {obrazenia} obrażeń!")

def losowy_atak_wr(cel, gracz):
    ataki = [
        atak_wrog1,
        atak_wrog2,
        atak_wrog3,
        atak_wrog4,
        atak_wrog5
    ]
    wybrany_atak = random.choice(ataki)
    wybrany_atak(cel, gracz)

def utworz_wroga(gracz, funkcja_wrogow):
    dane = funkcja_wrogow()
    nazwa = dane[0]
    dmg = dane[1] * gracz.poziom
    hp = dane[2] * gracz.poziom
    poziom = gracz.poziom
    return Wrog(nazwa, dmg, hp, poziom)

def sklep(gracz):
    while True:
        print("\nSKLEP:")
        print("1. Kup przedmiot")
        print("2. Sprzedaj złom")
        print("3. Wyjdź ze sklepu")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            if not itemy:
                print("Sklep jest pusty.")
                continue

            print("\nDOSTĘPNE PRZEDMIOTY:")
            for i, item in enumerate(itemy):
                print(f"{i}. {item[0]}  {item[1]} monet")

            wybor_itemu = input("Podaj numer przedmiotu do zakupu: ")
            if not wybor_itemu.isdigit():
                print("Nieprawidłowy wybór.")
                continue

            indeks = int(wybor_itemu)
            if indeks < 0 or indeks >= len(itemy):
                print("Taki przedmiot nie istnieje.")
                continue

            wybrany = itemy[indeks]
            cena = wybrany[1]

            if gracz.monety >= cena:
                gracz.monety -= cena
                gracz.eku.append(wybrany)
                del itemy[indeks]  
                print(f"{gracz.imie} kupił(a): {wybrany[0]}")
            else:
                print("Za mało monet.")

        elif wybor == "2":
            znaleziono = False
            for przedmiot in gracz.eku[:]: 
                if przedmiot in złom:
                    gracz.eku.remove(przedmiot)
                    gracz.monety += przedmiot[1]
                    print(f"Sprzedano: {przedmiot[0]} za {przedmiot[1]} monet.")
                    znaleziono = True
            if not znaleziono:
                print("Nie masz żadnego złomu do sprzedaży.")

        elif wybor == "3":
            print("Wychodzisz ze sklepu.")
            break

        else:
            print("Nieprawidłowy wybór.")

def legenda_menu(gracz):
    while True:
        print("\n" + "="*30)
        print(f" MENU GŁÓWNE {gracz.imie} (Poziom: {gracz.level})")
        print("="*30)
        print("1.  Postać")
        print("3.   Poziom Walki")
        print("4.  Droga Poboczna")
        print("5.  Sklep")
        print("6.  Wyjście z gry")
        print("="*30)

        wybor = input(" Wybierz opcję (1-6): ")

        if wybor == "1":
            print("\n Statystyki postaci:\n")
        elif wybor == "1":
            while True:
                print("\n MENU POSTACI:")
                print("1.  Pokaż statystyki")
                print("2.  Użyj przedmiotu z ekwipunku")
                print("3.  Usuń przedmiot z ekwipunku")
                print("4.  Wróć do menu głównego")

                pod_wybor = input(" Wybierz opcję (1-4): ")

                if pod_wybor == "1":
                    gracz.pokaz_statystyki()

                elif pod_wybor == "2":
                    if not gracz.eku:
                        print(" Ekwipunek pusty.")
                    else:
                        gracz.pokaz_eku()
                        indeks = input("Wpisz numer przedmiotu do użycia: ")
                        if indeks.isdigit():
                            gracz.uzyj_przedmiotu(int(indeks))
                        else:
                            print(" Nieprawidłowy indeks.")

                elif pod_wybor == "3":
                    if not gracz.eku:
                        print(" Ekwipunek pusty.")
                    else:
                        print("\n Ekwipunek:")
                        gracz.pokaz_eku()
                        indeks = input("Wpisz numer przedmiotu do usunięcia: ")
                        if indeks.isdigit():
                            indeks = int(indeks)
                            if 0 <= indeks < len(gracz.eku):
                                usuniety = gracz.eku.pop(indeks)
                                print(f" Usunięto przedmiot: {usuniety[0]}")
                            else:
                                print(" Indeks poza zakresem.")
                        else:
                            print(" Nieprawidłowy indeks.")

                elif pod_wybor == "4":
                    break 

                else:
                    print(" Nieprawidłowa opcja. Wybierz 1-4.")

        elif wybor == "3":
            print("\n Wyruszasz na poziom walki...\n")
            walka(gracz)  

        elif wybor == "4":
            print(" Kierujesz się na drogę poboczną...\n")
            droga_poboczna(gracz)

        elif wybor == "5":
            print("\n Wchodzisz do sklepu...\n")
            sklep(gracz)  

        elif wybor == "6":
            print(" Kończysz grę. Do zobaczenia!")
            break

        else:
            print(" Nieprawidłowy wybór. Spróbuj ponownie.")

def droga_poboczna(gracz):
    print(f"\n {gracz.imie} wyrusza na niebezpieczną drogę poboczną!")
    zabici = 0

    while gracz.czy_zyje():        
        przeciwnik = utworz_wroga(gracz)

        print(f"\n Walka z: {przeciwnik.nazwa} (HP: {przeciwnik.hp}, DMG: {przeciwnik.dmg})")

        while gracz.czy_zyje() and przeciwnik.czy_zyje():
            print(f"\n {gracz.imie} atakuje!")
            wykonaj_atak(gracz, przeciwnik)

            if not przeciwnik.czy_zyje():
                print(f" {przeciwnik.nazwa} został pokonany!")
                gracz.dodaj_exp(30)
                gracz.dodaj_monety(random.randint(5, 20))
                zabici += 1
                break

            print(f"\n {przeciwnik.nazwa} kontratakuje!")
            losowy_atak_wr(przeciwnik, gracz)

        if not gracz.czy_zyje():
            print(f"\n {gracz.imie} poległ na drodze pobocznej po pokonaniu {zabici} wrogów.")
            break

    print("\n Koniec wyprawy.")

def walka(gracz):
    poziom = gracz.poziom

    if poziom not in [1, 2, 3, 4]:
        print("Ten poziom walki nie jest jeszcze dostępny.")
        return

    print(f"\nRozpoczynasz Poziom Walki {poziom}!")


    if poziom == 1:
        funkcja_wrogow = wrogowie()
    elif poziom == 2:
        funkcja_wrogow = wrogowie2()
    elif poziom == 3:
        funkcja_wrogow = wrogowie3()
    elif poziom == 4:
        funkcja_wrogow = wrogowie4()

    while gracz.wrogowie_pokonani < 6 and gracz.czy_zyje():
        przeciwnik = utworz_wroga(gracz, funkcja_wrogow)
        print(f"\n{gracz.imie} napotyka przeciwnika: {przeciwnik.nazwa} (HP: {przeciwnik.hp})")

        while gracz.czy_zyje() and przeciwnik.czy_zyje():
            print(f"\n{gracz.imie} atakuje!")
            wykonaj_atak(gracz, przeciwnik)

            if not przeciwnik.czy_zyje():
                print(f"\n {przeciwnik.nazwa} został pokonany!")
                gracz.dodaj_exp(50)
                gracz.dodaj_monety(random.randint(10, 25))
                gracz.wrogowie_pokonani += 1
                print(f"Pokonani wrogowie: {gracz.wrogowie_pokonani}/6")
                break

            print(f"\n{przeciwnik.nazwa} atakuje!")
            losowy_atak_wr(przeciwnik, gracz)

            if not gracz.czy_zyje():
                print(f"\n {gracz.imie} poległ w walce...")
                return


    gracz.poziom += 1
    gracz.wrogowie_pokonani = 0
    print(f"\n {gracz.imie} awansował(a) na POZIOM WALKI {gracz.poziom}!")