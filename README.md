# Calcolatrice Grafica

## Specifiche

Potete trovare le specifiche nella cartella `spec/`.

## Codice

Mettere il codice sorgente in `src/`, non modificare `main.py` eccetto per
quanto richiesto al suo interno. Per il proprio codice sorgente si possono
creare dei nuovi file.

### Stile

Possibilmente seguire lo stile definito nella [PEP 8](https://peps.python.org/pep-0008/).

Utilizzare nomi di variabili descrittivi eccetto in contesti matematici:

```python
❌
a = []
x = "Errore"

✅
parti_funzione = []
msg_errore = "Errore"
a * x**2 + b * x + c
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

**ATTENZIONE**

È richiesto solo di scrivere funzioni o classi, mai qualcosa che viene
eseguito fine a sé stesso. Se nel vostro codice qualcosa viene eseguito senza
che ci sia un `if __name__ == "__main__"` avete sbagliato qualcosa. Il codice
dentro a classi e funzioni non è eseguito se non chiamato esplicitamente.
