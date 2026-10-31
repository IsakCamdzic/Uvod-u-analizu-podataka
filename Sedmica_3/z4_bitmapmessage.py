# =============================================================
# ZADATAK 3: Bitmap Message - istraži i nadogradi program
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
# a) Odgovori na pitanja (upiši odgovor kao komentar ispod pitanja).
#    Eksperimentiši: promijeni kod, pokreni, pogledaj šta se desi.
#
#    1. Šta se dešava ako korisnik unese prazan niz za poruku?
#       Odgovor:
#
#    2. Da li je važno koji su znakovi (koji nisu razmak) u bitmapi?
#       Odgovor: TODO
#
#    3. Šta predstavlja varijabla i u petlji "for i, bit in enumerate(red)"?
#       Odgovor: TODO
#
#    4. Šta se desi ako obrišeš (ili zakomentarišeš) print() na kraju
#       vanjske petlje (onaj koji prelazi u novi red)?
#       Odgovor: TODO
#
# b) Napravi vlastitu bitmapu (npr. srce) u varijabli BITMAPA_SRCE.
#    Koristi * za "puno" polje i razmak za "prazno".
#
# c) Nadogradi program:
#    - funkcija prikazi() treba da podrži obrnuti prikaz (obrnuto=True):
#      slova poruke na mjestu RAZMAKA, a razmak na mjestu znakova
#    - pitaj korisnika: koju bitmapu želi (1 = karta svijeta, 2 = srce)
#    - pitaj: obrnuti prikaz? (d/n)
#    - pitaj: velikim slovima? (d/n)  -> poruka.upper()
# =============================================================
import sys

# (!) Try changing this multiline string to any image you like:
# There are 68 periods along the top and bottom of this string:

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

# b) TODO: nacrtaj srce
BITMAPA_SRCE = """
"""


def prikazi(bitmapa, poruka, obrnuto=False):
    """Ispisuje bitmapu popunjenu slovima poruke."""
    # c) TODO: kad je obrnuto=True, zamijeni ulogu razmaka i znakova
    for red in bitmapa.splitlines():
        for i, znak in enumerate(red):
            if znak == ' ':
                print(' ', end='')
            else:
                print(poruka[i % len(poruka)], end='')
        print()


# --- Glavni program -----------------------------------------
print('Unesi poruku koja će se prikazati u bitmapi.')
poruka = input('> ')
if poruka == '':
    sys.exit()

# c) TODO: pitaj za bitmapu (1/2), obrnuti prikaz (d/n) i velika slova (d/n)

prikazi(bitmap, poruka)
