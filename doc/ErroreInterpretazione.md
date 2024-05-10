# `ErroreInterpretazione`

## Descrizione

Una classe che rappresenta un errore di interpretazione di una funzione
inserita dall'utente. Questa classe è uno dei possibili valori di ritorno di
[`interpreta_funzione`](interpreta_funzione.md).

Non si possono creare istanze di questa classe, quindi scrivere
`errore = ErroreInterpretazione('il mio messaggio')` risulta in un errore.

## Metodi

### `msg()`

Restituisce un messaggio che chiarisce l'errore commesso.

Questo metodo non prende argomenti.

## Esempi

```python
risultato = interpreta_funzione("x +", "x")

print(risultato.msg())  # stampa 'atteso un valore'
```
