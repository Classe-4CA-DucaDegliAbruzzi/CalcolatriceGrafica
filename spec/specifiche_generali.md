# Specifiche gruppi

![Lavagna con le specifiche decise in classe](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/lavagna.jpeg)

Se si voglio aggiungere attributi o metodi non richiesti alle classi
specificate, questi devono avere due trattini bassi prima del nome:

```text
❌
metodo_non_richiesto
attributo_non_richiesto

✅
__metodo_non_richiesto
__attributo_non_richiesto
```

## Numeri gruppi

- Gruppo 1: Francesco Desario
- Gruppo 2: Elia Bertoldo
- Gruppo 3: Matteo Favero
- Gruppo 4: Emma Rossi
- Gruppo 5: Davide Taffarello

## Diagramma classi

![Diagramma classi](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/diagramma_classi.png)

## Stile

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
