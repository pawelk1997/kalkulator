import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def dodawanie(*liczby):
    """Adds any number of numbers."""
    if not liczby:
        logging.warning("Brak liczb do dodania.")
        return 0
    operacja_str = " + ".join(map(str, liczby))
    logging.info(f"Dodaję: {operacja_str}")
    return sum(liczby)

def odejmowanie(liczba1, liczba2):
    """Subtracts two numbers."""
    logging.info(f"Odejmuję {liczba2} od {liczba1}")
    return liczba1 - liczba2

def mnozenie(*liczby):
    """Multiplies any number of numbers."""
    if not liczby:
        logging.warning("Brak liczb do pomnożenia.")
        return 1
    operacja_str = " * ".join(map(str, liczby))
    logging.info(f"Mnożę: {operacja_str}")
    wynik = 1
    for liczba in liczby:
        wynik *= liczba
    return wynik

def dzielenie(liczba1, liczba2):
    """Divides the first number by the second, supporting division by zero."""
    if liczba2 == 0:
        logging.error("Próba dzielenia przez zero!")
        return "Błąd! Nie można dzielić przez zero!"
    logging.info(f"Dzielę {liczba1} przez {liczba2}")
    return liczba1 / liczba2

if __name__ == "__main__":
    print("Kalkulator")
    while True:
        print("Podaj działanie, posługując się odpowiednią liczbą: 1 - Dodawanie, 2 - Odejmowanie, 3 -  Mnożenie, 4 - Dzielenie, 5 - Zamknij program")

        dzialanie = input("Podaj działanie: ")

        if dzialanie == "5":
            logging.info("Zamykam program")
            break

        wynik = None

        if dzialanie == "1" or dzialanie == "3":
            try:
                ile_liczb = int(input("Ile liczb chcesz użyć do tej operacji? "))
                if ile_liczb <= 0:
                    logging.warning("Liczba liczb do obliczenia musi być większa niż zero! Spróbnuj jeszcze raz!")
                    continue
            except ValueError:
                logging.warning("Nieprawidłowe dane. Podaj liczbę całkowitą!")
                continue
            
            liczby = []
            for i in range(ile_liczb):
                while True:
                    try:
                        liczba = float(input("Podaj kolejną liczbę: "))
                        liczby.append(liczba)
                        break
                    except ValueError:
                        logging.warning("Nieprawidłowe dane. Podaj właściwą liczbę!")

            if not liczby:
                logging.warning("Nie podano żadnych liczb. Spróbuj jeszcze raz!")
                continue

            if dzialanie == "1":
                wynik = dodawanie(*liczby)
            elif dzialanie == "3":
                wynik = mnozenie(*liczby)

        elif dzialanie == "2" or dzialanie == "4":
            try:
                liczba1 = float(input("Podaj pierwszą liczbę: "))
                liczba2 = float(input("Podaj drugą liczbę: "))
            except ValueError:
                logging.warning("Podano nieprawidłowe dane wejściowe. Należy wprowadzić liczby. Spróbuj jeszcze raz!")
                continue

            if dzialanie == "2":
                wynik = odejmowanie(liczba1, liczba2)
            elif dzialanie == "4":
                wynik = dzielenie(liczba1, liczba2)
        else:
            logging.warning("Podano nieprawidłowe działanie! Spróbuj jeszcze raz!")
            continue

        if isinstance(wynik, (int, float)):
            logging.info(f"Wynik operacji: {wynik}")
            print(f"Wynik: {wynik}")
        elif isinstance(wynik, str) and "Błąd" in wynik:
            logging.error(f"Operacja zakończyła się błędem: {wynik}")
            print(f"Wynik: {wynik}")