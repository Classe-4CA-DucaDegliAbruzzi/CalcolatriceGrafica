# Parte 2 - Tela per il disegno dei grafici

**Gruppo**: Elia Bertoldo

## Descrizione

La parte dell'interfaccia in cui vengono disegnati i grafici.

## Specifiche `Tela`

Creare una classe `Tela` con i seguenti requisiti.

### Costruttore (`__init__`)

- il costruttore deve accettare un solo argomento di tipo
  [`Canvas`](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html)

### Attributi

- `range_x`: una **tupla di due numeri (`float` o `int`)**, il primo è il valore
  di x all'estremo sinistro della tela e il secondo è il valore all'estremo
  destro
- `range_y`: una **tupla di due numeri (`float` o `int`)**, il primo è il valore
  di y all'estremo inferiore della tela e il secondo è il valore all'estremo
  superiore
- `colore`: il colore da utilizzare per tracciare le figure, è di tipo `str`
  nel formato `#XXXXXX` in cui `XXXXXX` è il colore in esadecimale, ad esempio
  il rosso è `#FF0000`
- `spessore`: lo spessore della linea con cui sono tracciate le figure, è di
  tipo `int`

### Metodi

**Nota**: per come funzionano le coordinate della tela e le coordinate del piano
vedi sotto.

- `w()`: restituisce la larghezza in pixel della `Canvas`, non prende argomenti
- `h()`: restituisce l'altezza in pixel della `Canvas`, non prende argomenti
- `x_tela_a_x_piano(x_tela)`, `y_tela_a_y_piano(y_tela)`: convertono una
  coordinata della tela a una coordinata del piano
- `x_piano_a_x_tela(x_piano)`, `y_piano_a_y_tela(y_piano)`: convertono una
  coordinata del piano a una coordinata sulla tela
- `linea(p1, p2)`: disegna un segmento sulla tela
  - prende i due estremi come argomenti che sono tuple o liste di lunghezza 2
    contenenti numeri interi; i punti sono espressi come coordinate della
    `Canvas` passata al costruttore
  - il colore e lo spessore del segmento sono dettati dagli attributi `colore` e
    `spessore`
- `linee(punti)`: disegna vari segmenti connessi agli estremi
  - prende come argomento una lista di punti; se la lista contiene quattro
    punti, `p1`, `p2`, `p3` e `p4`, verranno disegnati tre segmenti: il primo da
    `p1` a `p2`, il secondo da `p2` a `p3` e il terzo da `p3` a `p4`
  - il colore e lo spessore dei segmenti sono dettati dagli attributi `colore` e
    `spessore`
- `ellisse(p1, p2)`: disegna l'ellisse inscritta nel rettangolo definito da `p1`
  e `p2`
  - prende come argomenti due punti: `p1` è l'angolo in alto a sinistra del
    rettangolo e `p2` quello in basso a destra
  - il colore e lo spessore dell'ellisse è dettato dagli attributi `colore` e
    `spessore`
- `disegna_sfondo()`: disegna le linee del piano sulla `Canvas`
  - è a discrezione del gruppo come queste cambiano al cambiare di `range_x` e
    `range_y`
  - *non seguono* `colore` e `spessore`
- `disegna_numeri()`: disegna i numeri delle linee disegnate con
  `disegna_sfondo`
- `pulisci()`: ripulisce la tela togliendo tutti gli elementi disegnati

#### Coordinate del piano e coordinate della tela

Le coordinate della tela hanno il punto `(0, 0)` in alto a sinistra. La x cresce
da sinistra verso destra (come nel piano cartesiano) e la y dall'alto verso il
basso (il contrario del piano cartesiano). Queste coordinate sono legate alla
`Canvas` che viene passata al costruttore.

Le coordinate del piano invece sono le normali coordinate del piano cartesiano
utilizzate nel calcolo dei valori all'interno delle funzioni. `range_x` e
`range_y` definiscono i range che si vedono nei due assi di queste coordinate
nella finestra. Quindi, cambiando `range_x` e `range_y`, anche la conversione da
coordinata del piano e coordinata della tela cambia.

## Esempio di utilizzo

```python
# `canvas` è un oggetto di tipo tk.Canvas
tela = Tela(canvas)

tela.colore = "#FF0000"  # rosso
tela.spessore = 2
tela.range_x = (-5, 5)
tela.range_y = (-5, 5)

# disegna le linee di sfondo
tela.disegna_sfondo()

# disegna un segmento da (-3, 2) a (4, 1)
x1 = tela.x_piano_a_x_tela(-3)
y1 = tela.y_piano_a_y_tela(2)

x2 = tela.x_piano_a_x_tela(4)
y2 = tela.y_piano_a_y_tela(1)
tela.linea((x1, y1), (x2, y2))

# disegna i numeri delle linee
tela.disegna_numeri()
```

## Immagini

Schema coordinate tela VS coordinate piano:

![Coordinate](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/coordinate.png)

Metodo `ellisse`:

![Ellisse](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/ellisse.png)

Metodo `linea`:

![Linea](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/linea.png)

Metodo `linee`:

![Linee](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/linee.png)
