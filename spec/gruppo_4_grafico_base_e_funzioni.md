## Parte 4 - Grafico di base e funzioni semplici

**Gruppo**: Emma Rossi

### Descrizione

La classe base per il disegno dei grafici, la classe base del disegno delle
funzioni e le funzioni che hanno parametri particolari.

### Specifiche `BaseGrafico`

Creare una classe astratta `BaseGrafico` che definisca i metodi descritti in
seguito.

#### Costruttore

Il costruttore non è astratto e non deve essere modificato dalle sottoclassi.
Prende un solo parametro: una tela, di tipo
[`Tela`](https://github.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/blob/main/spec/gruppo_2_tela_disegno_grafici.md#specifiche-tela).

#### Attributi

- `param`: l'istanza dell'input parametri restituita da `crea_param`
- `tela`: la tela passata al costruttore

#### Metodi astratti

- `crea_param()`: un metodo che restituisce una nuova istanza di una sottoclasse
  di `BaseInputParametri` **non deve essere chiamato** ma deve essere solo
  sovrascritto dalle sottoclassi
- `disegna()`: un metodo che disegna la funzione sulla `tela`

### Specifiche `BaseGraficoFunzioneX` e `BaseGraficoFunzioneY`

Creare due classi astratte `BaseGraficoFunzioneX` e  `BaseGraficoFunzioneY` che
derivano da `BaseGrafico`.

Scrivere così le dichiarazioni:

```python
class BaseGraficoFunzioneX(BaseGrafico, ABC):
    ...
class BaseGraficoFunzioneY(BaseGrafico, ABC):
    ...
```

Scrivere `(ABC, BaseGrafico)` risulterebbe in un errore.

#### Metodi astratti

- `crea_param()` rimane astratto
- `funzione(x, parametri)`: un metodo che prende due argomenti, il primo è il
  valore della x per `BaseGraficoFunzioneX` oppure della y per
  `BaseGraficoFunzioneY`, il secondo è un dizionario che contiene come chiavi i
  nomi dei parametri di `param` e come valori i valori di questi parametri

#### Metodi

- `disegna`: questo metodo viene implementato e disegna la funzione, nel caso di
  `BaseGraficoFunzioneX` va da un estremo all'altro dell'asse x e calcola la y
  con la funzione, invece `BaseGraficoFunzioneY` va da un estremo all'altro
  dell'asse y e calcola il valore della x con la funzione

## Esempio di utilizzo

### Esempio di `BaseGrafico`

```python
# `BaseGrafico` è una classe astratta, occorre creare una classe che definisca
# i metodi astratti

class EllissiSemplice(BaseGrafico):
    def crea_param(self):
        return InputCaselle("x^2 / $a$ + y^2 / $b$ = 1")

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

### Esempio di `BaseGraficoFunzioneX`

```python
# `BaseGraficoFunzioneX` è una classe astratta, occorre creare una classe che
# definisca i metodi astratti

class Parabola(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputCaselle("y = $a$x^2 + $b$x + $c$")

    def funzione(self, x, parametri):
        a = parametri["a"]
        b = parametri["b"]
        c = parametri["c"]
        return a * x**2 + b * x + c

    
parabola = Parabola(tela)

tela.disegna_sfondo()
parabola.disegna()  # questo metodo è definito da `BaseGraficoFunzioneX`
tela.disegna_numeri()
```
