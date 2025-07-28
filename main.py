def dodawanie(liczba1, liczba2):
    return liczba1 + liczba2

def odejmowanie(liczba1, liczba2):
    return liczba1 - liczba2

def mnozenie(liczba1, liczba2):
    return liczba1 * liczba2

def dzielenie(liczba1, liczba2):
    return liczba1 / liczba2

print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")
dzialanie = int(input("Podaj działanie: "))

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

if dzialanie == 1:
    print(f"Wynik dodawania liczb {liczba1} oraz {liczba2} to {dodawanie(liczba1, liczba2)}")
elif dzialanie == 2:
    print(f"Wynik odejmowania liczb {liczba1} oraz {liczba2} to {odejmowanie(liczba1, liczba2)}")
elif dzialanie == 3:
    print(f"Wynik mnożenia liczb {liczba1} oraz {liczba2} to {mnozenie(liczba1, liczba2)}")
elif dzialanie == 4:
    if liczba1 == 0 or liczba2 == 0:
        print("Dzielenie przez 0!")
    else:
        print(f"Wynik dzielenia liczb {liczba1} oraz {liczba2} to {dzielenie(liczba1, liczba2)}")
else:
    print("Podano nieprawidłowe działanie!")