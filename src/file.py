from abc import ABC, abstractmethod
import tkinter as t

class BaseInputParametri(ABC):
    def __init__(self, fmt):
        self.fmt=fmt
        
    @abstractmethod
    def lista_nomi(self):
        pass
    
    @abstractmethod
    def crea_widget(self, master):
        pass
    
    @abstractmethod
    def valore(self, key):
        pass

    @abstractmethod
    def validi(self):
        pass
    
        
class InputCaselle(BaseInputParametri):
    def __init__(self, fmt):
        super().__init__(fmt)

    def lista_nomi(self):

    def crea_widget(self, master):
        Frame = t.Frame(master)

    def valore(self, key):

    def validi(self):

class InputFunzione(BaseInputParametri):
    def __init__(self):
        super().__init__(fmt)

    def lista_nomi(self):
        return ""

    def crea_widget(self, master):

    def valore(self,x):
        if not self.validi():
            return None

    def validi(self):
        
        
        
        
