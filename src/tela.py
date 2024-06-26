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
    
    def x_tela_a_x_piano(self, x_tela):
        return ((x_tela*(self.range_x[1]-self.range_x[0]))/self.w())+self.range_x[0]

    def y_tela_a_y_piano(self, y_tela):
        return (((y_tela-self.h())*(self.range_y[1]-self.range_y[0]))/(-self.h()))+self.range_y[0]
    
    def x_piano_a_x_tela(self, x_piano):
        return (x_piano-self.range_x[0])*self.w()/(self.range_x[1]-self.range_x[0])
     
    def y_piano_a_y_tela(self, y_piano):
        return ((y_piano-self.range_y[0])/(self.range_y[1]-self.range_y[0]))*(0-self.h())+self.h()

    def linea(self, p1, p2):
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], width=self.spessore, fill=self.colore)

    def linee(self, punti):
        # Disegna le linee connesse dai punti
        for i in range(len(punti) - 1):
            x1, y1 = punti[i]
            x2, y2 = punti[i + 1]
            self.linea((x1, y1), (x2, y2))
    
    def ellisse(self, p1, p2):
        self.canvas.create_oval(p1[0], p1[1], p2[0], p2[1], width=self.spessore, outline=self.colore)
    
    def disegna_sfondo(self):
        
        prev_spessore = self.spessore
        prev_colore = self.colore
        
        self.colore = "grey"
        self.spessore = 1
        
        # Disegna linee per ogni unità intera del piano
        for i in range(int(self.range_x[0]) - 1, int(self.range_x[1]) + 1):
            x = self.x_piano_a_x_tela(i)
            y_start = self.y_piano_a_y_tela(self.range_y[0])
            y_end = self.y_piano_a_y_tela(self.range_y[1])
            self.linea((x, y_start), (x, y_end))
        
        for i in range(int(self.range_y[0]) - 1, int(self.range_y[1]) + 1):
            y = self.y_piano_a_y_tela(i)
            x_start = self.x_piano_a_x_tela(self.range_x[0])
            x_end = self.x_piano_a_x_tela(self.range_x[1])
            self.linea((x_start, y), (x_end, y))

        self.colore = "black"
        self.spessore = 2
        # Disegna assi x e y
        x_assi_start = (0, self.y_piano_a_y_tela(0))
        x_assi_end = (self.w(), self.y_piano_a_y_tela(0))
        self.linea(x_assi_start, x_assi_end)

        y_assi_start = (self.x_piano_a_x_tela(0), 0)
        y_assi_end = (self.x_piano_a_x_tela(0), self.h())
        self.linea(y_assi_start, y_assi_end)

        self.colore = prev_colore
        self.spessore = prev_spessore

    def disegna_numeri(self):
        # Disegna i numeri nell'asse x
        for i in range(int(self.range_x[0]), int(self.range_x[1]) + 1):
            if i != 0:
                x = self.x_piano_a_x_tela(i)
                y = self.y_piano_a_y_tela(0)
                self.canvas.create_text(x, y + 10, text=str(i), fill="black")
        
        # Disegna i numeri nell'asse y
        for i in range(int(self.range_y[0]), int(self.range_y[1]) + 1):
            if i != 0:
                x = self.x_piano_a_x_tela(0)
                y = self.y_piano_a_y_tela(i)
                self.canvas.create_text(x - 10, y, text=str(i), fill="black")
        
        # Disegna lo zero
        x0 = self.x_piano_a_x_tela(0)
        y0 = self.y_piano_a_y_tela(0)
        self.canvas.create_text(x0 - 10, y0 + 10, text="0", fill="black")
    
    def pulisci(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    import tkinter as tk
    
    root = tk.Tk()
    canvas_ = tk.Canvas(root, width=500, height=500)
    canvas_.grid(column=0, row=0)
    tela = Tela(canvas_)

    pulsante_pulisci = tk.Button(root, text="Pulisci", command=tela.pulisci)
    pulsante_pulisci.grid(row=1, column=0)

    tela.colore = "#FF0000"  # rosso
    tela.spessore = 2
    tela.range_x = (-5.5, 5.5)
    tela.range_y = (-5.5, 5.5)

    # disegna le linee di sfondo
    tela.disegna_sfondo()

    # disegna un segmento da (-3, 2) a (4, 1)
    x1_ = tela.x_piano_a_x_tela(0)
    y1_ = tela.y_piano_a_y_tela(0)

    x2_ = tela.x_piano_a_x_tela(5)
    y2_ = tela.y_piano_a_y_tela(5)
    tela.linea((x1_, y1_), (x2_, y2_))
    
    # disegna un'ellisse
    tela.ellisse((100, 200), (300, 400))

    # disegna una serie di linee connesse
    tela.linee([(50, 50), (100, 150), (200, 100), (300, 200)])

    # disegna i numeri delle linee
    tela.disegna_numeri()
    
    root.mainloop()
