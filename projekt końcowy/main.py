from postac import Postac
from defy import legenda_menu

def main():
    print("Witaj w grze!")
    
    imie = input("Podaj imię swojej postaci: ")
    klasa_postaci = input("Wybierz klasę postaci (wojownik, mag, złodziej, nekromanta, berserker): ").lower()
    
    gracz = Postac(imie, klasa_postaci)
    
    print(f"\nStworzono postać: {gracz.imie}, Klasa: {gracz.klasa_postaci}")
    
    while True:
        print("\nWchodzisz do gry")
        legenda_menu(gracz)
        
        kontynuowac = input("Czy chcesz wrócić do legendy? (tak/nie): ").lower()
        if kontynuowac != 'tak':
            print("Dziękujemy za grę! Do zobaczenia!")
            break

if __name__ == "__main__":
    main()
