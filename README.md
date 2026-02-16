# Calculatrice Web Simple - LOG3000

## Informations Générales
* **Nom du Projet :** Calculatrice Web Simple
* **Numéro d'Équipe :** 70 
* **Cours :** Génie logiciel (LOG3000) 

---

## Objectif et Portée
Ce projet consiste en une application web de calculatrice simple construite avec la bibliothèque **Flask** de Python.

L'objectif principal de ce dépôt est de transformer une base de code initiale désordonnée et peu fiable en un produit stable, documenté et testé. Nous mettons en œuvre des pratiques rigoureuses de gestion de versions, incluant une documentation approfondie et un pipeline de correction de bogues structuré.

---

## Structure du Projet
[cite_start]Le projet est organisé de manière modulaire pour séparer la logique métier de l'interface utilisateur:

| Dossier/Fichier | Description |
| :--- | :--- |
| `app.py` | Point d'entrée du serveur Flask et gestion des routes. |
| `logic/` | Contient la logique mathématique de la calculatrice. |
| `templates/` | Fichiers HTML pour l'interface utilisateur. |
| `static/` | Fichiers CSS pour le style et le design. |
| `tests/` | Suite de tests unitaires et d'intégration. |

---

## Installation et Configuration

### Prérequis
Assurez-vous d'avoir les éléments suivants installés sur votre machine:
* **Python 3.x**
* **pip** (gestionnaire de paquets Python)
* **Git** 

### Guide d'installation (étape par étape)
1. **Cloner le dépôt :**
   ```bash
   git clone [URL_DE_TON_DEPOT_GITLAB]
   cd [NOM_DU_DOSSIER]
   ```
2. **Installer les dépendances :**
   ```bash
   pip install pytest, flask
   ```
### Lancer l'application
Pour démarrer le serveur de développement, exécutez la commande suivante à la racine du projet :

  ```bash
  python app.py
  ```
L'application sera accessible à l'adresse suivante : http://127.0.0.1:5000

#### Instructions d’utilisation:

Une fois l’application ouverte, l’utilisateur peut : Entrer une expression (ex. 4+5, 9/3, 6*7) à l’aide des boutons de la calculatrice. Appuyer sur = pour afficher le résultat. Appuyer sur C pour effacer l’écran. En cas d’erreur (par exemple, une expression invalide), un message d’erreur s’affiche à l’écran.

### Tests:

Le dossier /tests contient les fichiers de tests unitaires pour valider les fonctions de calcul et la logique Flask. Pour exécuter les tests, utiliser la commande suivante :
  ```bash
pytest
 ```
ou 
  ```bash
python -m pytest
  ```
Les tests couvrent notamment : Les opérations arithmétiques (add, subtract, multiply, divide) Les erreurs de saisie dans la fonction calculate() Le bon fonctionnement du serveur Flask

### Flux de contribution (branches, PR, issues):

Le projet utilise un flux Git structuré pour assurer une bonne collaboration :

* main : version stable et testée du projet. bugfix/ : correction de bogues détectés par les tests.

Chaque bogue détecté est documenté dans une Issue GitHub avec :

* une description du problème, les étapes pour le reproduire, et l’assignation à un membre responsable.

* Les correctifs sont effectués sur une branche dédiée avant d’être validés via une Pull Request (PR).
