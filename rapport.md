# Qu'est-ce qui freine la croissance au Maroc ?

*Analyse quantitative à partir des données du Haut-Commissariat au Plan (HCP), 2015-2025*

---

## 1. Le constat chiffré : une croissance faible, très volatile, et mal répartie

| Année | Croissance PIB | dont agricole | dont non agricole |
|-------|:---:|:---:|:---:|
| 2015 | 4,5 % | – | – |
| 2016 | 1,1 % | -13,7 % | – |
| 2017 | 4,1 % | +15,4 % | – |
| 2018 | 3,1 % | +3,7 % | +2,9 % |
| 2019 | 2,5 % | -5,8 % | +3,8 % |
| 2020 | -7,2 % | -8,1 % | -6,9 % |
| 2021 | 8,0 % | +19,5 % | +6,3 % |
| 2022 | 1,3 % | -12,9 % | +3,0 % |
| 2023 | 3,7 % | +1,5 % | +3,7 % |
| 2024 | 4,4 % | -5,7 % | +5,1 % |
| 2025 | 4,9 % | +8,2 % | +3,9 % |

*Source : notes HCP "Situation économique nationale" (voir `data/sources.md`).*

Sur onze ans, la croissance moyenne du PIB marocain ressort à environ **2,9 %**, très en
deçà de l'objectif de 6 % fixé par le Nouveau Modèle de Développement (NMD) marocain.
Deux constats ressortent immédiatement des chiffres officiels :

1. La croissance est **extrêmement volatile d'une année sur l'autre** (de -7,2 % en 2020 à
   +8,0 % en 2021), un profil bien plus heurté que celui de la plupart des économies
   émergentes comparables.
2. Même en écartant les années "accidentées" (Covid, sécheresses), la **partie non
   agricole de l'économie ne progresse en moyenne que d'environ 2,7 % par an** — loin,
   elle aussi, de l'objectif de 6 %.

![Croissance du PIB vs agriculture vs non-agricole](figures/croissance_pib_vs_secteurs.png)

---

## 2. Trois freins structurels identifiés dans les données

### 2.1 Une dépendance excessive à une agriculture pluviale et volatile

Le graphique ci-dessus est sans appel : la valeur ajoutée agricole oscille entre **-13,7 %
et +19,5 %** d'une année à l'autre, soit une volatilité (écart-type ≈ 11,5 points) **près
de 3 fois supérieure** à celle du reste de l'économie (écart-type ≈ 4,0 points). Chaque
sécheresse (2016, 2019, 2020, 2022, 2024) se traduit par une contraction brutale de la
valeur ajoutée agricole, qui tire mécaniquement la croissance nationale vers le bas —
et chaque bonne campagne céréalière (2017, 2021, 2025) produit l'effet inverse. D'après
la Direction générale du Trésor français, **la pluviométrie expliquerait à elle seule
près de 37 % de la variance du PIB marocain**, alors que l'agriculture ne représente que
12 % du PIB mais 30 % de l'emploi. Cette dépendance rend la trajectoire de croissance du
Maroc largement imprévisible et empêche toute programmation stable de l'investissement
et de l'emploi.

### 2.2 Une efficacité de l'investissement en dégradation constante (ICOR élevé et croissant)

Le Maroc n'est pourtant pas un pays qui sous-investit : au contraire, son taux
d'investissement (FBCF rapportée au PIB) compte parmi les plus élevés au monde, autour de
**30 % du PIB entre 2000 et 2019**. Le problème est que cet effort de capital ne se
traduit plus en croissance. Le HCP mesure ce phénomène à travers l'ICOR (*Incremental
Capital-Output Ratio* — le nombre de points d'investissement nécessaires pour produire un
point de croissance) :

- 2000-2009 : ICOR de **6,1** (investissement moyen ≈ 30 % du PIB, croissance moyenne 4,9 %)
- 2010-2023 : ICOR de **11,8** (investissement moyen 27,5 % du PIB, croissance moyenne 2,9 %)

**L'ICOR a donc quasiment doublé en une quinzaine d'années** : il faut aujourd'hui environ
deux fois plus de capital investi pour générer le même point de croissance qu'au début des
années 2000. Une explication centrale avancée par les économistes marocains est la
structure de cet investissement : au Maroc, il est réparti à parts quasi égales entre
secteur public et secteur privé (50 %/50 %), contre 85 % de part privée en Turquie par
exemple — un pays au taux d'investissement comparable (28 % du PIB) mais à une croissance
deux fois plus élevée (~6 %). Une prépondérance de l'investissement public, souvent
concentré dans de grandes infrastructures à rentabilité lente (autoroutes, ports, lignes à
grande vitesse), pénaliserait le rendement global du capital investi.

