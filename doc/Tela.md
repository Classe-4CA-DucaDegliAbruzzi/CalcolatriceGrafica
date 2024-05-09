# `Tela`

## Descrizione

Una classe che permette di disegnare all'interno di una `tkinter.Canvas`.

## Costruttore (`__init__`)

Il costruttore prende un singolo argomento di tipo
[`tkinter.Canvas`](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html).
L'istanza è creata con `Tela(canvas)`.

## Coordinate del piano VS coordinate della tela

![Coordinate](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/coordinate.png)

Le coordinate della tela hanno il punto `(0, 0)` in alto a sinistra. La x cresce
da sinistra verso destra (come nel piano cartesiano) e la y dall'alto verso il
basso (il contrario del piano cartesiano). Queste coordinate sono legate alla
`Canvas` che viene passata al costruttore.

Le coordinate del piano invece sono le normali coordinate del piano cartesiano
utilizzate nel calcolo dei valori all'interno delle funzioni. `range_x` e
`range_y` definiscono i range che si vedono nei due assi di queste coordinate
nella finestra. Quindi, cambiando `range_x` e `range_y`, anche la conversione da
coordinata del piano e coordinata della tela cambia.

I metodi `x_tela_a_x_piano`, `y_tela_a_y_piano`, `x_piano_a_x_tela` e
`y_piano_a_y_tela` permettono di passare da un sistema di coordinate all'altro.

## Attributi

### `range_x`

Una tupla o una lista di due elementi nella forma `(x_min, x_max)` dove `x_min`
è il valore della x all'estrema sinistra della tela e `x_max` è il valore della
x all'estrema destra.

### `range_y`

Una tupla o una lista di due elementi nella forma `(y_min, y_max)` dove `y_min`
è il valore della y all'estrema sinistra della tela e `y_max` è il valore della
y all'estrema destra.

### `colore`

Il colore da utilizzare per tracciare le figure, è di tipo `str`. Questo può
essere il nome di un colore in inglese (es. `black`) oppure un colore come in
CSS nella forma `#XXXXXX` dove al posto di `XXXXXX` c'è un colore esadecimale
(es. `#FF0000` per il rosso).

### `spessore`

Lo spessore della linea con cui sono tracciate le figure, è di tipo `int`, se
ad esempio si mette `2` la linea è tracciata con uno spessore di 2 pixel. Questo
metodo non prende argomenti.

## Metodi

### `w`

Restituisce la larghezza in pixel della `Tela`, non prende argomenti. Questo
valore dipende dalla `tkinter.Canvas` passata al costruttore. Questo metodo non
prende argomenti.

### `h`

Restituisce l'altezza in pixel della `Tela`, non prende argomenti. Questo valore
dipende dalla `tkinter.Canvas` passata al costruttore.

### `x_tela_a_x_piano(x_tela)`

Prende un valore x sulla tela e lo converte in una x del piano cartesiano. Se
ad esempio il range x è `[0, 10]` e la larghezza della tela è di 500 pixel,
quando si chiama il metodo `tela.x_tela_a_x_piano(250)` viene restituito `5`.
Questo perché `250` è la metà della tela e `5` è a metà tra `0` e `10`.

Questo metodo è il contrario di `x_piano_a_x_tela`.

### `y_tela_a_y_piano(x_tela)`

La stessa cosa di `x_tela_a_x_piano` ma per la y. Questo metodo è il contrario
di `y_piano_a_y_tela`.

### `x_piano_a_x_tela(x_piano)`

Prende un valore x del piano cartesiano e lo converte in una x della tela. Se
ad esempio il range x è `[0, 10]` e la larghezza della tela è di 500 pixel,
quando si chiama il metodo `tela.x_piano_a_x_tela(5)` viene restituito `250`.
Questo perché `5` è a metà tra `0` e `10` e `250` è a metà della tela.

Questo metodo è il contrario di `x_tela_a_x_piano`.

### `y_piano_a_y_tela(x_piano)`

La stessa cosa di `x_piano_a_x_tela` ma per la y. Questo metodo è il contrario
di `y_piano_a_y_tela`.

### `linea(p1, p2)`

![Linea](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/linea.png)

Disegna un segmento sulla tela. Prende i due estremi come argomenti che sono
tuple o liste di lunghezza 2 contenenti numeri interi; i punti sono espressi
come coordinate della tela passata al costruttore. Ad esempio, per disegnare
una linea da A(200, 300) a B(100, 350) si può scrivere
`tela.linea((200, 300), (100, 350))`.

Il colore e lo spessore del segmento sono dettati dagli attributi `colore` e
`spessore`.

Questo metodo non restituisce un valore.

### `linee(punti)`

![Linee](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/linee.png)

Disegna vari segmenti connessi agli estremi. Prende come argomento una lista di
punti; i punti sono espressi come coordinate della tela. Se ad esempio la lista
contiene quattro punti, `p1`, `p2`, `p3` e `p4`, verranno disegnati tre
segmenti: il primo da `p1` a `p2`, il secondo da `p2` a `p3` e il terzo da `p3`
a `p4`.

Come per `linea`, il colore e lo spessore dei segmenti sono dettati dagli
attributi `colore` e `spessore`.

Questo metodo non restituisce un valore.

### `ellisse(p1, p2)`

![Ellisse](https://raw.githubusercontent.com/Classe-4CA-DucaDegliAbruzzi/CalcolatriceGrafica/main/media/ellisse.png)

Disegna l'ellisse inscritta nel rettangolo definito da `p1` e `p2`; i punti sono
espressi come coordinate della tela. `p1` è l'angolo in alto a sinistra del
rettangolo e `p2` è l'angolo in basso a destra.

Il colore e lo spessore dell'ellisse è dettato dagli attributi `colore` e
`spessore`.

Questo metodo non restituisce un valore.

### `disegna_sfondo()`

Disegna le linee del piano sulla tela. È a discrezione del gruppo come queste
cambiano al cambiare di `range_x` e di `range_y`. Queste linee *non seguono*
`colore` e `spessore`. Questo metodo va chiamato prima di disegnare i grafici.

Questo metodo non prende argomenti e non restituisce un valore.

### `disegna_numeri()`

Disegna i numeri che fanno capire il range sulle x e sulle y del piano
cartesiano. Questo metodo va chiamato dopo che sono stati disegnati i grafici.

Questo metodo non prende argomenti e non restituisce un valore.

### `pulisci()`

Ripulisce la tela togliendo tutti gli elementi disegnati.

Questo metodo non prende argomenti e non restituisce un valore.

## Esempi

```python
# `canvas` è un oggetto di tipo tkinter.Canvas
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
