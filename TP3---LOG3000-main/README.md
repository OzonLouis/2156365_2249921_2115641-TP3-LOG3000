# Module racine

## Raison d'etre

Ce module contient l'application Flask et la logique de calcul. Il orchestre
le routage HTTP, la validation des expressions et l'appel aux operateurs.

## Fichiers principaux

- app.py: point d'entree de l'application Web et route principale.
- operators.py: operations arithmetiques utilisees par le calculateur.

## Dependances et hypotheses

- Python 3.x.
- Flask pour le serveur Web et le rendu des templates.
- L'interface Web envoie une expression avec un seul operateur binaire.
