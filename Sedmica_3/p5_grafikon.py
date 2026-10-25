# =============================================================
# PRIMJER 5: Prvi grafikon u Pythonu (matplotlib)
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
# Instalacija: pip install matplotlib
#   (u PyCharmu: Settings → Python Interpreter → + → matplotlib → Install)
#
# Crtamo teorijsku vjerovatnoću da u grupi od n osoba bar dvoje
# imaju isti rođendan, za n = 1 ... 60.
# =============================================================
import os
from matplotlib import pyplot as plt


def vjerovatnoca_poklapanja(n):
    """Vjerovatnoća (u %) da u grupi od n osoba bar dvoje dijele rođendan."""
    niko_isti = 1.0
    for i in range(n):
        niko_isti = niko_isti * (365 - i) / 365
    return (1 - niko_isti) * 100


# --- Podaci za grafikon: x i y liste -------------------------
osobe = list(range(1, 61))                               # x osa: 1, 2, ..., 60
procenti = [vjerovatnoca_poklapanja(n) for n in osobe]   # y osa

# --- Linijski grafikon ---------------------------------------
plt.figure(figsize=(9, 5))
plt.plot(osobe, procenti, color="#3A7CA5", linewidth=2, label="Teorija")

# Horizontalna isprekidana linija na 50%
plt.axhline(50, color="gray", linestyle="--", linewidth=1)

# Istaknute tačke: 23 osobe i 38 osoba (naša grupa)
for n in [23, 38]:
    p = vjerovatnoca_poklapanja(n)
    plt.plot(n, p, marker="o", markersize=9, color="#F2A541")
    plt.annotate(f"{n} osoba: {p:.1f}%",
                 xy=(n, p),
                 xytext=(n + 2, p - 10),
                 arrowprops=dict(arrowstyle="->"))

# Naslov, oznake osa, mreža
plt.title("Birthday paradox: vjerovatnoća poklapanja")
plt.xlabel("Broj osoba u grupi")
plt.ylabel("Vjerovatnoća da bar dvoje dijele rođendan (%)")
plt.ylim(0, 100)
plt.grid(True, alpha=0.3)

# Sačuvaj sliku pored skripte, pa prikaži prozor sa grafikonom
SLIKA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p5_grafikon.png")
plt.savefig(SLIKA, dpi=120, bbox_inches="tight")
print("Grafikon sačuvan kao:", SLIKA)
plt.show()
