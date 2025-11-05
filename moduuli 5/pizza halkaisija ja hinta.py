import math

def yksikkohinta(halkaisija, hinta):
    """Laskee ja palauttaa pizzan hinnan euroina per neliömetri."""
    # Muutetaan halkaisija metreiksi
    sade = (halkaisija / 100) / 2
    # Lasketaan pinta-ala (πr²)
    pinta_ala = math.pi * sade ** 2
    # Lasketaan yksikköhinta
    return hinta / pinta_ala

def main():
    print("Anna ensimmäisen pizzan tiedot:")
    halkaisija1 = float(input("Halkaisija (cm): "))
    hinta1 = float(input("Hinta (€): "))

    print("\nAnna toisen pizzan tiedot:")
    halkaisija2 = float(input("Halkaisija (cm): "))
    hinta2 = float(input("Hinta (€): "))

    # yksikköhintojen laskeminen funktiolla
    hinta_per_m2_1 = yksikkohinta(halkaisija1, hinta1)
    hinta_per_m2_2 = yksikkohinta(halkaisija2, hinta2)

    # tuloksien tulostaminen
    print(f"\nPizza 1: {hinta_per_m2_1:.2f} €/m²")
    print(f"Pizza 2: {hinta_per_m2_2:.2f} €/m²")

    # Verrataan vaihtoehtoja kumpi on edullisempi
    if hinta_per_m2_1 < hinta_per_m2_2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif hinta_per_m2_2 < hinta_per_m2_1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Pizzat ovat yhtä edullisia.")

if __name__ == "__main__":
    main()