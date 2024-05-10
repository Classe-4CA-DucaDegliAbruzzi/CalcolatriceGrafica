# `BaseGrafico`

## Descrizione

Una classe astratta da cui ereditano classi che disegnano i grafici.

## Costruttore (`__init__`)

Il costruttore prende un solo argomento di tipo [`Tela`](Tela.md). Questo argomento è poi
accessibile attraverso l'attributo `tela`. Questa è la tela dove verrà disegnata
la funzione.

## Attributi

### `param`

Questo attributo è impostato nel costruttore e il suo valore è quello che viene
restituito da `crea_param`. Può essere successivamente usato per accedere ai
parametri inseriti dall'utente attraverso l'interfaccia grafica.

### `tela`

Questa è la tela passata al costruttore dove la sottoclasse di `BaseGrafico`
deve disegnare l'equazione con i metodi `linea`, `linee` e `ellisse`. Vedere
la documentazione di [`Tela`](Tela.md) per più informazioni.

## Metodi astratti

### `crea_param()`

**QUESTO METODO NON DEVE ESSERE CHIAMATO**, utilizzare l'attributo `param` per
accedere all'input dei parametri.

Questo metodo è responsabile di restituire una nuova istanza dell'input dei
parametri utilizzato dalla classe per disegnare la funzione. Vedere la
documentazione di [`InputCaselle`](InputCaselle.md) e [`InputFunzione`](InputFunzione.md) per più informazioni.

Questo metodo non prende argomenti.

### `disegna()`

Questo metodo disegna la funzione specifica della classe sulla tela.

Questo metodo non prende argomenti e non restituisce un valore.

## Esempi

```python
class EllissiSemplice(BaseGrafico):
    def crea_param(self):
        return InputCaselle("x^2 / $a$^2 + y^2 / $b$^2 = 1")

    def disegna(self):
        if not self.param.validi():
            return
        a = self.param.valore("a")
        b = self.param.valore("b")
        
        # Codice che disegna l'ellissi su self.tela
        ...

    
ellissi = EllissiSemplice(tela)

tela.disegna_sfondo()
ellissi.disegna()
tela.disegna_numeri()
```
