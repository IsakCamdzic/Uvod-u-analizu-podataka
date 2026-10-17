# ZADATAK 4: Funkcije   (~8 minuta)
# =============================================================

# a) Napiši funkciju prosjek(lista) koja vraća prosjek brojeva u listi.
#    Ako je lista prazna, neka vrati 0.
def prosjek(lista):
    if(lista == []):
        return 0
    prosjek = sum(lista) / len(lista)
    return prosjek

# b) Napiši funkciju je_paran(n) koja vraća True ako je n paran,
#    a False ako nije.
def je_paran(n):
    if(n % 2 == 0):
        return True
    else:
        return False


# c) Napiši funkciju ocjena(bodovi) koja vraća ocjenu prema
#    pravilima iz Zadatka 3a.
def ocjena(bodovi):
    # TODO
    pass


# d) Napiši funkciju samo_parni(lista) koja vraća NOVU listu
#    samo sa parnim brojevima. Iskoristi funkciju je_paran!
def samo_parni(lista):
    nova_lista = []
    for i in lista:
        if(i % 2 == 0):
            nova_lista.append(i)
    return nova_lista


# --- Testiranje (ne mijenjaj) -------------------------------
print(prosjek([8, 9, 10]))          # 9.0
print(prosjek([]))                  # 0
print(je_paran(4), je_paran(7))     # True False
print(samo_parni([1, 2, 3, 4, 5, 6]))        # [2, 4, 6]
