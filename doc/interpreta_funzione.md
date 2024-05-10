# `interpreta_funzione`

## Descrizione

Questa funzione analizza una funzione inserita dall'utente.

## Argomenti

### `funzione_utente`

Questa è una stringa che contiene quello che viene inserito dall'utente. Ad
esempio può essere `10 + 3x` oppure `y^2 + 9`.

### `var_indipendente`

Questa è una stringa che contiene il nome della variabile indipendente della
funzione. Per `10 + 3x` questa stringa deve contenere `x` e per `y^2 + 9`
deve contenere `y`. I nomi delle variabili indipendenti possono contenere solo
lettere e non sono limitate a una lettera.

## Valore restituito

Questa funzione restituisce uno di due tipi di valori: una sottoclasse di
[`NodoBase`](NodoBase.md) oppure un [`ErroreInterpretazione`](ErroreInterpretazione.md).

La sottoclasse di [`NodoBase`](NodoBase.md) è restituita quando `funzione_utente` contiene una
funzione valida.

[`ErroreInterpretazione`](ErroreInterpretazione.md) invece è restituito quando `funzione_utente` non
contiene una funzione valida.

## Esempi

```python
funzione = interpreta_funzione("10 + 3x", "x")

if isinstance(funzione, ErroreInterpretazione):
    print("Errore nella funzione:", funzione.msg())
else:
    print("Il valore allo 0 è", funzione.calcola(0))
```
