# =============================================================
# ZADATAK 1: Izvještaj po smjeru (BEZ pandasa - samo modul csv)
# Uvod u analizu podataka - Vježbe, Sedmica 4
# =============================================================
# Fajl studenti.csv ima kolone:
#   ime,smjer,godina,matematika,programiranje,statistika,prisustvo
#
# a) Učitaj fajl u LISTU RJEČNIKA (csv.DictReader). Kolone godina,
#    matematika, programiranje, statistika i prisustvo pretvori u int.
#
# b) Svakom studentu dodaj ključ "prosjek":
#       (matematika + programiranje + statistika) / 3
#
# c) Grupiši studente po smjeru: rječnik u kojem je ključ smjer,
#    a vrijednost lista studenata tog smjera.
#
# d) Za svaki smjer izračunaj: broj studenata, prosjek smjera
#    (prosjek prosjeka) i najboljeg studenta. Ispiši smjerove
#    sortirane po prosjeku OPADAJUĆE, tačno ovako:
#
#    Informatika: 14 studenata, prosjek 8.10, najbolji: Ema (9.00)
#    Elektrotehnika: 14 studenata, prosjek 7.29, najbolji: Dino (8.33)
#    Menadžment: 12 studenata, prosjek 7.00, najbolji: Lana (7.67)
#
#    Savjet: max(lista, key=lambda s: s["prosjek"])
#            sorted(..., key=lambda r: r["prosjek"], reverse=True)
#
# e) Upiši izvještaj u fajl "izvjestaj_smjerovi.csv" sa kolonama:
#       smjer,broj_studenata,prosjek,najbolji
#    Savjet: csv.DictWriter, writeheader(), writerow()
#
# BONUS: napiši funkciju polozio(student) koja vraća True ako su sve
#        tri ocjene >= 6. Koliko je studenata položilo?  (očekivano: 25)
# =============================================================
import csv
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER, "studenti.csv")
IZLAZ = os.path.join(FOLDER, "izvjestaj_smjerovi.csv")

# a) TODO: učitaj studente u listu rječnika
studenti = []
with open(FAJL, "r", encoding="utf-8") as f:
    citac = csv.DictReader(f)
    for red in citac:
        red["matematika"] = int(red["matematika"])
        red["programiranje"] = int(red["programiranje"])
        red["statistika"] = int(red["statistika"])
        studenti.append(red)



print("Učitano studenata:", len(studenti))      # očekivano: 40


# b) TODO: dodaj ključ "prosjek" svakom studentu
for s in studenti:
    s["prosjek"] = (s["matematika"] + s["programiranje"] + s["statistika"]) / 3
    print(s["prosjek"])

# c) TODO: grupiši po smjeru
po_smjeru = {}
for s in studenti:
    smjer = s["smjer"]
    if smjer not in po_smjeru:
        po_smjeru[smjer] = []
    po_smjeru[smjer].append(s)

# d) TODO: izvještaj za svaki smjer, sortiran po prosjeku opadajuće
print("\nBroj studenata po smjeru:")
for smjer, lista in po_smjeru.items():
    print(f"  {smjer}: {len(lista)}")

# e) TODO: upiši izvještaj u izvjestaj_smjerovi.csv
with open(IZLAZ, "w", newline="", encoding="utf-8") as f:
    pisac = csv.DictWriter(f, fieldnames=["smjer", "broj_studenata"])
    pisac.writeheader()                                  # red sa nazivima kolona
    for smjer, lista in po_smjeru.items():
        pisac.writerow({"smjer": smjer, "broj_studenata": len(lista)})
print("\nIzvještaj sačuvan u:", IZLAZ)

# BONUS: TODO
def polozio(student):
    return False
