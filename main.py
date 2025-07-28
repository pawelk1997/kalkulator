import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def dodawanie(liczba1, liczba2):
    logging.info(f"Dodaję {liczba1} i {liczba2}")
    return liczba1 + liczba2

def odejmowanie(liczba1, liczba2):
    logging.info(f"Odejmuję {liczba1} i {liczba2}")
    return liczba1 - liczba2

def mnozenie(liczba1, liczba2):
    logging.info(f"Mnożę {liczba1} i {liczba2}")
    return liczba1 * liczba2

def dzielenie(liczba1, liczba2):
    if liczba2 == 0:
        logging.error("Próba dzielenia przez zero!")
        return "Błąd! Nie można dzielić przez zero!"
    logging.info(f"Dzielę {liczba1} i {liczba2}")
    return liczba1 / liczba2

if __name__ == "__main__":
    print("Kalkulator")
    while True:
        print("Podaj działanie, posługując się odpowiednią liczbą: 1 - Dodawanie, 2 - Odejmowanie, 3 -  Mnożenie, 4 - Dzielenie, 5 - Zamknij program")

        dzialanie = input("Podaj działanie: ")

        if dzialanie == "5":
            logging.info("Zamykam progam")
            break

        if dzialanie in ("1", "2", "3", "4"):
            try:
                liczba1 = float(input("Podaj pierwszą liczbę: "))
                liczba2 = float(input("Podaj drugą liczbę: "))
            except ValueError:
                logging.warning("Podano nieprawidłowe dane wejściowe. Należy wprowadzić liczby. Spróbuj jeszcze raz.")
                continue

            if dzialanie == "1":
                wynik = dodawanie(liczba1, liczba2)
            elif dzialanie == "2":
                wynik = odejmowanie(liczba1, liczba2)
            elif dzialanie == "3":
                wynik = mnozenie(liczba1, liczba2)
            elif dzialanie == "4":
                wynik = dzielenie(liczba1, liczba2)

            print(f"Wynik: {wynik}")
        else:
            logging.warning("Podano nieprawidłowe działanie! Spróbuj jeszcze raz!")