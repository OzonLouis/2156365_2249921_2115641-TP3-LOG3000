# Calculatrice Web Simple - LOG3000

## Informations Générales

| Information | Détail |
| :--- | :--- |
| **Nom du Projet** | Calculatrice Web Simple |
| **Numéro d'Équipe** | 70 |
| **Cours** | Génie Logiciel (LOG3000) |
| **Langue** | Python, HTML, CSS, JavaScript |
| **Framework** | Flask |

---

## Objectif et Portée

### Description du Projet
Ce projet est une **application web de calculatrice simple** construite avec **Flask (Python)**. L'application permet aux utilisateurs de réaliser des opérations arithmétiques basiques (addition, soustraction, multiplication, division) via une interface web intuitive.

### Objectif Principal
L'objectif principal est de transformer une base de code initiale désordonnée et peu fiable en un produit **stable, documenté et testé**. Le projet met en œuvre :

- Pratiques rigoureuses de gestion de versions (Git workflow)
- Documentation complète (code et utilisateur)
- Suite de tests complète (tests unitaires et d'intégration)
- Pipeline structuré de correction de bogues
- Standards de qualité logicielle

### Portée
- **Logique métier** : Opérations arithmétiques de base
- **Interface** : Interface web responsive avec Flask
- **Tests** : Coverage complet des fonctionnalités critiques
- **Gestion du code** : Workflow Git avec branches et pull requests

---

## Structure du Projet

```
TP3---LOG3000-main/
├── app.py                 # Point d'entrée Flask et gestion des routes
├── operators.py           # Logique des opérations arithmétiques
├── templates/
│   └── index.html         # Interface utilisateur (HTML)
├── static/
│   └── style.css          # Styles et design (CSS)
├── tests/
│   ├── test_operators.py  # Tests unitaires des opérateurs
│   └── test_calculate.py  # Tests de la fonction calculate()
├── .gitignore             # Fichiers à ignorer par Git
└── README.md              # Documentation du projet
```

---

## Installation et Configuration

### Prérequis
Assurez-vous d'avoir installé sur votre machine :

- **Python 3.8+**
- **pip** (gestionnaire de paquets Python)
- **Git**
- **Navigateur web moderne**

### Guide d'Installation (Étape par Étape)

#### 1. Cloner le Dépôt
```bash
git clone <URL_DU_DEPOT>
cd TP3---LOG3000-main
```

#### 2. Créer un Environnement Virtuel
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Installer les Dépendances
```bash
pip install -r requirements.txt
```

Ou installer manuellement :
```bash
pip install flask pytest
```
---

## Utilisation

### Lancer l'Application

1. **Assurez-vous que l'environnement virtuel est activé :**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Démarrez le serveur Flask :**
   ```bash
   python app.py
   ```

3. **Ouvrez votre navigateur web** et allez à :
   ```
   http://127.0.0.1:5000
   ```

### Guide d'Utilisation de la Calculatrice

#### Opérations Disponibles
- Addition : Appuyez sur `+` entre deux nombres
- Soustraction : Appuyez sur `-` entre deux nombres
- Multiplication : Appuyez sur `*` entre deux nombres
- Division : Appuyez sur `/` entre deux nombres

#### Étapes d'Utilisation
1. **Entrer une expression** : Utilisez les boutons de la calculatrice pour entrer une expression (ex. `10 + 5`)
2. **Valider l'opération** : Appuyez sur le bouton `=` pour calculer le résultat
3. **Voir le résultat** : Le résultat s'affiche sur l'écran de la calculatrice
4. **Effacer l'écran** : Appuyez sur `C` pour réinitialiser

#### Exemples d'Opérations
| Opération | Résultat |
| :--- | :--- |
| `10 + 5` | `15` |
| `10 - 4` | `6` |
| `6 * 7` | `42` |
| `7 / 2` | `3.5` |

#### Gestion des Erreurs
- Si vous entrez une **expression invalide** (ex. `5 +`), un **message d'erreur** s'affichera
- Les **expressions vides** sont rejetées avec un message approprié
- **Une seule opération** par expression (ex. `5 + 3 * 2` n'est pas autorisé)

---

## Tests

### Exécuter les Tests

#### Tous les Tests
```bash
python -m pytest
```

#### Tests Verbeux (Affiche les détails)
```bash
python -m pytest -v
```

### Couverture des Tests

La suite de tests couvre :

| Catégorie | Tests |
| :--- | :--- |
| **Opérateurs** | `add()`, `subtract()`, `multiply()`, `divide()` |
| **Fonction calculate()** | Expressions valides, expressions invalides, format d'erreur |
| **Intégration** | Validation complète du pipeline calculate → opérateurs |
| **Cas limites** | Division par zéro, expressions malformées, opérateurs multiples |

### Résultats Attendus
Tous les tests doivent **passer** (PASSED) pour que le code soit considéré comme stable.

---

## Flux de Contribution

### Workflow de Gestion des Branches

#### 1. Structure des Branches

```
main (branche stable)
├── fix/1-subtraction-inverted
├── fix/2-multiplication-exponentiation
├── fix/3-ui-button-labels
└── fix/4-division-floor-division
```

**Conventions de nommage :**
- `main` : Version stable et testée
- `fix/{numéro-issue}-{description}` : Correction de bogue
- `feature/{description}` : Nouvelles fonctionnalités
- `docs/{description}` : Documentation

#### 2. Processus de Correction de Bogue

##### Étape 1 : Créer une Issue
```markdown
**Titre :** [BUG] Description du problème

**Description :**
- Problème : Description claire du bogue
- Étapes à reproduire : 1. ... 2. ... 3. ...
- Résultat attendu : Comportement correct
- Résultat actuel : Comportement incorrect
```

##### Étape 2 : Créer une Branche
```bash
git checkout main
git pull origin main
git checkout -b fix/{numéro-issue}-{description}
```

Exemple :
```bash
git checkout -b fix/1-subtraction-inverted
```

##### Étape 3 : Corriger le Bogue
- Modifiez le code concerné
- Testez le fix localement

##### Étape 4 : Valider les Changements
```bash
git add <fichiers-modifiés>
git commit -m "Fix #{numéro}: {description courte}"
```

Exemple :
```bash
git commit -m "Fix #1: Correct subtract() to return a - b instead of b - a"
```

##### Étape 5 : Pousser la Branche
```bash
git push -u origin fix/{numéro-issue}-{description}
```

##### Étape 6 : Ouvrir une Pull Request
```markdown
**Titre :** Fix #1: Correct subtraction operator inverted result

**Description :**
Changed subtract() to return a - b instead of b - a.

## Tests
- test_calculate_subtraction
- test_subtract

## Changes
- Modified `operators.py`: Fixed subtract function
```

##### Étape 7 : Révision et Fusion
1. Attendez la **révision du code**
2. Répondez aux **commentaires**
3. Une fois **approuvée**, fusionnez la branche avec `main`
4. **Supprimez** la branche après fusion

```bash
git checkout main
git pull origin main
git branch -d fix/1-subtraction-inverted
```

#### 3. Réexécution des Tests

Après chaque fusion sur `main` :
```bash
git checkout main
python -m pytest -v
```

**Critères de succès :**
- Tous les tests pass
- Aucun avertissement de linter
- Documentation à jour
- Code bien formaté

## État du Projet

### Couverture des Tests
- Opérateurs : 100% des cas couverts
- Fonction calculate() : 100% des chemins testés
- Interface : Validation visuelle complètement

---

## Support et Questions

Pour toute question ou problème :
1. Consultez la **documentation du code**
2. Vérifiez les **issues existantes**
3. Ouvrez une **nouvelle issue** avec les détails

---

