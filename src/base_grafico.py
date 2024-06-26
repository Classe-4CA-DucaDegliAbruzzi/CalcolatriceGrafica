"""
Autrici: Emma Rossi, Alessia Ciocan
"""

import abc
import math
from input_parametri import InputCaselle, InputFunzione


class BaseGrafico(abc.ABC):
    def __init__(self, tela):
        self.tela = tela
        self.param = self.crea_param()  # metodo che mi restituisce l'input dei parametri

    @abc.abstractmethod
    def crea_param(self):
        pass

    @abc.abstractmethod
    def disegna(self):
        pass


class BaseGraficoFunzioneX(BaseGrafico, abc.ABC):
    @abc.abstractmethod
    def crea_param(self):
        pass

    @abc.abstractmethod
    def funzione(self, x, parametri):
        pass

    def disegna(self):
        if not self.param.validi():
            return

        lista_nomi = self.param.lista_nomi()
        dizionario = {}  # questo dizionario associa i nome dei parametro al suo valore
        for nome in lista_nomi:
            dizionario[nome] = self.param.valore(nome)

        lista_punti = []
        for x_pixel in range(0, self.tela.w()):
            x_piano = self.tela.x_tela_a_x_piano(x_pixel)  # x_tela è uguale a x_pixel
            y_piano = self.funzione(x_piano, dizionario)
            y_pixel = self.tela.y_piano_a_y_tela(y_piano)
            punto = (x_pixel, y_pixel)
            lista_punti.append(punto)
        self.tela.linee(lista_punti)


class BaseGraficoFunzioneY(BaseGrafico, abc.ABC):
    @abc.abstractmethod
    def crea_param(self):
        pass

    @abc.abstractmethod
    def funzione(self, y, parametri):
        pass

    def disegna(self):
        if not self.param.validi():
            return 

        lista_nomi = self.param.lista_nomi()
        dizionario = {}  # questo dizionario associa i nome dei parametro al suo valore
        for nome in lista_nomi:
            dizionario[nome] = self.param.valore(nome)

        lista_punti = []
        for y_pixel in range(0, self.tela.h()):
            y_piano = self.tela.y_tela_a_y_piano(y_pixel)  # y_tela è uguale a y_pixel
            x_piano = self.funzione(y_piano, dizionario)
            x_pixel = self.tela.x_piano_a_x_tela(x_piano)
            punto = (x_pixel, y_pixel)
            lista_punti.append(punto)
        self.tela.linee(lista_punti)
    

class Parabola(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputCaselle("y = $a$x^2 + $b$x + $c$")

    def funzione(self, x, parametri):
        a = parametri["a"]
        b = parametri["b"]
        c = parametri["c"]
        return a * x**2 + b * x + c


class Retta(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputCaselle("y = $m$x + $q$")

    def funzione(self, x, parametri):
        m = parametri["m"]
        q = parametri["q"]
        return m * x + q


class FunzioneX(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputFunzione("x")

    def funzione(self, x, parametri):
        return self.param.valore(x)


class FunzioneY(BaseGraficoFunzioneY):
    def crea_param(self):
        return InputFunzione("y")

    def funzione(self, y, parametri):
        return self.param.valore(y)


class Seno(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputCaselle("y = $a$ * sin($w$ * x)")

    def funzione(self, x, parametri):
        a = parametri["a"]
        w = parametri["w"]
        return a * math.sin(w * x)


class Coseno(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputCaselle("y = $a$ * cos($w$ * x)")

    def funzione(self, x, parametri):
        a = parametri["a"]
        w = parametri["w"]
        return a * math.cos(w * x)


if __name__ == "__main__":
    import tkinter as tk
    from tela import Tela


    class GraficoSenzaParametri(BaseGraficoFunzioneX):
        def crea_param(self):
            return InputCaselle("")

        def funzione(self, x, parametri):
            return x * x  # disegna y = x^2


    root = tk.Tk()

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.grid(row=0, column=0)
    tela_ = Tela(canvas)
    grafico = GraficoSenzaParametri(tela_)

    tela_.disegna_sfondo()
    grafico.disegna()

    root.mainloop()
