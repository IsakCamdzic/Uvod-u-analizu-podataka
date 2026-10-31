# =============================================================
# PRIMJER 1: CSV fajlovi bez pandasa (modul csv)
# Uvod u analizu podataka - Vježbe, Sedmica 4
# =============================================================
# CSV (Comma Separated Values) je tekstualni fajl u kojem je svaki
# red jedan zapis, a vrijednosti su odvojene zarezom. Prvi red je
# zaglavlje sa nazivima kolona:
#
#   ime,smjer,godina,matematika,programiranje,statistika,prisustvo
#   Amra,Informatika,1,7,10,6,70
#
# Modul csv je dio Pythona - ništa ne treba instalirati.
# =============================================================
import csv
import os

# Fajl studenti.csv je u istom folderu kao ova skripta
FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER, "studenti.csv")

# --- 1. Čitanje: csv.DictReader ------------------------------
# DictReader svaki red pretvori u rječnik: ključevi su nazivi kolona.
# Rezultat je LISTA RJEČNIKA - isti oblik kao To-do lista prošle sedmice.
studenti = []
with open(FAJL, "r", encoding="utf-8") as f:
    citac = csv.DictReader(f)
    for red in citac:
        studenti.append(red)

print("Broj studenata:", len(studenti))
print("Prvi student (sve je tekst!):", studenti[0])

# --- 2. Pretvaranje tipova -----------------------------------
# CSV ne zna za brojeve - sve što pročitamo je tekst (str).
# Ocjene i prisustvo pretvaramo u int.
for s in studenti:
    for kolona in ["godina", "matematika", "programiranje", "statistika", "prisustvo"]:
        s[kolona] = int(s[kolona])

print("Prvi student (sa brojevima):", studenti[0])

# --- 3. Nova vrijednost: prosjek za svakog studenta ----------
for s in studenti:
    s["prosjek"] = (s["matematika"] + s["programiranje"] + s["statistika"]) / 3

# --- 4. Sortiranje liste rječnika (key=lambda) ---------------
najbolji = sorted(studenti, key=lambda s: s["prosjek"], reverse=True)
print("\nTop 3 studenta:")
for i, s in enumerate(najbolji[:3], start=1):
    print(f"{i}. {s['ime']} ({s['smjer']}) - {s['prosjek']:.2f}")

# --- 5. Grupisanje: rječnik listi ----------------------------
# Ključ = smjer, vrijednost = lista studenata tog smjera
po_smjeru = {}
for s in studenti:
    smjer = s["smjer"]
    if smjer not in po_smjeru:
        po_smjeru[smjer] = []          # prvi student tog smjera
    po_smjeru[smjer].append(s)

# Isto, ali kraće - defaultdict sam napravi praznu listu:
from collections import defaultdict
po_godini = defaultdict(list)
for s in studenti:
    po_godini[s["godina"]].append(s)

print("\nBroj studenata po smjeru:")
for smjer, lista in po_smjeru.items():
    print(f"  {smjer}: {len(lista)}")

print("Broj studenata po godini:")
for godina in sorted(po_godini):
    print(f"  {godina}. godina: {len(po_godini[godina])}")

# --- 6. Pisanje: csv.DictWriter ------------------------------
IZLAZ = os.path.join(FOLDER, "izvjestaj_primjer.csv")
with open(IZLAZ, "w", newline="", encoding="utf-8") as f:
    pisac = csv.DictWriter(f, fieldnames=["smjer", "broj_studenata"])
    pisac.writeheader()                                  # red sa nazivima kolona
    for smjer, lista in po_smjeru.items():
        pisac.writerow({"smjer": smjer, "broj_studenata": len(lista)})
print("\nIzvještaj sačuvan u:", IZLAZ)

# --- 7. Prljavi podaci: try / except ValueError --------------
# U stvarnim podacima se često nađe nešto što nije broj.
vrijednosti = ["8", "9", "n/a", "7", "", "10"]
ispravne = []
neispravne = 0
for v in vrijednosti:
    try:
        ispravne.append(int(v))
    except ValueError:                # int("n/a") i int("") bacaju ValueError
        neispravne += 1
print("\nIspravne vrijednosti:", ispravne)
print("Preskočeno neispravnih:", neispravne)