![Taux d'investissement, croissance et ICOR par période](figures/investissement_icor.png)

### 2.3 Un tissu économique encore largement informel, qui freine productivité et recettes fiscales

Selon la dernière enquête nationale du HCP, le secteur informel représentait **28,7 % des
emplois créés et 11 % du PIB**. D'autres études (Banque mondiale, Bank Al-Maghrib) donnent
des estimations plus larges du travail informel, en particulier en zone rurale où
l'agriculture emploie de manière informelle jusqu'à 90 % de sa main-d'œuvre. Quelle que
soit la mesure retenue, ce poids de l'informel pèse sur la croissance de plusieurs façons :
les entreprises informelles ont un accès limité au financement et à la technologie, ce qui
brime les gains de productivité ; l'État perçoit moins de recettes fiscales et sociales,
ce qui limite sa capacité à financer l'investissement public de façon plus productive ; et
les travailleurs informels, sans contrat ni protection sociale, restent dans des emplois
précaires à faible valeur ajoutée — un frein direct à la montée en gamme de l'économie.

---

## 3. Conclusion

Les trois mécanismes identifiés se renforcent mutuellement pour brider la croissance
marocaine. La **dépendance climatique de l'agriculture** rend le PIB extrêmement volatile
d'une année sur l'autre, ce qui décourage la planification des investissements privés.
La **baisse de l'efficacité du capital investi** (ICOR en forte hausse) signifie que même
un effort d'investissement soutenu — l'un des plus élevés au monde en proportion du PIB —
ne parvient plus à produire une croissance suffisante pour créer des emplois en nombre. Et
le **poids persistant de l'économie informelle** prive le pays d'une partie des gains de
productivité et des recettes fiscales qui permettraient de financer un investissement
public plus efficace et un meilleur capital humain. Ensemble, ces trois facteurs expliquent
pourquoi le Maroc, malgré des atouts réels (stabilité macroéconomique, diversification
sectorielle croissante, position géographique), reste loin de l'objectif de croissance de
6 % par an nécessaire pour résorber durablement le chômage 

---

## 4. Méthodologie et limites

- Toutes les données proviennent des notes officielles du HCP (voir `data/sources.md`
  pour le détail des liens).
- Le HCP publie des chiffres "provisoires" qui sont révisés l'année suivante lors de la
  publication des comptes nationaux de l'année en cours (par exemple, la croissance 2024
  a été révisée de 3,8 % à 4,4 % lors de la publication des comptes 2025). Les valeurs
  retenues dans ce rapport sont les plus récentes disponibles au moment de la rédaction,
  mais restent, pour 2025, encore provisoires.
- Les chiffres de croissance agricole/non agricole pour 2015-2017 n'ont pas pu être
  retrouvés de façon homogène avec la méthodologie utilisée pour les années suivantes et
  sont donc laissés vides plutôt qu'estimés.
- L'ICOR est un indicateur simplifié (rapport investissement/croissance) qui ne tient pas
  compte des délais de maturation des grands projets d'infrastructure ; sa hausse doit
  être interprétée comme un signal de dégradation tendancielle plutôt que comme une mesure
  exacte et instantanée de l'efficacité du capital.
- Les estimations du poids du secteur informel varient fortement selon les institutions et
  les définitions retenues (28,7 % des emplois selon le HCP, jusqu'à 77,3 % du travail
  selon une lecture large de la Banque mondiale incluant l'agriculture) : le chiffre HCP a
  été retenu comme référence officielle nationale, mais le rapport signale cette variabilité.

## 5. Contenu du dépôt

```
croissance_maroc/
├── data/
│   ├── croissance_pib_annuelle.csv   # croissance PIB, agricole, non agricole, 2015-2025
│   ├── investissement_icor.csv       # taux d'investissement, croissance, ICOR par période
│   └── sources.md                    # liens vers toutes les sources HCP utilisées
├── script/
│   └── analyse_croissance.py         # importe les CSV, calcule des indicateurs, génère les 2 graphiques
├── figures/
│   ├── croissance_pib_vs_secteurs.png
│   └── investissement_icor.png
└── rapport.md                       
```


