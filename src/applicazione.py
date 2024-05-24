from tkinter import *
from tkinter import ttk
from base_grafico import Retta, Parabola, Seno, Coseno, FunzioneX, FunzioneY
from tela import Tela


class Applicazione:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calcolatrice")
        self.root.configure(bg="old lace")
        self.root.geometry('1000x800')
        self.root.columnconfigure(0, weight=1)

        self.tela = None

        self.range_x_min_entry = None
        self.range_x_max_entry = None
        self.range_y_min_entry = None
        self.range_y_max_entry = None

        self.valore_entry = None
        self.funz_da_selezionare = None

        self.funzioni = {
            "y = mx + q": Retta,
            "y = ax^2 + bx + c": Parabola,
            "y = a*sin(wx)": Seno,
            "y = a*cos(wx)": Coseno,
            "y = f(x)": FunzioneX,
            "x = f(y)": FunzioneY
        }

        self.frame_parametri = None
        self.widget_parametri = None
        self.grafico = None
        self.grafico_corrente = ""

        self.crea_ui()
        self.aggiorna()

    def crea_ui(self):
        self.root.columnconfigure(0, weight=1)

        a = Frame(self.root, bg='old lace', height=300, width=500)
        a.grid(column=0, row=0)
        b = Frame(self.root, bg='old lace', height=300, width=500)
        b.grid(column=1, row=0)

        self.funz_da_selezionare = StringVar()
        tendina = ttk.Combobox(a, width=30, background="antique white", textvariable=self.funz_da_selezionare)
        tendina['values'] = list(self.funzioni.keys())
        tendina['state'] = 'readonly'
        tendina.place(x=60, y=63)

        # testi

        self.frame_parametri = Frame(a, bg='old lace')
        self.frame_parametri.place(x=60, y=177)

        text_range = Label(a, text="Range x [       ;       ]", font="Times 13", fg="black", bg="antique white")
        text_range.place(x=60, y=250)
        text_range = Label(a, text="Range y [       ;       ]", font="Times 13", fg="black", bg="antique white")
        text_range.place(x=250, y=250)

        Valorex_funzione = Label(b, text="f(   ) = ", bg="antique white", fg="black", font="Verdana")
        Valorex_funzione.place(x=40, y=175)

        Valorey_funzione = Label(b, text=' ', bg="antique white", fg="black", font="Arial")
        Valorey_funzione.place(x=120, y=175, width=50)

        self.root.columnconfigure(0, weight=0)
        c = Frame(self.root, bg="antique white", height=500, width=500)
        c.grid(row=1, column=0, columnspan=4)

        grafico = Canvas(c, bg="white", width=500, height=500)
        grafico.place(x=0, y=0)
        self.tela = Tela(grafico)
        self.tela.colore = "red"
        self.tela.spessore = 2

        # Input

        self.range_x_min_entry = Entry(a)
        self.range_x_min_entry.insert(0, str(self.tela.range_x[0]))
        self.range_x_max_entry = Entry(a)
        self.range_x_max_entry.insert(0, str(self.tela.range_x[1]))
        self.range_x_min_entry.place(x=129, y=254, width=20)
        self.range_x_max_entry.place(x=162, y=254, width=20)
        self.range_y_min_entry = Entry(a)
        self.range_y_min_entry.insert(0, str(self.tela.range_y[0]))
        self.range_y_max_entry = Entry(a)
        self.range_y_max_entry.insert(0, str(self.tela.range_y[1]))
        self.range_y_min_entry.place(x=319, y=254, width=20)
        self.range_y_max_entry.place(x=352, y=254, width=20)

        valore = IntVar()
        self.valore_entry = Entry(b, textvariable=valore)
        self.valore_entry.place(x=55, y=178, width=18)

        Clean = Button(b, text="Aggiorna", font="Times 15", fg="black", bg="medium sea green", command=self.aggiorna)
        Clean.place(x=40, y=55)

        Imposta = Button(a, text="Imposta", font="Times 15", fg="black", bg="medium sea green", command=self.imposta)
        Imposta.place(x=310, y=55)

    def aggiorna(self):
        try:
            x_min = float(self.range_x_min_entry.get())
            x_max = float(self.range_x_max_entry.get())
            y_min = float(self.range_y_min_entry.get())
            y_max = float(self.range_y_max_entry.get())
            if x_max <= x_min or y_max <= y_min:
                raise ValueError
            self.tela.range_x = (x_min, x_max)
            self.tela.range_y = (y_min, y_max)
        except ValueError:
            pass

        self.tela.pulisci()
        self.tela.disegna_sfondo()
        if self.grafico is not None:
            self.grafico.disegna()
        self.tela.disegna_numeri()

    # imposta
    def imposta(self):
        if self.funz_da_selezionare.get() == "":
            return
        if self.funz_da_selezionare.get() == self.grafico_corrente:
            return

        if self.widget_parametri is not None:
            self.widget_parametri.destroy()
        self.grafico = self.funzioni[self.funz_da_selezionare.get()](self.tela)
        self.widget_parametri = self.grafico.param.crea_widget(self.frame_parametri)
        self.widget_parametri.pack()
        self.grafico_corrente = self.funz_da_selezionare.get()

    def run(self):
        self.root.mainloop()
