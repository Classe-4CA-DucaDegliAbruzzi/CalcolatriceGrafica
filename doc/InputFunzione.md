# `InputFunzione`

## Descrizione

È una sottoclasse di [`BaseInputParametri`](BaseInputParametri.md) che permette all'utente di inserire
una funzione qualsiasi.

## Interpretazione di `fmt`

La stringa di formato per questa classe è il nome della variabile indipendente
della funzione. Se si vuole scrivere una funzione `f(x)`, in cui la variabile
indipendente è la `x`, la stringa di formato deve contenere la stringa `'x'`.

## Metodi

### `lista_nomi()`

Restituisce sempre una lista vuota. Non ci sono parametri veri e propri in una
funzione qualsiasi.

Questo metodo non prende argomenti.

### `crea_widget(master)`

Crea un widget in cui c'è una `tkinter.Label` in cui è scritto `f(<var>) = `,
con al posto di `<var>` il nome della variabile indipendente affiancata a una
`tkinter.Entry` che permette all'utente di inserire la funzione.

Nell'esempio sopra (con `f(x)`) il widget dovrebbe essere simile a questo:

![Esempio input funzione](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/esempio_input_funzione.png)

### `valore(x)`

Prende come argomento la `x` e restituisce la `y` associata. La `y` è calcolata
con la funzione inserita dall'utente. Se la funzione inserita non è corretta
questo metodo restituisce `None`.

### `validi()`

Restituisce `True` se la funzione inserita dall'utente è valida e `False` se non
lo è.

Questo metodo non prende argomenti.

## Esempi

```python
input_funzione = InputFunzione("x")
print(input_funzione.lista_nomi())  # []

# Facciamo finta che ci sia scritto 'x +'
# qui quando si chiama [`interpreta_funzione`](interpreta_funzione.md) viene restituito un
# [`ErroreInterpretazione`](ErroreInterpretazione.md)
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
