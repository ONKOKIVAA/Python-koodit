oikea_kayttajatunnus = "python"
oikea_salasana = "rules"

yritykset: int = 0
maksimi_yritykset: int = 5

while yritykset < maksimi_yritykset:
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        print("Virheellinen käyttäjätunnus tai salasana.")
        yritykset += 1

if yritykset == maksimi_yritykset:
    print("Pääsy evätty")