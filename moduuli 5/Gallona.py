def gallonat_litroiksi(gallonat):
    """Muuntaa annetun bensiinin määrän (gallonina) litroiksi."""
    return gallonat * 3.785

def main():
    while True:
        gallonat = float(input("Anna bensiinin määrä (gallonina, negatiivinen lopettaa): "))
        if gallonat < 0:
            print("Ohjelma lopetetaan.")
            break
        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat:.2f} gallonaa on {litrat:.2f} litraa.")

if __name__ == "__main__":
    main()