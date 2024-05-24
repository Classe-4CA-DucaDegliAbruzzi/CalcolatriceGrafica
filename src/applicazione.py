from tkinter import * #type: ignore
from tkinter import ttk
import os
from PIL import ImageTk, Image

folder_path = os.path.dirname(__file__)
image_path = os.path.join(folder_path, 'button_finale.png')


class Applicazione:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calcolatrice")
        self.root.configure(bg="old lace")
        self.root.geometry('1000x750')
        self.root.columnconfigure(0, weight=1)

        self.range_x1_entry = None
        self.range_x2_entry = None
        self.valore_entry = None
        self.funz_entry = None
        self.funz_da_selezionare = None

        self.crea_ui()

    def crea_ui(self):
        self.root.columnconfigure(0, weight=1)

        a = Frame(self.root, bg='old lace', height=300, width=500)
        a.grid(column=0, row=0)
        b = Frame(self.root, bg='old lace', height=300, width=500)
        b.grid(column=1, row=0)

        funz = StringVar()
        self.funz_entry = Entry(a, textvariable=funz)
        self.funz_entry.place(x=122, y=180)

        self.funz_da_selezionare = StringVar()
        tendina = ttk.Combobox(a, width=30, background="antique white", textvariable=self.funz_da_selezionare)
        tendina['values'] = ["esponenziale", "logaritmo", "parabola", "retta", "sin", "cos", "tan"]
        tendina['state'] = 'readonly'
        tendina.place(x=60, y=63)

        # testi

        funzione = Label(a, text="f(x) = ", bg="antique white", fg="black", font="Verdana")
        funzione.place(x=60, y=177)
        text_range = Label(a, text="Range of x [       ;       ]", font="Times 13", fg="black", bg="antique white")
        text_range.place(x=60, y=250)

        Valorex_funzione = Label(b, text="f(   ) = ", bg="antique white", fg="black", font="Verdana")
        Valorex_funzione.place(x=40, y=175)

        Valorey_funzione = Label(b, text=' ', bg="antique white", fg="black", font="Arial")
        Valorey_funzione.place(x=120, y=175, width=50)

        self.root.columnconfigure(0, weight=0)
        c = Frame(self.root, bg="antique white", height=400, width=500)
        c.grid(row=1, column=0, columnspan=4)

        grafico = Canvas(c, bg="white", width=700, height=500)
        grafico.place(x=0, y=0)

        testo_grafico = Label(c, text="Il tuo grafico verrà visualizzato qui", font="Times", bg="white", fg="black")
        testo_grafico.place(x=150, y=200)

        # Input

        range_x1 = IntVar()
        range_x2 = IntVar()
        self.range_x1_entry = Entry(a, textvariable=range_x1)
        self.range_x2_entry = Entry(a, textvariable=range_x2)
        self.range_x1_entry.place(x=149, y=254, width=20)
        self.range_x2_entry.place(x=182, y=254, width=20)

        valore = IntVar()
        self.valore_entry = Entry(b, textvariable=valore)
        self.valore_entry.place(x=55, y=178, width=18)

        Clean = Button(b, text="Clean", font="Times 15", fg="black", bg="medium sea green", command=self.aggiorna)
        Clean.place(x=40, y=55)

        Imposta = Button(a, text="Set Up", font="Times 15", fg="black", bg="medium sea green", command=self.imposta)
        Imposta.place(x=310, y=55)

    def aggiorna(self):
        self.funz_entry.delete(first=0, last='end')
        self.funz_entry.focus()
        self.range_x1_entry.delete(first=0, last='end')
        self.range_x2_entry.delete(first=0, last='end')
        self.valore_entry.delete(first=0, last='end')

    # imposta
    def imposta(self):
        # cancella il contenuto di funz_entry
        self.funz_entry.delete(0, END)

        if self.funz_da_selezionare.get() == 'retta':
            self.funz_entry.insert(0, 'a*x+b')
        elif self.funz_da_selezionare.get() == 'parabola':
            self.funz_entry.insert(0, 'a*x^2+b*x+c')
        elif self.funz_da_selezionare.get() == 'esponenziale':
            self.funz_entry.insert(0, 'a^x+b')
        elif self.funz_da_selezionare.get() == 'sin':
            self.funz_entry.insert(0, 'a*sin(x)+b')
        elif self.funz_da_selezionare.get() == 'cos':
            self.funz_entry.insert(0, 'a*cos(x)+b')
        elif self.funz_da_selezionare.get() == 'tan':
            self.funz_entry.insert(0, 'a*tan(x)+b')
        elif self.funz_da_selezionare.get() == 'logaritmo':
            self.funz_entry.insert(0, "a*log[b](x)+c")

    def run(self):
        self.root.mainloop()


"""
App = Application()



def open_calc():
    App.main()

win= Tk()
win.title("Calcolatrice_Grafica_4CA")
win.configure(bg="antique white")
win.geometry("750x750")


#title 4ca


classe = Label(win, text="4 CA", font="Georgia 115", fg="maroon", bg="antique white")
classe.place(x=215, y = 10)


play_button= ImageTk.PhotoImage(Image.open(image_path))
img_label= ttk.Label(image=play_button)
button= Button(win, image=play_button, borderwidth=0, command=open_calc, cursor="pirate")
button.place(x=275, y=200)


win.mainloop()

"""
