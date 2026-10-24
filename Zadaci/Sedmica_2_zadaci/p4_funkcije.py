# =============================================================
# PRIMJER 4: Funkcije
# =============================================================

# Funkcija = imenovani dio koda koji prima ulaze i vraća izlaz.
# Pišemo je jednom, koristimo koliko god puta želimo.

def kvadrat(x):
    """Vraća kvadrat broja x."""
    return x * x

print(kvadrat(4))           # 16
print(kvadrat(2.5))         # 6.25


# Funkcija sa više parametara
def povrsina_pravougaonika(a, b):
    """Vraća površinu pravougaonika sa stranicama a i b."""
    return a * b

print(povrsina_pravougaonika(3, 5))   # 15


# Podrazumijevana (default) vrijednost parametra
def pozdrav(ime="studente"):
    print(f"Zdravo, {ime}!")

pozdrav("Emir")             # Zdravo, Emir!
pozdrav()                   # Zdravo, studente!


# Imenovani argumenti
def oduzmi(a=0, b=0):
    return a - b

print(oduzmi(10, 5))        # 5
print(oduzmi(b=5))          # -5


# Funkcija koja vraća više vrijednosti (tuple)
def min_i_max(lista):
    return min(lista), max(lista)

najmanji, najveci = min_i_max([4, 9, 1, 7])
print("Min:", najmanji, "Max:", najveci)


# Funkcija koja koristi drugu funkciju
def zbir_kvadrata(lista):
    zbir = 0
    for broj in lista:
        zbir += kvadrat(broj)
    return zbir

print(zbir_kvadrata([1, 2, 3]))      # 1 + 4 + 9 = 14


# Funkcija koja vraća True / False (korisno u if naredbama!)
def je_punoljetan(godine):
    return godine >= 18

if je_punoljetan(20):
    print("Punoljetan je.")


# Razlika: print vs return
def vrati_dvostruko(x):
    return 2 * x            # vraća vrijednost - možemo je dalje koristiti

def ispisi_dvostruko(x):
    print(2 * x)            # samo ispisuje - vraća None

rezultat = vrati_dvostruko(5) + 1    # 11
print(rezultat)
