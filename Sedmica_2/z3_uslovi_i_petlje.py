# =============================================================
# ZADATAK 3: Uslovi i petlje   (~10 minuta)
# =============================================================
import random

# a) Korisnik unese broj bodova (0-100). Ispiši ocjenu:
#      0-54 -> 5,  55-64 -> 6,  65-74 -> 7,
#      75-84 -> 8, 85-94 -> 9,  95-100 -> 10
bodovi = int(input("Unesi bodovi: "))
if(bodovi > 94):
    ocjena = 10
elif(bodovi > 84):
    ocjena = 9
elif(bodovi > 74):
    ocjena = 8
elif(bodovi > 64):
    ocjena = 7
elif(bodovi > 54):
    ocjena = 6
else:
    ocjena = 5
print(ocjena)

# b) Pomoću for petlje izračunaj sumu svih PARNIH brojeva od 1 do 100.
#    (Rezultat treba biti 2550)
zbir = 0
for i in range(0,101,2):
    zbir += i
print(zbir)

# c) MINI IGRA "Pogodi broj"
#    Računar zamisli broj od 1 do 20 (već napisano ispod).
#    Pomoću while petlje traži od korisnika da pogađa dok ne pogodi.
#    Nakon svakog pokušaja ispiši "Više!" ili "Manje!".
#    Na kraju ispiši iz koliko pokušaja je pogodio.
tajni_broj = random.randint(1, 20)
print(tajni_broj)
pokusaji = 0
pogodak = None

while pogodak != tajni_broj:
    pogodak = int(input("Unesi broj: (1-20): "))
    pokusaji += 1
    if pogodak < tajni_broj:
        print("Vise")
    elif pogodak > tajni_broj:
        print("Manje")

print(f"Bravo! Pogodio si broj {tajni_broj}, iz {pokusaji} pokusaja.")
