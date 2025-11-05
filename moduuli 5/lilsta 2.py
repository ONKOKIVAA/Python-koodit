def poista_parittomat(luvut):
    """Palauttaa uuden listan, josta on poistettu kaikki parittomat luvut."""
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:  # Jos luku on parillinen
            parilliset.append(luku)
    return parilliset


def main():
    # Laaditaan testilista
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Kutsutaan funktiota
    karsitut = poista_parittomat(luvut)

    # Tulostetaan molemmat listat
    print(f"Alkuperäinen lista: {luvut}")
    print(f"Parittomat poistettu: {karsitut}")


if __name__ == "__main__":
    main()
