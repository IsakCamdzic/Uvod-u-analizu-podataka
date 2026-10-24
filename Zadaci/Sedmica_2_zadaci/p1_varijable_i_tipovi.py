# =============================================================
# PRIMJER 1: Varijable, tipovi podataka, ispis i aritmetika
# Uvod u analizu podataka - Vježbe, Sedmica 2
# =============================================================

# --- Varijable i tipovi -------------------------------------
# U Pythonu ne deklarišemo tip - Python ga sam odredi (dinamički tipovi)
ime = "Amra"            # str  (tekst)
godine = 21             # int  (cijeli broj)
prosjek = 8.75          # float (decimalni broj)
redovan_student = True  # bool (True / False)

print(ime, godine, prosjek, redovan_student)
print(type(ime), type(godine), type(prosjek), type(redovan_student))

# Ista varijabla može kasnije dobiti vrijednost drugog tipa
x = 10
print("x =", x, type(x))
x = "deset"
print("x =", x, type(x))

# --- Lijep ispis: f-string ----------------------------------
print(f"Studentica {ime} ima {godine} godina i prosjek {prosjek}.")
print(f"Prosjek zaokružen na 1 decimalu: {prosjek:.1f}")

# --- Aritmetika ---------------------------------------------
a = 17
b = 5
print("a + b  =", a + b)    # 22
print("a - b  =", a - b)    # 12
print("a * b  =", a * b)    # 85
print("a / b  =", a / b)    # 3.4  -> obično dijeljenje (uvijek float)
print("a // b =", a // b)   # 3    -> cjelobrojno dijeljenje
print("a % b  =", a % b)    # 2    -> ostatak pri dijeljenju
print("a ** 2 =", a ** 2)   # 289  -> stepenovanje

# --- Pretvaranje tipova -------------------------------------
tekst = "42"
broj = int(tekst)           # "42" -> 42
print(broj + 8)             # 50
print(str(broj) + "8")      # "428"  (spajanje teksta!)

# --- Unos sa tastature --------------------------------------
# input() UVIJEK vraća tekst (str), zato ga pretvaramo u int/float
unos = input("Unesi neki broj: ")
broj = float(unos)
print(f"Dupla vrijednost broja {broj} je {broj * 2}")
