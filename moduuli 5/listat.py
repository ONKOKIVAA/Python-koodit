
def laske_summa(luvut):

    """Palauttaa listassa olevien kokonaislukujen summan."""

    return sum(luvut)


def main():
    # Laaditaan testilista
    luvut = [3, 7, 2, 8, 5]

    # Kutsutaan funktiota ja otetaan talteen sen palauttama arvo
    summa = laske_summa(luvut)

    # Tulostetaan tulos
    print(f"Listan {luvut} lukujen summa on {summa}.")


if __name__ == "__main__":
    main()