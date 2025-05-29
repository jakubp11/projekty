class Postac:
    def __init__(self,imie,  klasa_postaci):
        self.imie = imie
        self.klasa_postaci = klasa_postaci
        self.level = 1
        self.exp = 0
        self.hp = 100
        self.stamina = 50
        self.mana = 80
        self.dmg = 10
        self.psychika = 100
        self.max_hp = 100
        self.max_dmg = 10
        self.max_stamina = 50
        self.max_mana = 80
        self.max_psychika = 100
        self.monety = 0
        self.eku = []
        self.poziom = 1
        self.wrogowie_pokonani = 0

        self.ustaw_klase()

    def odejmij_monety(self, ile):
        self.monety -= ile
        if self.monety < 0:
            self.monety = 0
        print(f"{self.imie} ma {self.monety} monet.")
    def dodaj_psychika(self,ile):
        self.psychika += ile
        if self.psychika > self.max_psychika:
            self.psychika = self.max_psychika
        print(f"psychika {self.imie} powiększyła się o {ile}. Pozostało {self.psychika}.")

    def dodaj_exp(self, ile):
        self.exp += ile
        print(f"{self.imie} zdobył(a) {ile} EXP. Łącznie ma {self.exp} EXP.")
        self.sprawdz_poziom()

    def sprawdz_poziom(self):
        while self.exp >= 100 * self.level:
            self.exp -= 100 * self.level
            self.level += 1
            self.hp += 5
            self.max_hp += 5  
            self.dmg += 2
            self.max_dmg += 2 
            print(f"{self.imie} awansował(a) na poziom {self.level}!")
            print(f"Nowe statystyki: HP = {self.hp}, DMG = {self.dmg}")


    def dodaj_mana(self, ile):
        self.mana += ile
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        print(f"{self.imie} odzyskał(a) {ile} punktów many. Aktualna mana: {self.mana}")

    def dodaj_stamina(self, ile):
        self.stamina += ile
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
        print(f"{self.imie} zregenerował(a) {ile} punktów wytrzymałości. Aktualna wytrzymałość: {self.stamina}")

    def dodaj_hp(self,ile):
        self.hp += ile
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f" {self.imie} uleczył się o {ile} punktów życia. Pozostało {self.psychika}.")

    def dodaj_dmg(self,ile):
        self.dmg += ile
        if self.dmg > self.max_dmg:
            self.dmg = self.max_dmg
        print(f"obrażenia {self.imie} powiększyły się o {ile}.zadawane obrażenia wynoszą {self.dmg}.")

    def ustaw_klase(self):
        if self.klasa_postaci.lower() == "wojownik":
            self.dmg += 20
            self.max_dmg += 20
            self.stamina += 30
            self.max_stamina += 30
        elif self.klasa_postaci.lower() == "mag":
            self.psychika += 30
            self.max_psychika += 30
            self.mana += 40
            self.max_mana += 40
        elif self.klasa_postaci.lower() == "zlodziej":
            self.monety += 10
            self.stamina += 20
            self.max_stamina += 20
        elif self.klasa_postaci.lower() == "nekromanta":
            self.mana += 70
            self.max_mana += 70
            self.psychika += 50
            self.max_psychika += 50
            self.hp -= 20
            self.max_hp -= 20
            self.stamina -= 10
            self.max_stamina -= 10
        elif self.klasa_postaci.lower() == "berserker":
            self.dmg += 40
            self.max_dmg += 40
            self.stamina += 50
            self.max_stamina += 50
            self.psychika -= 30
            self.max_psychika -= 30
            self.mana = 0
            self.max_mana = 0
        else:
            print("Nieznana klasa – powtórz próbę.")


    def ustaw_imie(self, imie):
        self.imie = imie
        print(f"Imię postaci ustawiono na: {self.imie}")

    def odejmij_hp(self, ile):
        self.hp -= ile
        if self.hp < 0:
            self.hp = 0
        print(f"{self.imie} otrzymał(a) {ile} obrażeń. Pozostało HP: {self.hp}")
        
    def odejmij_dmg(self, ile):
        self.dmg -= ile
        if self.dmg < 0:
            self.dmg = 0
        print(f"obrażenia {self.imie} pomniejszyły się o {ile}.zadawane obrażenia wynoszą {self.dmg}")

    def odejmij_psychike(self, ile):
        self.hp -= ile
        if self.psychika < 0:
            self.psychika = 0
        print(f"psychika {self.imie} pomiejszyła się o {ile} Pozostało {self.psychika}")

    def odejmij_mane(self, ile):
        self.mana -= ile
        if self.mana < 0:
            self.mana = 0
        print(f"{self.imie} zużył(a) {ile} punktów many. Pozostało many: {self.mana}")

    def odejmij_stamine(self, ile):
        self.stamina -= ile
        if self.stamina < 0:
            self.stamina = 0
        print(f"{self.imie} stracił(a) {ile} punktów wytrzymałości. Pozostało wytrzymałości: {self.stamina}")


    def czy_zyje(self):
        return self.hp > 0
    
    def czy_monety(self,ile):
        return self.monety >= ile
    
    def dodaj_monety(self, ile):
        self.monety += ile
        print(f"{self.imie} zdobył(a) {ile} monet. Aktualnie posiada: {self.monety} monet.")

    def dodaj_do_ekwipunku(self, przedmiot):
        self.ekwipunek.append(przedmiot)
        print(f"{self.imie} dodał(a) do ekwipunku: {przedmiot[0]}")
    
    def usun_z_ekwipunku(self, nazwa):
        for przedmiot in self.ekwipunek:
            if przedmiot[0] == nazwa:
                self.ekwipunek.remove(przedmiot)
                print(f"{self.imie} usunął/ęła z ekwipunku: {nazwa}")
                return
        print(f"{self.imie} nie ma przedmiotu: {nazwa}")
    def pokaz_eku(self):
        if not self.eku:
            print(f"{self.imie} nie ma żadnych przedmiotów w ekwipunku.")
        else:
            print(f"Ekwipunek {self.imie}:")
            for i, przedmiot in enumerate(self.eku, start=0):
                print(f"{i}. {przedmiot[0]}")

    def uzyj_przedmiotu(self, indeks):
        if indeks < 0 or indeks >= len(self.eku):
            print(" Nieprawidłowy indeks przedmiotu.")
            return

        przedmiot = self.eku[indeks]
        nazwa = przedmiot[0]
        hp = przedmiot[2]
        dmg = przedmiot[3]
        mana = przedmiot[4]
        stamina = przedmiot[5]
        psychika = przedmiot[6]

        self.hp += hp
        self.max_hp += hp
        self.dmg += dmg
        self.max_dmg += dmg
        self.mana += mana
        self.max_mana += mana
        self.stamina += stamina
        self.max_stamina += stamina
        self.psychika += psychika
        self.max_psychika += psychika

        print(f"{self.imie} użył(a) przedmiotu: {nazwa}. Statystyki zostały zwiększone.")
        

    def pokaz_statystyki(self):
        print("----- Statystyki -----")
        print(f"Imię: {self.imie}")
        print(f"Klasa: {self.klasa_postaci}")
        print(f"HP: {self.hp}")
        print(f"Obrażenia: {self.dmg}")
        print(f"Poziom: {self.level}")
        print(f"Monety: {self.monety}")
        print(f"Psychika: {self.psychika}")
        print("----------------------")

