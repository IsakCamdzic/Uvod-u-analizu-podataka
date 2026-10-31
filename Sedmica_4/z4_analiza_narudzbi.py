# =============================================================
# ZADATAK 4: Mini projekat - analiza narudžbi dostave hrane
# Uvod u analizu podataka - Vježbe, Sedmica 4
# =============================================================
# narudzbe.csv: 600 narudžbi, kolone:
#   id, datum_vrijeme, grad, kategorija, iznos, ocjena
# Pazi: podaci su "prljavi" - neki iznosi i datumi nisu ispravni!
#
# a) Učitaj fajl, ispiši kolone (print(df.columns)) i dimenzije.
#       očekivano: (600, 6)
#
# b) Očisti podatke:
#       - iznos u broj:   pd.to_numeric(..., errors="coerce")
#       - datum u datum:  pd.to_datetime(..., errors="coerce")
#       - ispiši koliko je neispravnih iznosa (6) i datuma (4)
#       - izbaci te redove: dropna(subset=[...])  -> očekivano: (590, 6)
#
# c) Napravi izvedene kolone iz datuma:
#       "sat"    = .dt.hour
#       "dan"    = .dt.dayofweek pretvoren u naziv (lista DANI ispod)
#       "mjesec" = .dt.month
#
# d) Top 5 gradova po broju narudžbi (value_counts) + bar chart,
#    sačuvaj kao "z4_gradovi.png".
#       očekivano: Sarajevo 210, Tuzla 91, Banja Luka 78, Mostar 68, Zenica 61
#
# e) Broj narudžbi po satu (value_counts().sort_index()) + bar chart,
#    sačuvaj kao "z4_sati.png". U koji sat je najviše narudžbi?
#       očekivano: 19 h (69), odmah iza 18 h (68)
#
# f) Prosječan iznos po kategoriji, sortirano opadajuće (groupby).
#       očekivano: Sushi 44.30, Pizza 21.93, Burger 15.70,
#                  Ćevapi 13.88, Salata 12.05, Desert 9.08
#
# BONUS:  - broj narudžbi po danu u sedmici (koji dan je najjači?)
#         - ukupan promet (10643.64 KM) i prosječna narudžba (18.04 KM)
# BONUS 2: sažetak u "izvjestaj_narudzbe.xlsx" sa sheetovima
#          "Gradovi", "Kategorije", "Sati" (pd.ExcelWriter)
# =============================================================
import os
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER, "narudzbe.csv")
DANI = ["Pon", "Uto", "Sri", "Čet", "Pet", "Sub", "Ned"]   # 0 = ponedjeljak

# a) TODO: učitaj i pogledaj kolone
df = pd.read_csv(FAJL)
print(df.columns)
print("Dimenzije: ", df.shape)

# b) TODO: čišćenje
#       - iznos u broj:   pd.to_numeric(..., errors="coerce")
#       - datum u datum:  pd.to_datetime(..., errors="coerce")
#       - ispiši koliko je neispravnih iznosa (6) i datuma (4)
#       - izbaci te redove: dropna(subset=[...])  -> očekivano: (590, 6)
df["iznos"] = pd.to_numeric(df["iznos"], errors="coerce")
df["datum_vrijeme"] = pd.to_datetime(df["datum_vrijeme"], errors="coerce")
print(df.isnull().sum())
df = df.dropna(subset=["iznos", "datum_vrijeme"]).copy()
print("Nakon ciscenja: ", df.shape)

# c) TODO: izvedene kolone sat, dan, mjesec
df["sat"] = df["datum_vrijeme"].dt.hour
df["mjesec"] = df["datum_vrijeme"].dt.month
df["dan"] = df["datum_vrijeme"].dt.day_of_week

# d) TODO: top 5 gradova + grafikon
po_gradu = df["grad"].value_counts().sort_index()
print("\nNarudzbe po gradu:")
print(po_gradu)
po_gradu.plot(kind="bar", color="red")
plt.xlabel("Grad")
plt.ylabel("Narudzbe po gradu")
plt.savefig("z4_grafikon.png")
print("\nNarudzbe po gradu:")

# e) TODO: narudžbe po satu + grafikon
po_satu = df["sat"].value_counts().sort_index()
plt.title("Narudžbe po satu u danu")
plt.xlabel("Sat")
plt.ylabel("Broj narudžbi")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)
plt.savefig("z4_grafikon2.png")

# f) TODO: prosječan iznos po kategoriji
po_kategoriji = (
    df.groupby("kategorija")["iznos"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nProsječan iznos po kategoriji:")
print(po_kategoriji)

# BONUS: TODO

print("Zadatak 4 - dopuni TODO dijelove.")
