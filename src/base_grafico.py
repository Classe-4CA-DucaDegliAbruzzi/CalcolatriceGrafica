import abc


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
        lista_punti = []
        for x_pixel in range(0, self.tela.w()):
            x_piano = self.tela.x_tela_a_x_piano(x_pixel)  # x_tela è uguale a x_pixel
            y_piano = self.funzione(x_piano, {})
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
        lista_punti = []
        for y_pixel in range(0, self.tela.h()):
            y_piano = self.tela.y_tela_a_y_piano(y_pixel)  # y_tela è uguale a y_pixel
            x_piano = self.funzione(y_piano, {})
            x_pixel = self.tela.x_piano_a_x_tela(x_piano)
            punto = (x_pixel, y_pixel)
            lista_punti.append(punto)
        self.tela.linee(lista_punti)
