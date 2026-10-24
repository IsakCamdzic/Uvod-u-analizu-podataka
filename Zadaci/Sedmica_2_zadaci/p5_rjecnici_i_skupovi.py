# =============================================================
# PRIMJER 5: Rječnici (dict), skupovi (set) i Counter
# =============================================================
from collections import Counter

# --- Rječnik: parovi ključ -> vrijednost --------------------
student = {
    "ime": "Lejla",
    "godina_studija": 1,
    "ocjene": [9, 10, 8],
}

print(student["ime"])                       # Lejla
student["grad"] = "Sarajevo"                # dodavanje novog para
student["godina_studija"] = 2               # izmjena postojećeg
print(student)

print("ime" in student)                     # True  - postoji li ključ?
print(student.get("email", "nema emaila"))  # get ne baca grešku

# Prolazak kroz rječnik
for kljuc, vrijednost in student.items():
    print(kljuc, "->", vrijednost)

# --- Brojanje pomoću rječnika -------------------------------
boje = ["crvena", "plava", "crvena", "zelena", "plava", "crvena"]

brojac = {}
for b in boje:
    if b in brojac:
        brojac[b] += 1
    else:
        brojac[b] = 1
print(brojac)                   # {'crvena': 3, 'plava': 2, 'zelena': 1}

# Isto, ali jednostavnije - Counter (sa predavanja!)
c = Counter(boje)
print(c)
print(c.most_common(1))         # [('crvena', 3)]

# --- Skup (set): samo JEDINSTVENI elementi ------------------
brojevi = [1, 2, 2, 3, 3, 3, 4]
jedinstveni = set(brojevi)
print(jedinstveni)              # {1, 2, 3, 4}
print("Ukupno:", len(brojevi), "| Jedinstvenih:", len(jedinstveni))

# Provjera članstva u skupu je jako brza
print(3 in jedinstveni)         # True

# Operacije nad skupovima
python_studenti = {"Ana", "Emir", "Lejla"}
r_studenti = {"Emir", "Tarik"}
print("Oba jezika:", python_studenti & r_studenti)      # presjek
print("Bilo koji:", python_studenti | r_studenti)       # unija
print("Samo Python:", python_studenti - r_studenti)     # razlika
