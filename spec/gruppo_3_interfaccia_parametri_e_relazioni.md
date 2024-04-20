## Parte 3 - Generazione interfaccia parametri e grafici delle relazioni

**Gruppo**: Matteo Favero

### Descrizione

La classe responsabile di gestire i parametri per le funzioni disegnate e la
creazione dei grafici di cerchi, ellissi e iperboli.

### Specifiche `BaseInputParametri`

Creare una classe astratta `BaseInputParametri` che definisce i metodi descritti
in seguito.

#### Costruttore

Il costruttore non è astratto e prende un unico argomento che è una stringa.

#### Attributi

- `fmt`: la stringa passata al costruttore

#### Metodi astratti

- `lista_nomi`: nelle sottoclassi restituisce una lista con i nomi dei parametri
  specificati
- `crea_widget`: nelle sottoclassi restituisce un widget di Tkinter
  (probabilmente un `Frame`) che contiene l'interfaccia utilizzata per inserire
  i valori dei parametri
- `valore`: prende un argomento che è il nome del parametro e restituisce il
  valore associato oppure `None` se il parametro non esiste oppure se non
  contiene un valore valido
- `validi`: nelle sottoclassi restituisce `True` se tutti i valori associati ai
  parametri sono validi, se anche solo uno non è valido restituisce `False`

### Specifiche `InputCaselle`

Creare una classe `InputCaselle` che eredita da `BaseInputParametri` e quindi
deve implementare i metodi astratti.

#### Costruttore

Il costruttore interpreta `fmt` in modo che i nomi dei parametri siano in mezzo
a segni di dollaro. Serve fare l'overriding richiamando con `super` l'`__init__`
della classe base.

#### Formato stringa dei parametri

Prendiamo come esempio la stringa `"y = $a$x^2 + $b$x + $c$"`, i parametri
definiti al suo interno sono `a`, `b` e `c`. Il widget creato dovrà quindi
essere

```text
y = [___]x^2 + [___]x + [___]
```

dove `[___]` sono caselle alternate a
etichette.

#### Metodi

- `lista_nomi` restituisce la lista dei nomi all'interno della stringa di
  formato
- `crea_widget` crea un widget come sopra indicato
- `valore` prende una stringa come argomento che contiene il nome del parametro
  di cui restituire il valore
- `validi` deve controllare che all'interno delle caselle di testo associate ai
  parametri ci siano numeri validi.

### Specifiche `InputFunzione`

Creare una classe `InputFunzione` che eredita da `BaseInputParametri` e quindi
deve implementare i metodi astratti.

#### Costruttore

Interpreta `fmt` come il nome della variabile indipendente della funzione, ad
esempio per `f(x)` è `x`, invece per `f(y)` è `y`. Anche qui è necessario
l'overriding richiamando con `super` l'`__init__` della classe base.

#### Formato del widget

Questa classe deve creare un widget nel formato

```text
f(<var>) = [_________________]
```

in cui `<var>` deve essere sostituita con il nome passato al costruttore. Nella
casella di testo viene scritta la funzione che poi deve essere passata a
[`interpreta_funzione`](https://github.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/blob/main/spec/gruppo_5_interpretazione_funzioni.md#specifiche-interpreta_funzione).

#### Metodi

- `lista_nomi` restituisce una stringa vuota
- `crea_widget` restituisce un widget nella forma indicata
- `valore` prende come argomento il numero della variabile indipendente e
  restituisce il valore calcolato dalla funzione interpretata oppure `None` se
  la funzione non è valida
- `validi` controlla che la funzione inserita sia valida

**Consiglio**: l'interpretazione di una funzione è molto complesso e
dispendioso, consiglio di eseguirlo solamente quando il contenuto della casella
di testo cambia e di salvare la funzione corrente in un attributo.

### Specifiche delle relazioni

Creare delle sottoclassi che derivano da `BaseGrafico` e che implementano i
metodi astratti per disegnare cerchi, ellissi e iperboli.
