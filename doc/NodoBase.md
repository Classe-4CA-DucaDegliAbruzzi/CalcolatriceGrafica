# `NodoBase`

## Descrizione

Questa classe è la superclasse di tutte le classi che rappresentano una funzione
interpretata da [`interpreta_funzione`](interpreta_funzione.md). Quindi il metodo descritto per questa
classe (`calcola`) può essere utilizzato quando [`interpreta_funzione`](interpreta_funzione.md) non trova
errori nella funzione.

## Metodi

### `calcola(val)`

Calcola la funzione inserita utilizzando `val` come il valore della variabile
indipendente. `val` è un numero (quindi di tipo `int` oppure `float`).

Questo metodo restituisce il valore della funzione calcolato con `val`. Nel
caso in cui `val` è fuori dal dominio della funzione viene restituito `None`.

## Esempi

```python
funzione1 = interpreta_funzione("x + 3", "x")
# qui `val` è sostituito alla x
print(funzione1.calcola(0))  # 3
print(funzione1.calcola(5))  # 8

funzione2 = interpreta_funzione("y + 3", "y")
# qui `val` è sostituito alla y
print(funzione2.calcola(0))  # 3
print(funzione2.calcola(5))  # 8
```
