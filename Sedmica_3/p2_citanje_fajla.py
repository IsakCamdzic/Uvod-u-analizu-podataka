# =============================================================
# PRIMJER 2: Čitanje i pisanje tekstualnih fajlova
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
import os

# Putanja do fajla koji se nalazi u istom folderu kao ova skripta
# (tako Python pronađe fajl bez obzira odakle pokrećeš program)
FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")

# --- 1. Čitanje cijelog fajla red po red -------------------
# "with" automatski zatvara fajl kad završimo
# "r" = read (čitanje), encoding="utf-8" = da rade naša slova
with open(FAJL, "r", encoding="utf-8") as f:
    redovi = f.readlines()          # lista stringova, svaki red je jedan string

print("Prvi red (sirovo):", repr(redovi[0]))   # vidi se i "\n" na kraju!

# --- 2. Čišćenje: strip() i preskakanje praznih redova -----
datumi = []
for red in redovi:
    red = red.strip()               # ukloni razmake i "\n" sa krajeva
    if red == "":                   # prazan red -> preskoči
        continue
    datumi.append(red)

print("Prvih 5 datuma:")
for d in datumi[:5]:
    print("  ", d)
print("Ukupno datuma u fajlu:", len(datumi))

# --- 3. Rastavljanje stringa: split() ----------------------
prvi = datumi[0]                    # npr. "15-06"
dan, mjesec = prvi.split("-")       # "15-06" -> ["15", "06"]
print(f"Datum {prvi}: dan = {int(dan)}, mjesec = {int(mjesec)}")

# --- 4. Pisanje u fajl: "w" (write) ------------------------
# "w" pravi novi fajl (ili BRIŠE stari sadržaj ako fajl postoji)
IZLAZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "primjer_izlaz.txt")

with open(IZLAZ, "w", encoding="utf-8") as f:
    f.write("Ukupno rođendana: " + str(len(datumi)) + "\n")
    f.write("Prvi datum: " + datumi[0] + "\n")

# --- 5. Dodavanje na kraj fajla: "a" (append) ---------------
with open(IZLAZ, "a", encoding="utf-8") as f:
    f.write("Zadnji datum: " + datumi[-1] + "\n")

# --- 6. Čitanje onoga što smo upisali -----------------------
with open(IZLAZ, "r", encoding="utf-8") as f:
    sadrzaj = f.read()              # cijeli fajl kao jedan string

print("\nSadržaj fajla primjer_izlaz.txt:")
print(sadrzaj)
