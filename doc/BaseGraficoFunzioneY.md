# `BaseGraficoFunzioneY`

## Descrizione

Una classe astratta che è sottoclasse di `BaseGrafico` e che permette alle
classi che ereditano da essa di disegnare una funzione qualsiasi in cui la
variabile indipendente è la y.

## Attributi

Vedere `BaseGrafico`.

## Metodi astratti

### `crea_param()`

Questo metodo rimane astratto. Vedere `BaseGrafico` per più informazioni.

### `funzione(y, parametri)`

Questo metodo implementa la funzione che deve essere disegnata dalla classe.
Prende due argomenti: il primo è il valore della y, il secondo sono i parametri
inseriti dall'utente. Poi calcola il valore della x associato e lo restituisce.

L'argomento `parametri` è un dizionario che viene creato a partire dall'input
dei parametri della classe (quello che contiene l'attributo `param`). Le chiavi
sono i nomi dei parametri e i valori associati alle chiavi sono i valori che si
ottengono con il metodo `valore` di `param` (vedere `BaseInputParametri` per
più informazioni).

I parametri che sono inseriti all'interno di questo dizionario sono quelli
all'interno della lista restituita da `lista_nomi`. Quindi quando l'input dei
parametri è un `InputFunzione` il dizionario sarà vuoto perché `lista_nomi`
restituisce sempre una lista vuota (vedere `InputFunzione` per più
informazioni).

## Metodi

### `disegna()`

Questo metodo disegna il grafico della funzione definita dal metodo `funzione`.

Questo metodo non prende argomenti e non restituisce un valore.

## Esempi

```python
class ParabolaRuotata(BaseGraficoFunzioneY):
    def crea_param(self):
        return InputCaselle("x = $a$y^2 + $b$y + $c$")

    def funzione(self, y, parametri):
        a = parametri["a"]
        b = parametri["b"]
        c = parametri["c"]
        return a * y**2 + b * y + c
```
