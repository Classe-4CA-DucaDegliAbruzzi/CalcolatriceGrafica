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
        self.parti = fmt.split('$')
        self.dictionary = {}
        for i in self.parti[1::2]:
            self.dictionary[i]=None

    def lista_nomi(self):
        return list(self.dictionary.keys())

    def crea_widget(self, master):
        frame = t.Frame(master, padx=10, pady=10)
        for i, parte in enumerate(self.parti):
            if i %2 == 0:
                label_input_sosa1 = t.Label(frame, text=parte)
                label_input_sosa1.grid(row=0, column=i, sticky='w')
            else:
                entry_sosa1 = t.Entry(frame, width=8)
                entry_sosa1.grid(row=0, column=i, padx=5,pady=5)
                self.dictionary[parte]=entry_sosa1
        return frame
        
    def valore(self, key):
        if key in self.dizionary:
            return self.dizionary[key].get()
        return None

    def validi(self):
        for entry in self.dizionary.values():
            try:
                float(entry.get())
            except ValueError:
                return False
        return True


class InputFunzione(BaseInputParametri):
    def __init__(self):
        super().__init__(fmt)

    def lista_nomi(self):
        return []
        

    def crea_widget(self, master):

        def no_one_f_with_sosa(self):
            read_sosa = entry_sosa.get()
            interpreta_funzione(read_sosa)

        frame = t.Frame(master, padx=10, pady=10)
        frame.pack()
        label_input_sosa= t.Label(frame, text=fmt)
        label_input_sosa.grid(row=0, column=0, sticky="w")
        entry_sosa = t.Entry(frame, width=40)
        entry_sosa.grid(row=0, column=1, padx=5, pady=5)
        entry_funzione.bind('<Return>', no_one_f_with_sosa)
        
        master.mainloop()
        
    def valore(self,x):
        if not self.validi():
            return None

    def validi(self):
        return
        
