# =============================================================
# PRIMJER 3: Uslovi (if/elif/else) i petlje (for, while)
# =============================================================

# --- if / elif / else ---------------------------------------
# Pažnja: Python koristi UVLAČENJE (4 razmaka) umjesto { }
temperatura = 23

if temperatura < 10:
    print("Hladno je, obuci jaknu.")
elif temperatura < 20:
    print("Prijatno je.")
else:
    print("Toplo je!")

# Ternarni if u jednom redu
broj = 7
parnost = "paran" if broj % 2 == 0 else "neparan"
print(broj, "je", parnost)

# Logički operatori: and, or, not
godine = 20
ima_indeks = True
if godine >= 18 and ima_indeks:
    print("Može upisati ispit.")

# --- for petlja ---------------------------------------------
# range(5) daje 0, 1, 2, 3, 4
for i in range(5):
    print("Ponavljanje broj", i)

# range(od, do, korak)
for i in range(10, 0, -2):
    print(i, end=" ")       # end=" " -> ispis u istom redu
print()

# Petlja kroz listu
voce = ["jabuka", "kruška", "šljiva"]
for v in voce:
    print("Volim", v)

# Sabiranje u petlji (akumulator)
suma = 0
for broj in [4, 8, 15, 16, 23, 42]:
    suma += broj            # isto kao: suma = suma + broj
print("Suma je", suma)

# --- while petlja -------------------------------------------
# Ponavlja se DOK je uslov tačan
x = 1
while x < 100:
    x = x * 2
print("Prvi stepen dvojke veći od 100:", x)

# --- break i continue ---------------------------------------
for x in range(10):
    if x == 3:
        continue            # preskoči ostatak i idi na sljedeći krug
    if x == 6:
        break               # potpuno izađi iz petlje
    print(x, end=" ")       # ispisuje: 0 1 2 4 5
print()

# --- Ugniježđene petlje: tablica množenja -------------------
for red in range(1, 4):
    for kolona in range(1, 4):
        print(red * kolona, end="\t")
    print()
