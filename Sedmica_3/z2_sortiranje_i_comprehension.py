# =============================================================
# ZADATAK 2: Sortiranje, list comprehension, zip, enumerate, random
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
import os
import random

studenti = ["Amra", "Emir", "Lejla", "Tarik", "Ana"]
bodovi = [78, 92, 65, 88, 92]

# a) Pomoću zip() napravi listu parova (ime, bodovi) i ispiši
#    svaki par u obliku:   Amra: 78
parovi = list(zip(studenti, bodovi))
for studenti, bodovi in parovi:
    print(f"{studenti}: {bodovi}")


# b) Sortiraj parove po bodovima OPADAJUĆE i ispiši rang listu
#    pomoću enumerate(..., start=1):
#       1. Emir - 92
#       2. Ana - 92
#       ...
#    Savjet: sorted(parovi, key=lambda p: p[1], reverse=True)
print("\nRang lista:")
rang = sorted(parovi, key=lambda x: x[1], reverse=True)
for mjesto, (ime, b) in enumerate(rang, start=1):
    print(f"{mjesto}: {ime} - {b}")






# c) List comprehension: lista imena studenata sa 80 ili više bodova.
#    Očekivano: ['Emir', 'Tarik', 'Ana']
dobri = [ime for ime, b in parovi if b >= 80]
print("\n80 ili vise bodova:", dobri)

# d) Iz fajla real_birthdays.txt (format DD-MM) napravi pomoću
#    list comprehension-a listu MJESECI kao brojeve (int),
#    a zatim ispiši sortirane jedinstvene mjesece.
#    Očekivano: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")
# TODO


# e) random: postavi random.seed(42), pa
#    - nasumično izaberi studenta koji odgovara (random.choice)
#    - napravi KOPIJU liste studenti i promiješaj je (random.shuffle)
#      -> to je redoslijed prezentacija
# TODO
