import abc 
class BaseGrafico(abc.ABC):
    def __init__(self, tela): 
        self.tela = tela  #è del gruppo 2 e io lo prendo, è un oggetto perché contiene dei valori 
        self.param = self.crea_param()   # io dopo creo un metodo che mi restituisce dei valori che vengono chiamati param 
    @abc.abstractmethod
    def crea_param(): 
        pass
    @abc.abstractmethod
    def disegna(): 
        pass

class BaseGraficoFunzioneY(BaseGrafico, abc.ABC): 
    @abc.abstractmethod
    def crea_param():
        pass
    @abc.abstractmethod
    def funzione(self, y, parametri): #un attributi è diverso dall'argomento della funzione
        pass 
    def disegna(self):
        lista_punti = []
        for y_pixel in range(0, self.tela.h()):
            y_piano = self.tela.y_tela_a_y_piano(y_pixel) #x_tela è uguale a x_piano 
            x_piano = self.funzione(y_piano, {}) 
            x_pixel = self.tela.x_piano_a_x_tela(x_piano)
            punto = (x_pixel, y_pixel)
            y_pixel += 0.00000000000000001
            lista_punti.append(punto)
        self.tela.linee(lista_punti)
