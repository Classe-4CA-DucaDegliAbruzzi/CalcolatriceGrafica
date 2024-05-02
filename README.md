# Calcolatrice Grafica

## Specifiche

Potete trovare le specifiche nella cartella `spec/`.

## Numeri gruppi

- Gruppo 1: Francesco Desario
- Gruppo 2: Elia Bertoldo
- Gruppo 3: Matteo Favero
- Gruppo 4: Emma Rossi
- Gruppo 5: Davide Taffarello

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

Possibilmente seguire lo stile definito nella [PEP 8](https://peps.python.org/pep-0008/).

Utilizzare nomi di variabili descrittivi eccetto in contesti matematici:[^1]

[^1]: motivo: rende il codice più leggibile e semplice da interpretare

```python
❌
a = []
x = "Errore"

✅
parti_funzione = []
msg_errore = "Errore"
y = a * x**2 + b * x + c
```

Utilizzare un'indentazione di quattro spazi (e *non* tabulazioni):[^2]

[^2]: motivo: evita errori di indentazione

```python
❌
def funzione():
  return "Hello"

✅
def funzione():
    return "Hello"
```

Per eseguire del codice all'interno di un file che state scrivendo e che non
è `main.py`, il codice deve essere messo dentro `if __name__ == "__main__"`:[^3]

[^3]: motivo: serve eseguire codice per testare, non deve essere eseguito quando
il file è semplicemente importato.

```python
❌
print("Prova")

✅
if __name__ == "__main__":
    print("prova")
```

I nomi di classi, funzioni e attributi devono essere esattamente quelli
descritti nelle specifiche:[^4]

[^4]: motivo: le specifiche servono a tutti per utilizzare parti di codice che
non hanno scritto, utilizzare nomi diversi renderebbe inutili le specifiche a
questo scopo.

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
