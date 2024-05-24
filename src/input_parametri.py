from abc import ABC, abstractmethod
import tkinter as t
from interpretatore import interpreta_funzione, ErroreInterpretazione


class BaseInputParametri(ABC):
    def __init__(self, fmt):
        self.fmt = fmt
        
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
        self.parti = fmt.split('$')
        self.dictionary = {}
        for i in self.parti[1::2]:
            self.dictionary[i] = None

    def lista_nomi(self):
        return list(self.dictionary.keys())

    def crea_widget(self, master):
        frame = t.Frame(master, padx=10, pady=10)
        for i, parte in enumerate(self.parti):
            if i % 2 == 0:
                label_input_sosa1 = t.Label(frame, text=parte)
                label_input_sosa1.grid(row=0, column=i, sticky='w')
            else:
                entry_sosa1 = t.Entry(frame, width=8)
                entry_sosa1.grid(row=0, column=i, padx=5,pady=5)
                self.dictionary[parte] = entry_sosa1
        return frame
        
    def valore(self, key):
        if key in self.dictionary:
            try:
                return float(self.dictionary[key].get())
            except ValueError:
                return None
        return None

    def validi(self):
        for entry in self.dictionary.values():
            if entry is None:
                return False
            try:
                float(entry.get())
            except ValueError:
                return False
        return True


class InputFunzione(BaseInputParametri):
    def __init__(self, fmt):
        super().__init__(fmt)
        self.__prev_func = ""
        self.__func = None
        self.__func_entry = None
        self.__entry = None

    def lista_nomi(self):
        return []
        
    def crea_widget(self, master):
        frame = t.Frame(master, padx=10, pady=10)
        label_input_sosa = t.Label(frame, text='f(' + self.fmt + ') =')
        label_input_sosa.grid(row=0, column=0, sticky="w")
        self.__entry = t.Entry(frame, width=40)
        self.__entry.grid(row=0, column=1, padx=5, pady=5)
        return frame

    def __update_func(self):
        if self.__entry is None:
            return
        if self.__entry.get() == self.__prev_func:
            return self.__func
        self.__func = interpreta_funzione(self.__entry.get(), self.fmt)
        if isinstance(self.__func, ErroreInterpretazione):
            self.__func = None
        self.__prev_func = self.__entry.get()
    
    def valore(self,x):
        if not self.validi():
            return None
        return self.__func.calcola(x)

    def validi(self):
        if self.__entry is None:
            return False
        self.__update_func()
        return self.__func is not None
