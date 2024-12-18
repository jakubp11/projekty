from random import randint , choice


life = 150
stamina = 150
mana = 100
monety = 0

lup = 0
maxlife = 150
maxstamina = 150
maxmana = 100



def wrogowie():
    wrog = [
        ["trol skalisty",(randint(13,17)),20,1],
        ["małpa",(randint(11,19)),15,1],
        ["Korzenna Bestia",(randint(15,20)),20,1],
        ["Dżunglowy Strażnik",(randint(12,17)),25,1],
        ["Burzowy Wędrowiec",(randint(10,21)),25,1],
    ]
    return choice(wrog)

def wrogowie2():
    wrog = [
        ["Morski Gigant", randint(22, 28), 28,1],
        ["Błękitny Strażnik", randint(10, 16), 22,1],
        ["Koronowiec Głębin", randint(12, 18), 25,1],
        ["Faleń Żywiołów", randint(14, 20), 30,1],
        ["Syrena Wojowniczka", randint(11, 17), 24,1]
    ]
    return choice(wrog)
def wrogowie3():
    wrog = [
        ["Piekielny Wojownik", randint(14, 20), 30,1],
        ["Demoniczna Harpia", randint(12, 18), 24,1],
        ["Cień Chaosu", randint(10, 16), 22,1],
        ["Ognisty Golem", randint(15, 21), 35,1],
        ["Upiorny Niszczyciel", randint(16, 22), 40,1]
    ]
    return choice(wrog)
def wrogowie4():
    wrog = [
        ["Cybernetyczny Tytan", randint(16, 22), 40,1],
        ["Mechaniczna Małpa", randint(12, 18), 25,1],
        ["Nano-Bestia", randint(10, 15), 18,1],
        ["Plazmowy Strażnik", randint(14, 20), 35,1],
        ["Dronowy Wędrowiec", randint(11, 17), 22,1]
    ]
    return choice(wrog)

def boss():
    boss = [
    ["Wielki Trol", randint(40, 50), 50]

    ["Wodny Władca", randint(45, 55), 60]

    ["Czarny Demon", randint(50, 60), 70]

    ["Mistrz Mechaniczny", randint(55, 65), 80]
    ]
n = 0
def wybormikstury():
    global n
    print("wybierz miksture:")
    print("A = mikstura życia")
    print("B = mikstura many")
    print("C = mikstura staminy")

    wybor = input().upper()
    if wybor == "A" and n > 0:
        potion1()
        n -= 1
        return 0

    elif wybor == "B" and n > 0:
        potion3()
        n -= 1
        return 0
    elif wybor == "C"and n > 0:
        potion2()
        n -= 1
        return 0
    else:
        print("nie ma takiej mikstury lub nie masz żadnych mikstur")
        return 0

def atakmiecz():
    global stamina
    stamina -= 10
    return randint(10,14)
def atakmagia():
    global mana
    mana -= 10
    return randint(15,19)
def ataktornado():
    global mana,stamina
    mana -= 20
    stamina -= 20
    return randint(24,30)
def wyborataku():
    print("wybierz atak:")
    print("A = atak mieczem")
    print("B = atak magią")
    print("C = zmasowany atak")
    print("D = wybór mikstury")
    wybor = input().upper()
    if wybor == "A":
        return atakmiecz()
    elif wybor == "B":
        return atakmagia()
    elif wybor == "C":
        return ataktornado()
    elif wybor == "D":
        wybormikstury()
        return 0
    else:
        print("nie ma takiego ataku")
        return 0
def potion1():
    global life,maxlife
    if life < maxlife:
        life += 40
        print(f"Twoje życie po użyciu mikstury to {life} na {maxlife}")
    elif life >= maxlife:  
            life = maxlife
            print("Masz już pełne zdrowie!")
    return 0
        

def potion2():
    global stamina,maxstamina
    if stamina < maxstamina:
        stamina += 40
        print(f"Twoja stamina po użyciu mikstury to {stamina} na {maxstamina}")
    elif stamina >= maxstamina:  
            stamina = maxstamina
            print("Masz już pełną stamine!")
    return 0
def potion3():
    global mana,maxmana
    if mana < maxmana:
        mana += 40
        print(f"Twoja mana po użyciu mikstury to {mana} na {maxmana}")
    elif mana >= maxmana:  
            mana = maxmana
            print("Masz już pełną manę!")
    return 0
def ulepszenia():
     global maxmana,maxlife,maxstamina

wrog  = wrogowie()
wrog2 = wrogowie2()
wrog3 = wrogowie3()
wrog4 = wrogowie4()
#mana22level1
def wyborwybor():
    print("-----"*10)
    print("wybierz opcje:")
    print("A = główna ścieżka""\n"
    "B - sklep ""\n"
    "C - poboczne ruiny""\n"
    "D - statystyki")
    print("-----"*10)
def staty():
    print(f"życie - {maxlife}")
    print(f"stamina - {maxstamina}")
    print(f"mana - {maxmana}")

