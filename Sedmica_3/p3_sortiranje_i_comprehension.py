# =============================================================
# PRIMJER 3: Sortiranje, list comprehension, enumerate, zip, random
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
import random

# --- Sortiranje: sorted() vs .sort() ------------------------
x = [4, 1, 2, 3]
y = sorted(x)                    # vraća NOVU listu, x ostaje isti
print("sorted:", y, "| x je i dalje:", x)
x.sort()                         # sortira listu "na mjestu" (mijenja x)
print("x.sort():", x)

print("Opadajuće:", sorted([4, 1, 2, 3], reverse=True))

# key = po čemu sortiramo
rijeci = ["banana", "kivi", "jabuka", "šljiva"]
print("Po dužini:", sorted(rijeci, key=len))
print("Po apsolutnoj vrijednosti:", sorted([-4, 1, -2, 3], key=abs, reverse=True))

ocjene = [("Amra", 8), ("Emir", 10), ("Lejla", 7)]
# lambda = kratka funkcija bez imena: za par p vrati p[1] (ocjenu)
print("Po ocjeni:", sorted(ocjene, key=lambda p: p[1], reverse=True))

# --- List comprehension -------------------------------------
# [izraz  for element in kolekcija  if uslov]
kvadrati = [x * x for x in range(5)]
print("Kvadrati:", kvadrati)                       # [0, 1, 4, 9, 16]

parni = [x for x in range(10) if x % 2 == 0]
print("Parni:", parni)                             # [0, 2, 4, 6, 8]

# Isto bez comprehension-a (duže):
parni2 = []
for x in range(10):
    if x % 2 == 0:
        parni2.append(x)
print("Parni (petlja):", parni2)

velika = [r.upper() for r in rijeci]
print("Velikim slovima:", velika)

# Dict comprehension: {ključ: vrijednost for ...}
kvadrati_dict = {x: x * x for x in range(5)}
print("Rječnik kvadrata:", kvadrati_dict)

# --- enumerate: indeks + element ----------------------------
print("Lista voća:")
for i, voce in enumerate(rijeci, start=1):
    print(f"  {i}. {voce}")

# --- zip: spajanje dvije liste u parove ---------------------
imena = ["Ana", "Tarik", "Lejla"]
godine = [20, 22, 21]
for ime, god in zip(imena, godine):
    print(f"{ime} - godine: {god}")
print("zip kao lista:", list(zip(imena, godine)))

# --- random -------------------------------------------------
random.seed(10)                  # isti "seed" -> isti nasumični brojevi
print("randint(1, 6):", random.randint(1, 6))              # kocka
print("choice:", random.choice(imena))                     # jedan element
karte = [1, 2, 3, 4, 5]
random.shuffle(karte)                                      # promiješaj na mjestu
print("shuffle:", karte)
print("sample (3 bez ponavljanja):", random.sample(range(1, 40), 3))
