import math

# Kysytään käyttäjältä säde
sade = float(input("Anna ympyrän säde: "))

# Lasketaan pinta-ala (A = π * r^2)
pinta_ala = math.pi * sade ** 2

# Tulostetaan tulos
print(f"Ympyrän pinta-ala on {pinta_ala:.2f}")
