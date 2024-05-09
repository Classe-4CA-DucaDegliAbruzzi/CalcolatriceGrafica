# Parte 1 - Interfaccia generale

**Gruppo**: Francesco Desario

## Descrizione

L'interfaccia che mette insieme quello che viene prodotto dagli altri gruppi.

## Specifiche `Applicazione`

L'interfaccia deve permettere di fare le seguenti cose:

- scegliere la funzione da visualizzare con la tela
- modificare il range che si vede all'interno della tela
- quando la funzione che si sta visualizzando è una funzione inserita
  dall'utente (non una che accetta solo dei parametri) si deve poter fornire
  un valore specifico da calcolare alla funzione
- la tela deve essere quadrata, di 500 pixel per 500

Per creare questa interfaccia creare una classe `Applicazione` con le seguenti
caratteristiche:

### Costruttore (`__init__`)

Non prende nessun argomento.

### Metodi

- `run()`: apre la finestra, non prende argomenti

Vedere `main.py` per come viene usata la classe `Applicazione`.

## Selezione delle funzioni

Quando l'utente sceglie una funzione si deve creare l'istanza di una classe che
deriva da `BaseGrafico`. Queste classi sono create dai gruppi 3 e 4 e sono le
seguenti:

- `Circonferenza` (gruppo 3)
- `Ellisse` (gruppo 3)
- `Iperbole` (gruppo 3)
- `Retta` (gruppo 4)
- `Seno` (gruppo 4)
- `Coseno` (gruppo 4)
- `Parabola` (gruppo 4)
- `FunzioneX` (gruppo 4)
- `FunzioneY` (gruppo 4)

Per l'inserimento dei dati utilizzare il widget fornito dal metodo `crea_widget`
dell'attributo `param`. **Chiamare questo metodo una sola volta per istanza.**

## Modificare il range della tela

L'interfaccia deve permettere di modificare gli attributi `range_x` e `range_y`
della `Tela` che si usa per disegnare il grafico selezionato.

Se il range delle x è `(x_min, x_max)`, `x_min` deve essere minore di `x_max`.
Lo stesso vale per il range delle y.
