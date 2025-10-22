luvut = []


while True:
    syöte = input("Anna luku (tai tyhjä lopettaaksesi): ")
    if syöte == "":
        break
    try:
        luku = int(syöte)
        luvut.append(luku)
    except ValueError:
        print("Anna kelvollinen kokonaisluku.")


luvut.sort(reverse=True)

viisi_suurinta = luvut[:5]


print("Viisi suurinta lukua:")
for luku in viisi_suurinta:
    print(luku)