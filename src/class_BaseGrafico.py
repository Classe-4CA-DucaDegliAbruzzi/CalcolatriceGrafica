import abc 
class BaseGrafico(abc.ABC):
    def __init__(self, tela): 
        self.tela = tela 
        self.param = self.crea_param()   # io dopo creo un metodo che mi restituisce dei valori che vengono chiamati param 
    @abc.abstractmethod
    def crea_param(): 
        pass
    @abc.abstractmethod
    def disegna(): 
        pass
