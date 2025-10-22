luvut = []


while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    try:
        luku = int(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte, anna kokonaisluku.")


luvut.sort(reverse=True)


print("\nViisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)