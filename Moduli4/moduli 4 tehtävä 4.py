import random


oikea_luku = random.randint(1, 10)

while True:
    syote = input("Arvaa luku (1–10): ")


    try:
        arvaus = int(syote)

    except ValueError:

        print("Anna kelvollinen kokonaisluku.")
        continue

    if arvaus < oikea_luku:
        print("Liian pieni arvaus.")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus.")
    else:
        print("Oikein!")
        break