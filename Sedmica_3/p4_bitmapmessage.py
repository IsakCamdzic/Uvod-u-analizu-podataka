# =============================================================
# PRIMJER 4: Bitmap Message (Laboratorijske vježbe 3)
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
# Program koristi višelinijski string kao "bitmapu" (2D sliku sa
# samo dvije boje). Na mjestu razmaka ispisuje razmak, a na mjestu
# svakog drugog znaka ispisuje slovo iz korisnikove poruke.
# Rezultat: karta svijeta "nacrtana" tvojom porukom.
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

print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()          # prazna poruka -> program se završava

# Loop over each line in the bitmap:
# splitlines() rastavi višelinijski string na listu redova
for line in bitmap.splitlines():
    # Loop over each character in the line:
    # enumerate daje i = pozicija (kolona) znaka u redu, bit = sam znak
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            # i % len(message) se "vrti u krug": 0, 1, ..., len-1, 0, 1, ...
            # pa se poruka ponavlja dok red ne završi
            print(message[i % len(message)], end='')
      # Print a newline.
    print()