# Tests module

## Raison d'etre

Ce module contient les tests automatises pour la logique de calcul et les
operateurs arithmetiques.

## Comment executer les tests

Depuis la racine du projet:

```
python -m pytest
```

Pour voir chaque test (reussi ou echoue):

```
python -m pytest -v
```

## Ce qui est couvert

- Parsing et evaluation d'expressions simples (fonction `calculate`).
- Operations de base: addition, soustraction, multiplication, division.

## Notes

Si des tests echouent, cela indique un ecart entre le comportement attendu
et l'implementation actuelle.
