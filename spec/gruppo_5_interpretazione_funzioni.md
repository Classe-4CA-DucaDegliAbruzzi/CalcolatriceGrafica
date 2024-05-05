## Parte 5 - Interpretazione delle funzioni inserite

**Gruppo**: Davide Taffarello

### Descrizione

Un oggetto che interpreta una stringa come una funzione. La sintassi delle
funzioni è lasciata a discrezione del gruppo.

### Specifiche `interpreta_funzione`

Creare una funzione `interpreta_funzione` con le caratteristiche descritte in
seguito.

#### Argomenti

- il primo argomento è di tipo `str` ed è la stringa da interpretare come
  funzione
- anche il secondo argomento è di tipo `str` ed è il nome della variabile
  indipendente della funzione (es. `'x'`)

#### Valore restituito

Il valore restituito può essere di uno di due tipi: una sottoclasse di
`NodoBase` oppure un'istanza di `ErroreInterpretazione` o sottoclasse.

**Attenzione**: NON SCRIVERE `type(var) == ErroreInterpretazione` NON FUNZIONA,
vedere esempio per capire come fare.

### Specifiche `NodoBase`

Creare una classe astratta `NodoBase` che abbia le caratteristiche scritte di
seguito.

#### Metodi astratti

- `calcola(x)`: prende un argomento che è il valore della variabile indipendente
  e restituisce il valore della funzione per il parametro passato oppure `None`
  se il parametro è fuori dal dominio

### Specifiche `ErroreInterpretazione`

Creare una classe `ErroreInterpretazione` che abbia le caratteristiche scritte
di seguito. **Non si devono creare istanze di questa classe** al di fuori di
`interpreta_funzioni`, quindi il costruttore è libero.

#### Metodi

- `msg()`: restituisce una stringa che contiene la spiegazione dell'errore


## Esempio di utilizzo

```python
# `entry` è una casella
# Facciamo finta che al momento ci sia scritto 'x +'
funzione = interpreta_funzione(entry.get(), "x")
print(type(funzione))  # <class 'interpretatore.ErroreInterpretazione'>
print(funzione.msg())  # Atteso un valore

# per controllare se `funzione` è un errore
if isinstance(funzione, ErroreInterpretazione):
    # codice da eseguire se `funzione` è un errore
    ...

# NON FARE `type(funzione) == ErroreInterpretazione` NON FUNZIONA

# Ora facciamo finta che ci sia scritto 'x + 3'
funzione = interpreta_funzione(entry.get(), "x")
# Non è `ErroreInterpretazione` quindi va bene
print(type(funzione))  # <class 'interpretatore.interpretatore.NodoBinario'>
print(funzione.calcola(5))  # 8
print(funzione.calcola('5'))  # None (è una stringa)

# Errore di Python: non si può creare un'istanza di `ErroreInterpretazione`
il_mio_errore = ErroreInterpretazione("messaggio")

# Errore di Python: non si può creare un'istanza di una classe astratta
il_mio_nodo = NodoBase()
```
