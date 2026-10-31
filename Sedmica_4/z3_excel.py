# =============================================================
# ZADATAK 3: Excel - spajanje sheetova, obrada i export
# Uvod u analizu podataka - Vježbe, Sedmica 4
# =============================================================
# studenti.xlsx ima dva sheeta: "Grupa_A" i "Grupa_B" (po 20 studenata).
# Instalacija (ako već nije): pip install pandas openpyxl
#
# a) Učitaj oba sheeta u dva DataFrame-a.  Savjet: sheet_name="Grupa_A"
#
# b) Svakom dodaj kolonu "grupa" sa vrijednošću "A", odnosno "B".
#
# c) Spoji ih u jedan DataFrame.  Savjet: pd.concat([...], ignore_index=True)
#       očekivano: (40, 8)
#
# d) Dodaj kolone:
#       "prosjek" = (matematika + programiranje + statistika) / 3, zaokruženo na 2
#       "polozio" = True ako su sve tri ocjene >= 6
#       očekivano: (40, 10), položilo 25
#
# e) Spremi u "rezultati.xlsx" sa DVA sheeta:
#       "Svi"      - svih 40 studenata
#       "Polozili" - samo oni koji su položili (25)
#    Savjet:
#       with pd.ExcelWriter(putanja) as pisac:
#           df.to_excel(pisac, sheet_name="Svi", index=False)
#
# f) Pretvori sheet "Svi" iz rezultati.xlsx u "rezultati.csv" (index=False),
#    pa ga učitaj nazad i ispiši shape.  očekivano: (40, 10)
# =============================================================
import os
from Tools.scripts.var_access_benchmark import B

import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
EXCEL = os.path.join(FOLDER, "studenti.xlsx")
IZLAZ_XLSX = os.path.join(FOLDER, "rezultati.xlsx")
IZLAZ_CSV = os.path.join(FOLDER, "rezultati.csv")

# a) TODO: učitaj Grupa_A i Grupa_B
grupa_a = pd.read_excel(EXCEL, sheet_name="Grupa_A")
grupa_b = pd.read_excel(EXCEL, sheet_name="Grupa_B")


# b) TODO: kolona "grupa"
grupa_a["grupa"] = "A"
grupa_b["grupa"] = "B"

svi_sheet = pd.read_excel(EXCEL, sheet_name=None)

# c) TODO: concat
svi = pd.concat([grupa_a, grupa_b], ignore_index=True)
print("Nakon concat:", svi.shape)

# d) TODO: prosjek i polozio
#       "prosjek" = (matematika + programiranje + statistika) / 3, zaokruženo na 2
#       "polozio" = True ako su sve tri ocjene >= 6
#       očekivano: (40, 10), položilo 25
svi["prosjek"] = ((svi["matematika"] + svi["programiranje"] + svi["statistika"]) / 3).round(2)
svi["polozio"] = (svi["matematika"] >= 6) & (svi["programiranje"] >= 6) & (svi["statistika"] >= 6)# e)
print("Broj položenih:", svi["polozio"].sum())

# TODO: ExcelWriter sa dva sheeta
polozili = svi[svi["polozio"]].copy()

with pd.ExcelWriter(IZLAZ_XLSX) as pisac:
    svi.to_excel(pisac, sheet_name="Svi", index=False)
    polozili.to_excel(pisac, sheet_name="Polozili", index=False)

# f) TODO: Excel -> CSV i provjera
svi_ucitani = pd.read_excel(IZLAZ_XLSX, sheet_name="Svi")
svi_ucitani.to_csv(IZLAZ_CSV, index=False)

df_csv = pd.read_csv(IZLAZ_CSV)
print("Shape iz CSV:", df_csv.shape)

