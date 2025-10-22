import random


lukumäärä = int(input("Anna arpakuutioiden lukumäärä: "))


summa = 0


for i in range(lukumäärä):
    heitto = random.randint(1, 6)
    print(f"{i+1}. noppa: {heitto}")
    summa += heitto


print(f"Silmälukujen summa on: {summa}")