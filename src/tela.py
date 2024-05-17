import tkinter as t

class Tela:
    def __init__(self, canvas):
        self.canvas = canvas
        self.range_x = (-5.0, 5.0)
        self.range_y = (-5.0, 5.0)
        self.colore = "black"
        self.spessore = 1

    def w(self):
        return int(self.canvas.cget("width"))

    def h(self):
        return int(self.canvas.cget("height"))
    
    def x_tela_a_x_piano(self,x_tela):
        return (((x_tela)*(self.range_x[1]-self.range_x[0]))/(self.range_x[1]))+self.range_x[0]

    def y_tela_a_y_piano(self,y_tela):
        return (((y_tela-self.h())*(self.range_y[1]-self.range_y[0]))/(0-self.h()))+self.h()
    
    def x_piano_a_x_tela(self,x_piano):
        return (x_piano-self.range_x[0])*self.w()/(self.range_x[1]-self.range_x[0])
     
    def y_piano_a_y_tela(self,y_piano):
        return ((y_piano-self.range_y[0])/(self.range_y[1]-self.range_y[0]))*(0-self.h())+self.h()
    
    def linea(self,p1, p2):
        self.canvas.create_line(p1[0],p1[1],p2[0],p2[1],width=self.spessore,fill=self.colore)

    def linee(self,punti):
        # Disegna le linee connesse dai punti
        for i in range(len(punti) - 1):
            x1, y1 = punti[i]
            x2, y2 = punti[i + 1]
            self.canvas.create_line(x1, y1, x2, y2,width=self.spessore,fill=self.colore)
    
    def ellisse(self,p1, p2):
        self.canvas.create_oval(p1[0],p1[1],p2[0],p2[1],width=self.spessore,outline=self.colore)
    
    def disegna_sfondo(self):
        pass
    
    def disegna_numeri(self):
        pass
    
    def pulisci(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.grid(column=0,row=0)
    tela = Tela(canvas)

    pulsante_pulisci = tk.Button(root, text="Pulisci", command=tela.pulisci)
    pulsante_pulisci.grid(row=1, column=0)

    tela.colore = "#FF0000"  # rosso
    tela.spessore = 2
    tela.range_x = (-5, 5)
    tela.range_y = (-5, 5)

    # disegna le linee di sfondo
    tela.disegna_sfondo()

    # disegna un segmento da (-3, 2) a (4, 1)
    x1 = tela.x_piano_a_x_tela(0)
    y1 = tela.y_piano_a_y_tela(0)

    x2 = tela.x_piano_a_x_tela(5)
    y2 = tela.y_piano_a_y_tela(5)
    tela.linea((x1, y1), (x2, y2))
    tela.ellisse((100,200),(300,400))
    
     # disegna le linee di sfondo
    tela.disegna_sfondo()   #più difficile

    tela.linee([(50, 50), (100, 150), (200, 100), (300, 200)])

    # disegna i numeri delle linee
    tela.disegna_numeri()
    root.mainloop()

   