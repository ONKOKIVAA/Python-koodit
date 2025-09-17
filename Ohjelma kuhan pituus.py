pituus = int(input("Anna kuhan pituus senttimetreinä: "))

alin_mitta = 37

if pituus < alin_mitta:
    puuttuu = alin_mitta - pituus
    print("Kuha on alamittainen. Laske kuha takaisin järveen!")
    print(f"Kuha on {puuttuu} cm liian lyhyt.")
else:
    print("Kuha on tarpeeksi suuri. Voit pitää sen.")



