# =============================================================
# ZADATAK 1: Stvarni rođendani - da li se paradoks potvrdio?
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
# U fajlu real_birthdays.txt su rođendani studenata (format DD-MM).
# Provjeri da li u našoj grupi postoje isti rođendani i uporedi
# rezultat sa teorijom (Birthday Paradox).
# =============================================================
import os
from collections import Counter
from concurrent.interpreters import list_all
from os.path import split

# Putanja do fajla koji se nalazi u istom folderu kao ova skripta
FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")

# --- Učitavanje ---------------------------------------------
# Učitaj sve datume iz fajla u listu datumi.
# Savjet: with open(FAJL, "r", encoding="utf-8") as f:
#         strip() i preskoči prazne redove
datumi = []
with open(FAJL, "r", encoding="utf-8") as f:
        for red in f:
            red = red.strip()
            if red != "":
                datumi.append(red)


# a) Koliko je ukupno rođendana?            (očekivano: 38)
ukupno_datuma = len(datumi)
print(f"Koliko je ukupno rodjendana? {ukupno_datuma}\n")

# b) Koliko je JEDINSTVENIH rođendana?      (očekivano: 34)
jedinstveni = set(datumi)
broj_jedinstvenih = len(jedinstveni)
print(f"Koliko je jedinstvenih rodjendana? {broj_jedinstvenih}\n")


# c) Postoje li duplikati? Ispiši True/False.
print(f"Postoje li duplikati: {jedinstveni != ukupno_datuma}\n")

# d) Koji se datumi ponavljaju? Ispiši ih SORTIRANO, npr:
#       03-01 -> 2 puta
#    Savjet: Counter(datumi), pa sorted(...)
brojac = Counter(datumi)
print("Datumi koji se ponavljaju:")
for datum, broj in sorted(brojac.items()):
    if broj > 1:
        print(f"{datum} -> {broj} puta")
print()

# e) Uporedi sa teorijom.
#    Vjerovatnoća da u grupi od n osoba NIKO nema isti rođendan je:
#       (365/365) * (364/365) * (363/365) * ... * ((365-n+1)/365)
#    Vjerovatnoća poklapanja = 1 - to.
#    Napiši funkciju i ispiši:
#       Teorijska vjerovatnoća za 38 osoba: 86.4%
def vjerovatnoca_poklapanja(n):
    niko_isti = 1.0
    for i in range(n):
        niko_isti = niko_isti * (365 - i) / 365
    return 1 - niko_isti

# e) Uporedi sa teorijom.
#    Vjerovatnoća da u grupi od n osoba NIKO nema isti rođendan je:
#       (365/365) * (364/365) * (363/365) * ... * ((365-n+1)/365)
#    Vjerovatnoća poklapanja = 1 - to.
#    Napiši funkciju i ispiši:
#    Teorijska vjerovatnoća za 38 osoba: 86.4%
p = vjerovatnoca_poklapanja(ukupno_datuma)
print(f"Teorijska vjerovatnoca za {ukupno_datuma} osoba: {p * 100:.1f}%\n")

# BONUS: Koliko je rođendana u svakom mjesecu?
#    Savjet: mjesec je dio iza crtice -> datum.split("-")[1]

lista_mjeseci = []
for datum in datumi:
    mjesec = datum.split("-")[1]
    lista_mjeseci.append(mjesec)

mjesecBrojac = Counter(lista_mjeseci)
for datum, broj in sorted(mjesecBrojac.items()):
    print(f"{datum} -> {broj}")
