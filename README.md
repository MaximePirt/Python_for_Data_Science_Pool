# Python for Data Science Pool

Piscine 42 « Python for Data Science » : une semaine d'exercices Python, du cœur du langage jusqu'aux bibliothèques de calcul scientifique et de data science (NumPy, Pandas, Matplotlib). Chaque jour (`Day0` à `Day04`) est un dossier contenant plusieurs exercices (`exXX`), chacun indépendant avec son propre script et parfois un `tester.py`.

## Day0 — Bases de Python
- `ex00` : manipulation des structures de base (`list`, `tuple`, `set`, `dict`) et de leur mutabilité.
- `ex01` : calcul et formatage de dates/durées avec `datetime`.
- `ex02` / `ex03` : reconnaissance de types via le pattern matching (`match`/`case`), y compris les cas particuliers (`None`, `NaN`, chaîne vide...).
- `ex04` : lecture d'arguments CLI (`sys.argv`) et détection pair/impair.
- `ex05` : comptage de caractères (majuscules, minuscules, ponctuation, espaces, chiffres) dans une chaîne.
- `ex06` : réimplémentation de `filter()` avec une liste en compréhension, et script de filtrage de chaînes par longueur.
- `ex07` : conversion de texte en morse.
- `ex08` : barre de progression animée dans le terminal.
- `ex09` : création et packaging d'un module Python (`ft_package`) installable via `pip`/`setup.py`.

## Day01 — NumPy
- `ex00` : calcul vectorisé de l'IMC à partir de listes de tailles/poids.
- `ex01` : slicing d'un tableau 2D NumPy.
- `ex02` : chargement d'une image en tableau NumPy (`PIL` + `numpy`).
- `ex03` : recadrage et passage en niveaux de gris d'une image.
- `ex04` : rotation manuelle d'une image (parcours de tableau).
- `ex05` : transformations de couleur sur une image (inversion, teintes rouge...).

## Day02 — Pandas & visualisation
- `ex00` : chargement et validation d'un fichier CSV en `DataFrame`.
- `ex01` : extraction et affichage de l'espérance de vie d'un pays au fil du temps (Matplotlib).
- `ex02` : conversion de valeurs de population (notations `k`/`M`) et tracé de leur évolution.
- `ex03` : croisement de deux jeux de données (PIB par habitant et espérance de vie) sur un nuage de points.

## Day03 — Programmation orientée objet
- `ex00` : classes abstraites (`ABC`) et héritage simple (univers Game of Thrones).
- `ex01` : héritage multiple et représentation d'objets (`__str__`/`__repr__`).
- `ex02` : héritage en diamant et résolution de méthode (MRO) via `super()`.
- `ex03` : surcharge d'opérateurs (`__add__`, `__sub__`, `__mul__`, `__truediv__`) sur une classe `calculator`.
- `ex04` : méthodes statiques de calcul vectoriel (produit scalaire, somme, différence).

## Day04 — Fonctions avancées & structures de données
- `ex00` : calcul de statistiques (moyenne, médiane, écart-type, variance) sans bibliothèque externe.
- `ex01` : fonctions d'ordre supérieur et fermetures (closures).
- `ex02` : décorateur limitant le nombre d'appels d'une fonction.
- `ex03` : génération d'objets `Student` via `dataclass` (identifiant et login générés automatiquement).

## Environnement
Un environnement virtuel (`.venv`, Python 3.10) est utilisé avec : `numpy`, `pandas`, `matplotlib`, `scipy`, `Pillow`, ainsi que `flake8`/`autopep8` pour le linting.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install numpy pandas matplotlib scipy Pillow flake8 autopep8
```

Chaque exercice se lance indépendamment, par exemple :
```sh
python Day02/ex01/aff_life.py
```
