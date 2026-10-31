# =============================================================
# PRIMJER 2: Uvod u pandas
# Uvod u analizu podataka - Vježbe, Sedmica 4
# =============================================================
# Instalacija: pip install pandas
#   (u PyCharmu: Settings → Python Interpreter → + → pandas → Install)
#
# pandas je biblioteka za rad s tabelarnim podacima - kao Excel
# u Pythonu. Glavna struktura je DataFrame: tabela sa redovima
# (indeks 0, 1, 2, ...) i kolonama (imena kolona).
# =============================================================
import os
import pandas as pd

# Prikaži sve kolone u ispisu (bez "..." u sredini)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
FAJL = os.path.join(FOLDER, "studenti.csv")

# --- 1. Učitavanje: jedna linija! ----------------------------
df = pd.read_csv(FAJL)

# --- 2. Prvi pogled na podatke -------------------------------
print("Prva 3 reda:")
print(df.head(3))              # head() bez broja = prvih 5 redova

print("\nZadnja 2 reda:")
print(df.tail(2))

print("\nDimenzije (redovi, kolone):", df.shape)
print("Kolone:", list(df.columns))
print("\nTipovi kolona:")
print(df.dtypes)               # pandas SAM prepozna da su ocjene brojevi

# --- 3. Statistički sažetak ----------------------------------
print("\nStatistički sažetak (describe):")
print(df.describe().round(2))  # count, mean, std, min, 25%, 50%, 75%, max

# --- 4. Biranje kolona ---------------------------------------
print("\nJedna kolona (Series):")
print(df["ime"].head(3))

print("\nViše kolona (DataFrame) - dvostruke uglaste zagrade:")
print(df[["ime", "smjer"]].head(3))

# --- 5. Izračunata kolona (kao formula u Excelu) -------------
df["prosjek"] = (df["matematika"] + df["programiranje"] + df["statistika"]) / 3
print("\nNova kolona prosjek:")
print(df[["ime", "prosjek"]].head(3).round(2))

# --- 6. Sortiranje: sort_values ------------------------------
print("\nTop 5 po prosjeku:")
top5 = df.sort_values("prosjek", ascending=False, kind="stable").head(5)
print(top5[["ime", "smjer", "prosjek"]].round(2))

# --- 7. Filtriranje: uslov u uglastim zagradama --------------
slabo_prisustvo = df[df["prisustvo"] < 70]
print("\nStudenti sa prisustvom ispod 70%:", len(slabo_prisustvo))
print(slabo_prisustvo[["ime", "prisustvo"]])

# --- 8. Brojanje kategorija: value_counts --------------------
print("\nBroj studenata po smjeru:")
print(df["smjer"].value_counts())

# --- 9. Grupisanje: groupby ----------------------------------
print("\nProsjek po smjeru:")
print(df.groupby("smjer")["prosjek"].mean().round(2).sort_values(ascending=False))

# --- 10. Pojedinačne statistike ------------------------------
print("\nProsjek prisustva:", round(df["prisustvo"].mean(), 2))
print(f"Najmanji prosjek: {df['prosjek'].min():.2f}")
print(f"Najveći prosjek: {df['prosjek'].max():.2f}")
print("Zbir svih ocjena iz matematike:", df["matematika"].sum())
