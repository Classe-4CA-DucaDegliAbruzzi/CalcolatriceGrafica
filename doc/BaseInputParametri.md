# `BaseInputParametri`

## Descrizione

La classe astratta da cui ereditano le classi responsabili di gestire i
parametri per le funzioni disegnate. Le classi che derivano da questa sono
utilizzate nel metodo `crea_param` delle sottoclassi di [`BaseGrafico`](BaseGrafico.md).

## Costruttore (`__init__`)

Il costruttore prende un unico argomento che è la stringa accessibile con
l'attributo `fmt`.

## Attributi

### `fmt`

La stringa passata al costruttore (fmt sta per "formato").

## Metodi astratti

Le sottoclassi poi faranno l'overriding di questi metodi, vedere le singole
sottoclassi per il funzionamento più specifico.

### `lista_nomi()`

Nelle sottoclassi restituisce una lista con i nomi dei parametri specificati.

Questo metodo non prende argomenti.

### `crea_widget(master)`

Nelle sottoclassi restituisce un widget di tkinter che contiene l'interfaccia
utilizzata per inserire i valori dei parametri, prende un singolo argomento che
è il widget che contiene il widget creato (in tkinter chiamato "master").

### `valore(key)`

Prende un parametro e nelle sottoclassi restituisce il valore
associato oppure `None` se il parametro non esiste oppure se non contiene un
valore valido.

### `validi()`

Nelle sottoclassi restituisce `True` se tutti i valori associati
ai parametri sono validi, se anche solo uno non è valido restituisce `False`.

Questo metodo non prende argomenti.
