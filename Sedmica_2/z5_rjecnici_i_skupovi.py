# =============================================================
# ZADATAK 5: Rječnici i skupovi - "Rođendani u grupi"  (~5 minuta)
# Veza sa predavanjem: Birthday Paradox
# =============================================================

from collections import Counter
rodjendani = [
    "03-14", "07-22", "11-05", "03-14", "01-30", "09-09",
    "12-25", "07-22", "05-17", "02-28", "10-10", "07-22",
    "04-01", "08-15", "06-06", "11-05", "03-03", "09-18",
]

# a) Koliko je ukupno rođendana u listi?
ukupno = len(rodjendani)
print(f"Ukupno rodjendana: {ukupno}")

# b) Koliko ima JEDINSTVENIH rođendana?  Savjet: set()
jedinstveni = set(rodjendani)
jedinstveni_ukupno = len(jedinstveni)
print(f"Jedinstvenih rodjendana rodjendana: {jedinstveni_ukupno}")


# c) Postoje li duplikati? Ispiši True/False.
print("Postoje li duplikati: ", ukupno != jedinstveni_ukupno)


# d) Pomoću rječnika (ili Counter-a) prebroj koliko se puta
brojac = {}
for datum in rodjendani:
    brojac[datum] = brojac.get(datum, 0) + 1

for datum, broj in brojac.items():
    if broj > 1:
        print(datum, "->", broj, "puta")


# e) BONUS: Koliko je studenata rođeno u martu (mjesec "03")?
#    Savjet: datum[:2] daje mjesec
u_martu = 0
for datum in rodjendani:
    if datum[:2] == "03-":
        u_martu += 1
print("Rodjeno u martu: ", u_martu)