# =============================================================
# PRIMJER 4: Prljavi podaci, datumi i prvi pandas grafikon
# Uvod u analizu podataka - Vježbe, Sedmica 4
# =============================================================
# narudzbe.csv: 600 narudžbi dostave hrane (septembar-oktobar 2026).
# Kolone: id, datum_vrijeme, grad, kategorija, iznos, ocjena
# Pitanje: U koje doba dana se najviše naručuje?
#
# Instalacija: pip install pandas matplotlib
# =============================================================
import os
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(FOLDER, "narudzbe.csv"))

# --- 1. UVIJEK prvo pogledaj kolone --------------------------
print(df.columns)
print("Dimenzije:", df.shape)

# --- 2. Greška koju svi naprave: kolona koja ne postoji ------
try:
    print(df["sat"])
except KeyError:
    print("\nKeyError: kolona 'sat' ne postoji! Imamo samo 'datum_vrijeme'.")
    print("Sat moramo IZVESTI iz datuma.")

# --- 3. Čišćenje: pretvaranje tipova sa errors="coerce" ------
# Neispravne vrijednosti ("n/a", "greška", "nepoznato") postaju NaN
# (Not a Number = nedostajuća vrijednost) umjesto da program pukne.
df["iznos"] = pd.to_numeric(df["iznos"], errors="coerce")
df["datum_vrijeme"] = pd.to_datetime(df["datum_vrijeme"], errors="coerce")

print("\nNedostajuće vrijednosti po kolonama:")
print(df.isna().sum())

# Izbaci redove gdje fali iznos ili datum
df = df.dropna(subset=["iznos", "datum_vrijeme"]).copy()
print("Nakon čišćenja:", df.shape)       # (590, 6)

# --- 4. Izvedene kolone iz datuma: .dt -----------------------
df["sat"] = df["datum_vrijeme"].dt.hour
df["mjesec"] = df["datum_vrijeme"].dt.month
df["dan"] = df["datum_vrijeme"].dt.dayofweek   # 0 = ponedjeljak, 6 = nedjelja
print("\nPrva 3 reda sa novim kolonama:")
print(df[["datum_vrijeme", "sat", "mjesec", "dan"]].head(3))

# --- 5. Brojanje: value_counts + sort_index ------------------
po_satu = df["sat"].value_counts().sort_index()   # sortiraj po satu, ne po broju
print("\nNarudžbe po satu:")
print(po_satu)

# --- 6. Grafikon direktno iz pandasa -------------------------
po_satu.plot(kind="bar", color="#3A7CA5", figsize=(10, 5))
plt.title("Narudžbe po satu u danu")
plt.xlabel("Sat")
plt.ylabel("Broj narudžbi")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)

SLIKA = os.path.join(FOLDER, "p4_grafikon.png")
plt.savefig(SLIKA, dpi=120, bbox_inches="tight")
print("\nGrafikon sačuvan kao:", SLIKA)
plt.show()
