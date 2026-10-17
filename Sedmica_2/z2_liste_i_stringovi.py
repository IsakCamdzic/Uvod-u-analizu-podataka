# =============================================================
# ZADATAK 2: Liste i stringovi   (~7 minuta)
# =============================================================

ocjene = [8, 6, 10, 7, 9, 6, 8]

# a) Ispiši prvu i zadnju ocjenu.
print(f"Prva ocjena: {ocjene[0]}")
print(f"Zadnja ocjena: {ocjene[-1]}")

# b) Ispiši prve tri ocjene (koristi rezanje / slicing).
print(f"Prve tri ocjene: {ocjene[:3]}")


# c) Student je dobio još jednu ocjenu: 10. Dodaj je u listu.
ocjene.append(10)
print(f"Ocjene nakon dodavanja: {ocjene}")


# d) Izračunaj i ispiši prosjek ocjena na 2 decimale.
#    Savjet: sum() i len()
prosjek = sum(ocjene) / len(ocjene)
print(f"Prosjek ocjena: {prosjek:.2f}")

# e) Ispiši da li student ima ocjenu 6 (True/False).
print("Ima li ocjenu 6? ",6 in ocjene)


# f) Zadana je rečenica. Ispiši koliko ima riječi
#    i koja je najduža riječ.
#    Savjet: split(), a za najdužu riječ max(rijeci, key=len)
recenica = "analiza podataka pomaže da donosimo bolje odluke"
rijeci = recenica.split()
print("Broj rijeci: ", len(rijeci))
print("Najduza rijec: ", max(rijeci, key=len))
