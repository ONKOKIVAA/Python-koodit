import random

def heita_noppaa():
    """Palauttaa satunnaisen nopan silmäluvun väliltä 1..6."""
    return random.randint(1, 6)

def main():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print(f"Heitto: {silmaluku}")

if __name__ == "__main__":
    main()