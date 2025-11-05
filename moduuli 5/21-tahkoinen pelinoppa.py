import random


def heita_noppaa(tahkojen_maara):
    """Palauttaa satunnaisen nopan silmäluvun väliltä 1..tahkojen_maara."""
    return random.randint(1, tahkojen_maara)


def main():
    # Käyttäjältä kysytään, kuinka monta tahkoa nopassa on
    tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

    silmaluku = 0
    # Noppaa heitetään, kunnes saadaan maksimisilmäluku
    while silmaluku != tahkojen_maara:
        silmaluku = heita_noppaa(tahkojen_maara)
        print(f"Heitto: {silmaluku}")


if __name__ == "__main__":
    main()