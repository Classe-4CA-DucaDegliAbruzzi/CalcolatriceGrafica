# InputCaselle

## Descrizione

È una sottoclasse di `BaseInputParametri` che permette inserire i valori
definendo i parametri in un'equazione predefinita.

## Interpretazione di `fmt`

La stringa di formato per questa classe è l'equazione che si vuole disegnare in
cui i parametri sono lettere con prima e dopo un segno di dollaro (`$`).
Prendiamo come esempio l'equazione di una parabola, `y = ax^2 + bx + c`. In
questo caso i parametri sono `a`, `b` e `c` e quindi la stringa di formato è
`y = $a$x^2 + $b$x + $c$`.

## Metodi

### `lista_nomi()`

Restituisce la lista dei nomi dei parametri all'interno della stringa di
formato. Nell'esempio sopra questo metodo restituirebbe `['a', 'b', 'c']`.

Questo metodo non prende argomenti.

### `crea_widget(master)`

Crea un widget in cui le `tkinter.Entry` sono messe al posto dei nomi dei
parametri per inserire i valori e delle `tkinter.Label` sono usate per il resto
del testo.

Nell'esempio sopra il widget dovrebbe essere simile a questo:

![Esempio input caselle](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/esempio_input_caselle.png)

### `valore(nome)`

Prende il nome di uno dei parametri come argomento e restituisce il valore
inserito nella `tkinter.Entry` associata al parametro indicato. Nell'esempio
sopra, per prendere il valore del parametro `a` si può scrivere
`param.valore('a')`. Se il nome non esiste questo metodo restituisce `None`.

### `validi()`

Deve controllare che all'interno delle caselle di testo associate ai parametri
ci siano numeri validi. Se sono tutti numeri validi questo metodo restituisce
`True`, altrimenti restituisce `False`.

Questo metodo non prende argomenti.

## Esempi

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
