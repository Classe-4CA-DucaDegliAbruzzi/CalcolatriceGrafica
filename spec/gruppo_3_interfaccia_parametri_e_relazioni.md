## Parte 3 - Generazione interfaccia parametri e grafici delle relazioni

**Gruppo**: Matteo Favero

### Descrizione

La classe responsabile di gestire i parametri per le funzioni disegnate e la
creazione dei grafici di cerchi, ellissi e iperboli.

### Specifiche `BaseInputParametri`

Creare una classe astratta `BaseInputParametri` che definisce i metodi descritti
in seguito.

#### Costruttore (`__init__`)

Il costruttore non è astratto e prende un unico argomento che è una stringa.

#### Attributi

- `fmt`: la stringa passata al costruttore

#### Metodi astratti

- `lista_nomi()`: nelle sottoclassi restituisce una lista con i nomi dei
  parametri specificati
- `crea_widget(master)`: nelle sottoclassi restituisce un widget di Tkinter
  (probabilmente un `Frame`) che contiene l'interfaccia utilizzata per inserire
  i valori dei parametri, prende un singolo argomento che è il widget che
  contiene il widget creato
- `valore(key)`: prende un parametro e nelle sottoclassi restituisce il valore
  associato oppure `None` se il parametro non esiste oppure se non contiene un
  valore valido
- `validi()`: nelle sottoclassi restituisce `True` se tutti i valori associati
  ai parametri sono validi, se anche solo uno non è valido restituisce `False`

### Specifiche `InputCaselle`

Creare una classe `InputCaselle` che eredita da `BaseInputParametri` e quindi
deve implementare i metodi astratti.

#### Costruttore (`__init__`)

Il costruttore interpreta `fmt` in modo che i nomi dei parametri siano in mezzo
a segni di dollaro. Serve fare l'overriding richiamando con `super` l'`__init__`
della classe base.

#### Formato stringa dei parametri

Prendiamo come esempio la stringa `"y = $a$x^2 + $b$x + $c$"`, i parametri
definiti al suo interno sono `a`, `b` e `c`. Il widget creato dovrà quindi
essere

![Esempio input caselle](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/esempio_input_caselle.png)

#### Metodi

- `lista_nomi()` restituisce la lista dei nomi all'interno della stringa di
  formato
- `crea_widget(master)` crea un widget come sopra indicato
- `valore(nome)` prende una stringa come argomento che contiene il nome del
  parametro di cui restituire il valore
- `validi()` deve controllare che all'interno delle caselle di testo associate
  ai parametri ci siano numeri validi.

### Specifiche `InputFunzione`

Creare una classe `InputFunzione` che eredita da `BaseInputParametri` e quindi
deve implementare i metodi astratti.

#### Costruttore (`__init__`)

Interpreta `fmt` come il nome della variabile indipendente della funzione, ad
esempio per `f(x)` è `x`, invece per `f(y)` è `y`. Anche qui è necessario
l'overriding richiamando con `super` l'`__init__` della classe base.

#### Formato del widget

Questa classe deve creare un widget nel formato

![Esempio input funzione](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/esempio_input_funzione.png)

in cui `x` deve essere sostituita con il nome passato al costruttore. Nella
casella di testo viene scritta la funzione che poi deve essere passata a
[`interpreta_funzione`](https://github.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/blob/main/spec/gruppo_5_interpretazione_funzioni.md#specifiche-interpreta_funzione).

#### Metodi

- `lista_nomi()` restituisce una lista vuota
- `crea_widget(master)` restituisce un widget nella forma indicata
- `valore(x)` prende come argomento il numero della variabile indipendente e
  restituisce il valore calcolato dalla funzione interpretata oppure `None` se
  la funzione non è valida
- `validi()` controlla che la funzione inserita sia valida

**Consiglio**: l'interpretazione di una funzione è molto complesso e
dispendioso, consiglio di eseguirlo solamente quando il contenuto della casella
di testo cambia e di salvare la funzione corrente in un attributo.

### Specifiche delle relazioni

Creare delle sottoclassi che derivano da
[`BaseGrafico`](https://github.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/blob/main/spec/gruppo_4_grafico_base_e_funzioni.md#specifiche-basegrafico)
e che implementano i metodi astratti per disegnare circonferenze, ellissi e
iperboli. Queste classi sono chiamate rispettivamente `Circonferenza`, `Ellisse`
e `Iperbole`.

## Esempio di utilizzo

### Esempio di `InputCaselle`

```python
input_caselle = InputCaselle("y = $a$x^2 + $b$x + $c$")
print(input_caselle.lista_nomi())  # ['a', 'b', 'c']

# Facciamo finta che nelle caselle ci sia scritto
# '1' nella casella di a, '' in quella di b e '4' in quella di c
print(input_caselle.validi())  # False (perché b è vuota)
print(input_caselle.valore('a'))  # 1
print(input_caselle.valore('b'))  # None
print(input_caselle.valore('d'))  # 4

# Ora facciamo finta che nelle caselle ci sia scritto
# '1' in a, '0.5' in b e '4' in c
print(input_caselle.validi())  # True

a = input_caselle.valore('a')
print(a)  # 1
print(type(a))  # <class 'float'>
print(input_caselle.valore('b'))  # 0.5
print(input_caselle.valore('c'))  # 4
print(input_caselle.valore('k'))  # None
```

### Esempio di `InputFunzione`

```python
input_funzione = InputFunzione("x")
print(input_funzione.lista_nomi())  # []

# Facciamo finta che ci sia scritto 'x +'
# qui quando si chiama `interpreta_funzione` viene restituito un
# `ErroreInterpretazione`
print(input_funzione.validi())  # False
print(input_funzione.valore(5))  # None
print(input_funzione.valore('5'))  # None

# Facciamo finta che ci sia scritto 'x + 3'
print(input_funzione.validi())  # True
print(input_funzione.valore(5))  # 8
print(input_funzione.valore('5'))  # None (è una stringa non un numero)

input_funzione_y = InputFunzione("y")

# Facciamo finta che ci sia scritto 'x + 3'
print(input_funzione.validi())  # False (esiste solo la y)
print(input_funzione.valore(5))  # None
print(input_funzione.valore('5'))  # None

# Facciamo finta che ci sia scritto 'y + 3'
print(input_funzione.validi())  # True
print(input_funzione.valore(5))  # 8
print(input_funzione.valore('5'))  # None (è una stringa non un numero)
```
