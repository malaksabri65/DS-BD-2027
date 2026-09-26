"""
Qu'est-ce qui freine la croissance au Maroc ? (2015-2025)
============================================================
Ce script :
  1. Importe les données du dossier ../data/ (croissance annuelle du PIB avec
     décomposition agricole/non agricole, et efficacité de l'investissement),
     issues des notes du Haut-Commissariat au Plan (HCP).
  2. Calcule quelques indicateurs simples (volatilité comparée de l'agriculture
     et du non-agricole, dégradation de l'ICOR).
  3. Génère deux graphiques enregistrés dans ../figures/ :
       - croissance_pib_vs_secteurs.png : croissance du PIB total vs.
         valeur ajoutée agricole vs. valeur ajoutée non agricole, 2015-2025.
       - investissement_icor.png : taux d'investissement, croissance moyenne et
         ICOR par période (2000-2009, 2010-2019, 2010-2023).

Usage :
    python3 analyse_croissance.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. Chargement des données
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
FIG_DIR = os.path.join(BASE_DIR, "..", "figures")
os.makedirs(FIG_DIR, exist_ok=True)

croissance = pd.read_csv(os.path.join(DATA_DIR, "croissance_pib_annuelle.csv"))
icor = pd.read_csv(os.path.join(DATA_DIR, "investissement_icor.csv"))

# ---------------------------------------------------------------------------
# 2. Quelques indicateurs rapides
# ---------------------------------------------------------------------------
print("=" * 70)
print("APERCU DES DONNEES : CROISSANCE DU PIB (HCP)")
print("=" * 70)
print(croissance)

vol_agricole = croissance.croissance_agricole_pct.std()
vol_non_agricole = croissance.croissance_non_agricole_pct.std()
print(f"\nÉcart-type de la croissance agricole (2016-2025)   : {vol_agricole:.1f} points")
print(f"Écart-type de la croissance non agricole (2018-2025): {vol_non_agricole:.1f} points")
print(f"-> L'agriculture est environ {vol_agricole / vol_non_agricole:.1f}x plus volatile "
      f"que le reste de l'économie")

moy_non_agricole = croissance.croissance_non_agricole_pct.mean()
print(f"\nCroissance non agricole moyenne (2018-2025) : {moy_non_agricole:.1f} %"
      f" (nettement sous l'objectif de 6 % du Nouveau Modèle de Développement)")

hausse_icor = icor.loc[icor.periode == "2010-2023", "icor"].values[0] - \
              icor.loc[icor.periode == "2000-2009", "icor"].values[0]
print(f"\nDégradation de l'ICOR entre 2000-2009 et 2010-2023 : +{hausse_icor:.1f} points "
      f"(un ICOR plus élevé = un investissement moins efficace)")

# ---------------------------------------------------------------------------
# 3. Graphique 1 : croissance du PIB vs agriculture vs non-agricole
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(croissance.annee, croissance.croissance_pib_pct, marker="o", linewidth=2.5,
        color="#c1272d", label="PIB total")
ax.plot(croissance.annee, croissance.croissance_agricole_pct, marker="o", linewidth=1.5,
        linestyle="--", color="#4a8f4a", label="Valeur ajoutée agricole")
ax.plot(croissance.annee, croissance.croissance_non_agricole_pct, marker="o", linewidth=1.5,
        color="#2c6e91", label="Valeur ajoutée non agricole")

ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(2020, color="grey", linestyle=":", linewidth=1)
ax.text(2020.1, 18, "Covid-19", fontsize=9, color="grey")

ax.set_title("Croissance du PIB marocain : le grand écart\nagriculture vs reste de l'économie, 2015-2025",
              fontsize=13, weight="bold")
ax.set_xlabel("Année")
ax.set_ylabel("Croissance annuelle (%)")
ax.legend(loc="upper left")
ax.grid(axis="y", alpha=0.3)

fig.tight_layout()
fig.savefig(os.path.join(FIG_DIR, "croissance_pib_vs_secteurs.png"), dpi=150)
print(f"\nGraphique enregistré : {os.path.join(FIG_DIR, 'croissance_pib_vs_secteurs.png')}")

# ---------------------------------------------------------------------------
# 4. Graphique 2 : taux d'investissement, croissance et ICOR par période
# ---------------------------------------------------------------------------
fig2, ax1 = plt.subplots(figsize=(9, 6))

x = range(len(icor))
width = 0.35
ax1.bar([i - width / 2 for i in x], icor.taux_investissement_moyen_pib_pct, width,
        color="#2c6e91", label="Taux d'investissement moyen (% du PIB)")
ax1.bar([i + width / 2 for i in x], icor.croissance_moyenne_pib_pct, width,
        color="#4a8f4a", label="Croissance moyenne du PIB (%)")
ax1.set_xticks(list(x))
ax1.set_xticklabels(icor.periode)
ax1.set_ylabel("%")
ax1.set_ylim(0, 35)

ax2 = ax1.twinx()
ax2.plot(x, icor.icor, marker="o", linewidth=2.5, color="#c1272d", label="ICOR (échelle droite)")
ax2.set_ylabel("ICOR (points de capital / point de croissance)")
ax2.set_ylim(0, 14)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9)

ax1.set_title("Un investissement stable, une croissance en baisse :\nl'efficacité du capital se dégrade",
              fontsize=13, weight="bold")

fig2.tight_layout()
fig2.savefig(os.path.join(FIG_DIR, "investissement_icor.png"), dpi=150)
print(f"Graphique enregistré : {os.path.join(FIG_DIR, 'investissement_icor.png')}")

plt.close("all")
print("\nTerminé.")
