# Calcolatrice Grafica

## Specifiche

Potete trovare le specifiche nella cartella `spec/`.

## Numeri gruppi

- Gruppo 1: Francesco Desario
- Gruppo 2: Elia Bertoldo
- Gruppo 3: Matteo Favero
- Gruppo 4: Emma Rossi
- Gruppo 5: Davide Taffarello

## Diagramma classi

![Diagramma classi](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/diagramma_classi.png)

## Codice

Mettere il codice sorgente in `src/`, non modificare `main.py` eccetto per
quanto richiesto al suo interno. Per il proprio codice sorgente si possono
creare dei nuovi file.

**ATTENZIONE**

È richiesto solo di scrivere funzioni o classi, mai qualcosa che viene
eseguito fine a sé stesso. **Se nel vostro codice qualcosa viene eseguito senza
che ci sia un `if __name__ == "__main__"` avete sbagliato qualcosa.** Il codice
dentro a classi e funzioni non è eseguito se non chiamato esplicitamente
(leggere sotto per capire come usare `if __name__ == "__main__"`).

### Stile

Utilizzare nomi di variabili descrittivi eccetto in contesti matematici:

```python
❌
a = []
x = "Errore"

✅
parti_funzione = []
msg_errore = "Errore"
y = a * x**2 + b * x + c
```

Utilizzare un'indentazione di quattro spazi (e *non* tabulazioni):

```python
❌
def funzione():
  return "Hello"

✅
def funzione():
    return "Hello"
```

Per eseguire del codice all'interno di un file che state scrivendo e che non
è `main.py`, il codice deve essere messo dentro `if __name__ == "__main__"`:

```python
❌
print("Prova")

✅
if __name__ == "__main__":
    print("prova")
```

I nomi di classi, funzioni e attributi devono essere esattamente quelli
descritti nelle specifiche:

```python
❌
class base_grafico(ABC):
    ...

class InputFunzione:
    def Validi(self):
        ...

✅
class BaseGrafico(ABC):
    ...

class InputFunzione:
    def validi(self):
        ...
```

Controllare il tipo di un oggetto con `isinstance` e non con `type(x) == ...`:

```python
❌
if type(funzione) == ErroreInterpretazione:
    ...
if type(funzione) == NodoBase:
    ...

✅
if isinstance(funzione, ErroreInterpretazione):
    ...
if isinstance(funzione, NodoBase):
    ...
```
