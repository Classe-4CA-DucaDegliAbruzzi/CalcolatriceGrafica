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
`NodoBase` oppure un'istanza di `ErroreInterpretazione`.

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
