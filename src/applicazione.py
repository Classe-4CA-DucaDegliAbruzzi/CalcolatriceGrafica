from tkinter import *
from tkinter import ttk
from base_grafico import Retta, Parabola, Seno, Coseno, FunzioneX, FunzioneY
from tela import Tela
from input_parametri import InputFunzione


class Applicazione:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calcolatrice")
        self.root.resizable(False, False)

        self.tela = None

        self.range_x_min_entry = None
        self.range_x_max_entry = None
        self.range_y_min_entry = None
        self.range_y_max_entry = None

        self.valore_entry = None
        self.valore_label = None
        self.funz_da_selezionare = None

        self.funzioni = {
            "y = mx + q": Retta,
            "y = ax^2 + bx + c": Parabola,
            "y = a*sin(wx)": Seno,
            "y = a*cos(wx)": Coseno,
            "y = f(x)": FunzioneX,
            "x = f(y)": FunzioneY
        }

        self.grafico_default = "y = mx + q"

        self.frame_parametri = None
        self.widget_parametri = None
        self.grafico = None
        self.grafico_corrente = ""

        self.frame_argomento_funz = None

        self.crea_ui()
        self.aggiorna()

    def crea_ui(self):
        self.root.columnconfigure(0, weight=1)

        controlli = ttk.Frame(self.root)
        controlli.grid(row=0, column=0, sticky=EW)
        controlli.columnconfigure(0, weight=1)

        grafico = Canvas(self.root, bg="white", width=500, height=500)
        grafico.grid(row=1, column=0)
        self.tela = Tela(grafico)
        self.tela.colore = "red"
        self.tela.spessore = 2

        prima_riga = ttk.Frame(controlli)
        prima_riga.grid(row=0, column=0, sticky=EW)
        prima_riga.columnconfigure(0, weight=0)
        prima_riga.columnconfigure(1, weight=0)
        prima_riga.columnconfigure(2, weight=1)

        self.funz_da_selezionare = ttk.Combobox(
            prima_riga,
            width=30,
            values=list(self.funzioni.keys())
        )
        self.funz_da_selezionare.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.funz_da_selezionare.insert(0, self.grafico_default)
        self.funz_da_selezionare["state"] = "readonly"

        ttk.Button(
            prima_riga,
            text="Imposta",
            command=self.imposta
        ).grid(row=0, column=1, sticky=W, padx=5, pady=2)

        ttk.Button(
            prima_riga,
            text="Aggiorna",
            command=self.aggiorna
        ).grid(row=0, column=2, sticky=E, padx=5, pady=2)

        seconda_riga = ttk.Frame(controlli)
        seconda_riga.grid(row=1, column=0, sticky=EW)

        self.frame_parametri = ttk.Frame(seconda_riga)
        self.frame_parametri.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.frame_argomento_funz = ttk.Frame(seconda_riga)
        self.frame_argomento_funz.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        ttk.Label(self.frame_argomento_funz, text="f(").pack(side=LEFT)
        self.valore_entry = ttk.Entry(self.frame_argomento_funz, width=3, justify=RIGHT)
        self.valore_entry.pack(side=LEFT)
        ttk.Label(self.frame_argomento_funz, text=") =").pack(side=LEFT)
        self.valore_label = ttk.Label(self.frame_argomento_funz, text="")
        self.valore_label.pack(side=LEFT)
        self.imposta()

        terza_riga = ttk.Frame(controlli)
        terza_riga.grid(row=2, column=0, pady=2)

        self.range_x_min_entry = ttk.Entry(terza_riga, width=4, justify=RIGHT)
        self.range_x_min_entry.insert(0, str(self.tela.range_x[0]))
        self.range_x_max_entry = ttk.Entry(terza_riga, width=4, justify=RIGHT)
        self.range_x_max_entry.insert(0, str(self.tela.range_x[1]))
        self.range_y_min_entry = ttk.Entry(terza_riga, width=4, justify=RIGHT)
        self.range_y_min_entry.insert(0, str(self.tela.range_y[0]))
        self.range_y_max_entry = ttk.Entry(terza_riga, width=4, justify=RIGHT)
        self.range_y_max_entry.insert(0, str(self.tela.range_y[1]))

        ttk.Label(terza_riga, text="Range x [").pack(side=LEFT)
        self.range_x_min_entry.pack(side=LEFT)
        ttk.Label(terza_riga, text=";").pack(side=LEFT)
        self.range_x_max_entry.pack(side=LEFT)
        ttk.Label(terza_riga, text="]             Range y [").pack(side=LEFT)
        self.range_y_min_entry.pack(side=LEFT)
        ttk.Label(terza_riga, text=";").pack(side=LEFT)
        self.range_y_max_entry.pack(side=LEFT)
        ttk.Label(terza_riga, text="]").pack(side=LEFT)

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

        if self.grafico and isinstance(self.grafico.param, InputFunzione):
            try:
                val = float(self.valore_entry.get())
            except ValueError:
                return
            risultato = self.grafico.param.valore(val)
            if risultato is None:
                return
            self.valore_label.configure(text=str(risultato))

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

        if isinstance(self.grafico.param, InputFunzione):
            self.frame_argomento_funz.grid(column=1, row=0)
        else:
            self.frame_argomento_funz.grid_forget()

    def run(self):
        self.root.mainloop()
