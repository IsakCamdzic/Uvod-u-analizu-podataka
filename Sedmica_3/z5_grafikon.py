# =============================================================
# ZADATAK 5: Grafikon - rođendani po mjesecima
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
# Nacrtaj stupčasti grafikon (bar chart) koji pokazuje koliko
# studenata iz real_birthdays.txt je rođeno u svakom mjesecu.
# (Prvo instaliraj matplotlib, vidi primjer p5_grafikon.py.)
# =============================================================
import os
from collections import Counter
from matplotlib import pyplot as plt

FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")
MJESECI = ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun",
           "Jul", "Avg", "Sep", "Okt", "Nov", "Dec"]

# a) Učitaj datume i prebroj koliko ih je u svakom mjesecu.
#    Mjesec je dio iza crtice: "15-06" -> 6
#    Savjet: Counter(...) ili rječnik
datumi = []
with open(FAJL, "r", encoding="utf-8") as f:
    for red in f:
        red = red.strip()
        if red != "":
            datumi.append(red)

lista_mjeseci = []
for datum in datumi:
    mjesec = datum.split("-")[1]
    lista_mjeseci.append(mjesec)

brojac = Counter(lista_mjeseci)

print(brojac)

# b) Napravi listu broj_po_mjesecima sa 12 brojeva, redom od januara
#    do decembra. Očekivano: [5, 2, 3, 3, 2, 2, 5, 6, 3, 3, 2, 2]
sortirano = sorted(brojac.items())
broj_po_mjesecima = [broj for mjesec, broj in sortirano]

print("Broj rođendana po mjesecima:", broj_po_mjesecima)

najveci = broj_po_mjesecima.index(max(broj_po_mjesecima))
boje = ["#4a90e2"] * len(broj_po_mjesecima)
boje[najveci] = "#e74c4c"

for x, y in zip(MJESECI, broj_po_mjesecima):
    plt.text(x, y + 0.1, str(y), ha="center")
# c) Nacrtaj bar chart:
#    plt.bar(MJESECI, broj_po_mjesecima)
#    naslov: "Rođendani po mjesecima (38 studenata)"
#    oznaka y ose: "Broj rođendana"
#    pa plt.show()
plt.bar(MJESECI, broj_po_mjesecima, color=boje)
plt.title("Rodjendani po mjesecima (38 studenata)")
plt.ylabel("Broj rodjendana")
plt.savefig("z5_grafikon.png")
plt.show()


# d) BONUS:
#    - mjesec sa najviše rođendana oboji drugom bojom
#      (savjet: lista boja, npr. ["#3A7CA5", ..., "#F2A541", ...] i color=boje)
#    - iznad svakog stupca ispiši broj (plt.text(x, y, tekst, ha="center"))
#    - sačuvaj sliku: plt.savefig("z5_grafikon.png") PRIJE plt.show()


