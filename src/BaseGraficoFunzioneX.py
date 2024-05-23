import abc 
#NB TUTTO QUELLO CHE E' SCRITTO QUI E' SBAGLIATO 
# FARE RIFERIMENTO A BASE GRAFICO 
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

class BaseGraficoFunzioneX(BaseGrafico, abc.ABC): 
    @abc.abstractmethod
    def crea_param():
        pass
    @abc.abstractmethod
    def funzione(self, x, parametri): #un attributi è diverso dall'argomento della funzione
        pass 
    def disegna(self):
        lista_punti = []
        for x_pixel in range(0, self.tela.w()):
            x_piano = self.tela.x_tela_a_x_piano(x_pixel) #x_tela è uguale a x_piano 
            y_piano = self.funzione(x_piano, {}) 
            y_pixel = self.tela.y_piano_a_y_tela(y_piano)
            punto = (x_pixel, y_pixel)
            x_pixel += 0.00000000000000001
            lista_punti.append(punto)
        self.tela.linee(lista_punti)

