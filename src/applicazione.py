from tkinter import * #type: ignore
from tkinter import ttk

class Application:
    def main(self):
        #win.destroy()
        r = Tk()
        r.title("calcolatrice")
        r.configure(bg="antique white")
        r.geometry('1000x750')
       
        r.columnconfigure(0, weight=1)

       
        a = Frame(r, bg='antique white', height=300, width=500)
        a.grid(column=0, row=0)
        b = Frame(r, bg='antique white', height=300, width=500)
        b.grid(column=1, row=0)
       
       
        funz = StringVar()
        funz_entry = Entry(a, textvariable=funz)
        funz_entry.place(x=122, y=180)

        funz_da_selezionare = StringVar()
        tendina = ttk.Combobox(a, width=30, background="antique white", textvariable=funz_da_selezionare)
        tendina['values']=["esponenziale","logaritmo", "parabola", "retta", "sin", "cos", "tan"]
        tendina['state']='readonly'
        tendina.place(x = 60, y = 63)

        #testi

        funzione = Label(a, text="f(x) = ", bg="antique white", fg="black", font="Verdana")
        funzione.place(x=60, y=177)
        text_range= Label(a, text="Range of x [       ;       ]",font="Times 13", fg="black", bg="antique white")
        text_range.place(x=60, y=250)


        Valorex_funzione = Label(b, text="f(   ) = ", bg="antique white", fg="black", font="Verdana")
        Valorex_funzione.place(x=40, y=175)

        Valorey_funzione = Label(b, text=' ', bg="antique white", fg="black", font="Arial")
        Valorey_funzione.place(x=120, y=175, width=50)
       
        r.columnconfigure(0, weight=0)
        c = Frame(r, bg="antique white", height=400, width=500)
        c.grid(row=1, column=0, columnspan=4)

        grafico=Canvas(c, bg="white", width=700, height=500)
        grafico.place(x=0, y=0)

        testo_grafico = Label(c, text="Il tuo grafico verrà visualizzato qui",font="Times", bg="white", fg="black")
        testo_grafico.place(x=150, y=200)

        #Input

        range_x1 = IntVar()
        range_x2 = IntVar()
        range_x1_entry = Entry(a, textvariable=range_x1)
        range_x2_entry = Entry(a, textvariable=range_x2)
        range_x1_entry.place(x=149 ,y=254, width=20)
        range_x2_entry.place(x=182, y=254, width=20)


        valore= IntVar()
        valore_entry = Entry(b, textvariable=valore)
        valore_entry.place(x=55, y=178, width=18)
       
       

        #Aggiorna
        def aggiorna():
            funz_entry.delete(first=0, last='end')
            funz_entry.focus()
            range_x1_entry.delete(first=0, last='end')
            range_x1_entry.focus()
            range_x2_entry.delete(first=0, last='end')
            range_x2_entry.focus()
            valore_entry.delete(first=0, last='end')
            valore_entry.focus()
            #grafico.delete()
            #grafico.focus()

       
        Clean = Button(b, text="Clean",font="Times 15", fg="black", bg="mediumorchid", command=aggiorna)
        Clean.place(x=40, y=55)

        #imposta
        def imposta():
            # cancella il contenuto di funz_entry
            funz_entry.delete(0, END)


            if funz_da_selezionare.get()=='retta':
                funz_entry.insert(0, 'a*x+b')
            elif funz_da_selezionare.get()=='parabola':
                funz_entry.insert(0, 'a*x^2+b*x+c')
            elif funz_da_selezionare.get()=='esponenziale':
                funz_entry.insert(0, 'a^x+b')
            elif funz_da_selezionare.get()=='sin':
                funz_entry.insert(0, 'a*sin(x)+b')
            elif funz_da_selezionare.get()=='cos':
                funz_entry.insert(0, 'a*cos(x)+b')
            elif funz_da_selezionare.get()=='tan':
                funz_entry.insert(0, 'a*tan(x)+b')
            elif funz_da_selezionare.get()=='logaritmo':
                funz_entry.insert(0, "a*log[b](x)+c")


        Imposta = Button(a,text="Set Up", font="Times 15", fg ="black" , bg = "mediumorchid",command=imposta)
        Imposta.place(x=310, y=55)


        r.mainloop()

App = Application()
App.main()

'''
def open_calc():
    main()

win= Tk()
win.title("Calcolatrice_Grafica_4CA")
win.configure(bg="antique white")
win.geometry("750x750")


#title 4ca


classe = Label(win, text="4 CA", font="Georgia 115", fg="maroon", bg="antique white")
classe.place(x=250, y = 10)


play_button=PhotoImage(file="button_finale.png")
img_label= ttk.Label(image=play_button)
button= Button(win, image=play_button, borderwidth=0, command=open_calc, cursor="pirate")
button.place(x=275, y=200)


win.mainloop()
'''