def sklep():
    global maxlife, maxstamina, maxmana, monety
    print("[Sklep]")
    print(f"1 - ulepszenia do życia z {maxlife}  do {maxlife +10} koszt 20 monet ")
    print(f"2 - ulepszenia do staminy z {maxstamina}  do {maxstamina +10} koszt 20 monet ")
    print(f"3 - ulepszenia do many z {maxmana}  do {maxmana +10} koszt 20 monet ")
    print(f"Q - Wyjdź ze sklepu")
    opcja = input("Wybierz opcję: ").upper()   
    
    if opcja == "1":
        if monety >= 20:
            maxlife += 10
            monety -= 20
            print(f"Ulepszono życie! Nowe max życie: {maxlife}. Pozostałe monety: {monety}")
        else:
            print("Nie masz wystarczająco monet!")
    elif opcja == "2":
        if monety >= 20:
            maxstamina += 10
            monety -= 20
            print(f"Ulepszono staminę! Nowa max stamina: {maxstamina}. Pozostałe monety: {monety}")
        else:
            print("Nie masz wystarczająco monet!")
    elif opcja == "3":
        if monety >= 20:
            maxmana += 10
            monety -= 20
            print(f"Ulepszono manę! Nowa max mana: {maxmana}. Pozostałe monety: {monety}")
        else:
            print("Nie masz wystarczająco monet!")
lzp = 0
lzp2 = 0
lzp3 = 0
lzp4 = 0
print("---"*10)
imie = input("podaj imie")
print(f"twoje imie to {imie}")
i = 0

lzpx = 0
while True:

    wyborwybor()
    inp = input().upper()
    if inp == "A":
        if i == 0:
            while life > 0 and lzp < 5:
                print("poziom 1")
                wrog  = wrogowie()
                print(f"{imie} walczy teraz z {wrog[0]}")
                print(f"Przeciwnik ma {wrog[1]} HP i zadaje Ci {wrog[2]} obrażeń")
                life -= wrog[2]
                if life <= 0:
                    life = maxlife
                    mana = maxmana
                    stamina = maxstamina
                    break


                print(f"Masz {life} HP , {mana} many i {stamina} staminy")
                atak = wyborataku()
                wrog[1] -= atak
                print(f"Zadałeś {atak} obrażeń")
                if wrog[1] <= 0:
                    print('Zabiłeś przeciwnika!!!')
                    lzp += 1
                    monety += 1
            if lzp == 5:
                i += 1
                life = maxlife
                mana = maxmana
                stamina = maxstamina
                break
        if i == 1:
            while life > 0 and lzp2 < 5:
                print("poziom 2")
                wrog2  = wrogowie2()
                print(f"{imie} walczy teraz z {wrog2[0]}")
                print(f"Przeciwnik ma {wrog2[1]} HP i zadaje Ci {wrog2[2]} obrażeń")
                life -= wrog2[2]
                if life <= 0:
                    life = maxlife
                    mana = maxmana
                    stamina = maxstamina
                    break


                print(f"Masz {life} HP , {mana} many i {stamina} staminy")
                atak = wyborataku()
                wrog2[1] -= atak
                print(f"Zadałeś {atak} obrażeń")
                if wrog2[1] <= 0:
                    print('Zabiłeś przeciwnika!!!')
                    lzp2 += 1
                    monety += 1
            if lzp2 == 5:
                i += 1
                life = maxlife
                mana = maxmana
                stamina = maxstamina
                break
        if i == 2:
            while life > 0 and lzp3 < 5:
                print("poziom 3")
                wrog3  = wrogowie3()
                print(f"{imie} walczy teraz z {wrog3[0]}")
                print(f"Przeciwnik ma {wrog3[1]} HP i zadaje Ci {wrog3[2]} obrażeń")
                life -= wrog3[2]
                if life <= 0:
                    life = maxlife
                    mana = maxmana
                    stamina = maxstamina
                    break


                print(f"Masz {life} HP , {mana} many i {stamina} staminy")
                atak = wyborataku()
                wrog3[1] -= atak
                print(f"Zadałeś {atak} obrażeń")
                if wrog3[1] <= 0:
                    print('Zabiłeś przeciwnika!!!')
                    lzp3 += 1
                    monety += 1
            if lzp3 == 5:
                i += 1
                life = maxlife
                mana = maxmana
                stamina = maxstamina
                break
        if i == 3:
            while life > 0 and lzp4 < 5:
                print("poziom 4")
                wrog4  = wrogowie4()
                print(f"{imie} walczy teraz z {wrog4[0]}")
                print(f"Przeciwnik ma {wrog4[1]} HP i zadaje Ci {wrog4[2]} obrażeń")
                life -= wrog4[2]
                if life <= 0:
                    life = maxlife
                    mana = maxmana
                    stamina = maxstamina                   
                    break


                print(f"Masz {life} HP , {mana} many i {stamina} staminy")
                atak = wyborataku()
                wrog4[1] -= atak
                print(f"Zadałeś {atak} obrażeń")
                if wrog4[1] <= 0:
                    print('Zabiłeś przeciwnika!!!')
                    lzp4 += 1
                    monety += 1
            if lzp4 == 5:
                 i += 1
                 life = maxlife
                 mana = maxmana
                 stamina = maxstamina
                 break
    elif inp == "B":
        sklep()
    elif inp == "C":
        while life > 0:
            wrog = wrogowie()
            while wrog[1] > 0 and life > 0:
                print(f"{imie} walczy teraz z {wrog[0]}")
                print(f"Przeciwnik ma {wrog[1]} HP i zadaje Ci {wrog[2]} obrażeń")
       
                life -= wrog[2]
                if life <= 0:
                    life = maxlife
                    mana = maxmana
                    stamina = maxstamina
                    break


                print(f"Masz {life} HP , {mana} many i {stamina} staminy")
                atak = wyborataku()
                wrog[1] -= atak
                print(f"Zadałeś {atak} obrażeń")


            if wrog[1] <= 0:
                print('Zabiłeś przeciwnika!!!')
                lzpx += 1
                monety += 1
            if lzpx % 5 == 0:
                n += 1
        print(f"zabiłeś {lzpx} przeciwników i otrzymałeś {n} butelek mikstur")
    elif inp == "D":
        staty()
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")

             
             
        