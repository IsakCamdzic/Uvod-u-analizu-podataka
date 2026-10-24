# =============================================================
# PRIMJER 2: Liste i stringovi (znakovni nizovi)
# =============================================================

# --- Liste: uređena kolekcija elemenata ---------------------
temperature = [12, 15, 9, 18, 21, 17, 14]

print("Cijela lista:", temperature)
print("Broj elemenata:", len(temperature))
print("Suma:", sum(temperature))
print("Najmanja / najveća:", min(temperature), max(temperature))

# Indeksiranje počinje od 0!
print("Prvi element:", temperature[0])      # 12
print("Drugi element:", temperature[1])     # 15
print("Zadnji element:", temperature[-1])   # 14
print("Predzadnji:", temperature[-2])       # 17

# Rezanje (slicing): lista[od:do]  -> "do" NIJE uključen
print("Prva tri:", temperature[:3])         # [12, 15, 9]
print("Od trećeg do kraja:", temperature[2:])
print("Svaki drugi:", temperature[::2])

# Mijenjanje liste
temperature.append(20)                      # dodaj na kraj
temperature[0] = 11                         # promijeni prvi element
print("Nakon izmjena:", temperature)

# Provjera članstva: operator in
print("Da li je bilo 21 stepen?", 21 in temperature)   # True
print("Da li je bilo 30 stepeni?", 30 in temperature)  # False

# Sortiranje
print("Sortirano:", sorted(temperature))
print("Sortirano opadajuće:", sorted(temperature, reverse=True))

# --- Stringovi ----------------------------------------------
recenica = "Python je Odličan jezik za Analizu podataka"

print(len(recenica))            # broj znakova
print(recenica[0])              # 'P'
print(recenica[:6])             # 'Python'
print(recenica.lower())         # sve malim slovima
print(recenica.upper())         # sve velikim slovima

rijeci = recenica.split()       # rastavi na riječi -> lista!
print(rijeci)
print("Broj riječi:", len(rijeci))

print("podataka" in recenica)   # True
print(recenica.replace("Python", "R"))
