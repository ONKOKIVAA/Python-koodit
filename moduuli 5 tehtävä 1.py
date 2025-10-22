import random


lukumaara  = int(input("Anna arpakuutioiden lukumaara: "))


summa = 0

for i in range(lukumaara):

    silmaluku = random.randint(1, 6)
    print(f"{i+1}. noppa: {silmaluku}")
    summa += silmaluku


print(f"Silmälukujen summa on: {summa}")
