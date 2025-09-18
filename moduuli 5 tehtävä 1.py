import random


lukumäärä = int(input("Anna arpakuutioiden lukumäärä: "))


summa = 0

for i in range(lukumäärä):

    silmaluku = random.randint(1, 6)
    print(f"{i+1}. noppa: {silmaluku}")
    summa += silmaluku


print(f"Silmälukujen summa on: {summa}")
