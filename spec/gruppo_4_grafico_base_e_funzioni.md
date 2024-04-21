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
Prende due parametri: una tela, di tipo
[`Tela`](https://github.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/blob/main/spec/gruppo_2_tela_disegno_grafici.md#specifiche-tela),
e la classe dei parametri da utilizzare la quale deve derivare da
[`BaseInputParametri`](https://github.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/blob/main/spec/gruppo_3_interfaccia_parametri_e_relazioni.md#specifiche-baseinputparametri).

#### Attributi

- `param`: l'istanza dell'input parametri creata con la classe passata al
  costruttore
- `tela`: la tela passata al costruttore.

#### Metodi astratti

- `str_formato()`: un metodo che restituisce la stringa utilizzata come formato
  dalla classe dell'input parametri
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

- `str_formato()` rimane astratto
- `funzione(x, parametri)`: un metodo che prende due argomenti, il primo è il
  valore della x per `BaseGraficoFunzioneX` oppure della y per
  `BaseGraficoFunzioneY`, il secondo è un dizionario che contiene come chiavi i
  nomi dei parametri di `param` e come valori i valori di questi parametri

#### Metodi

- `disegna`: questo metodo viene implementato e disegna la funzione, nel caso di
  `BaseGraficoFunzioneX` va da un estremo all'altro dell'asse x e calcola la y
  con la funzione, invece `BaseGraficoFunzioneY` va da un estremo all'altro
  dell'asse y e calcola il valore della x con la funzione
