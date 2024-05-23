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
        self.dizionary = {}

    def lista_nomi(self):
        return

    def crea_widget(self, master):
        
       frame1 = t.Frame(master, padx=10, pady=10)
       frame1.pack()
       label_input_sosa_y= t.Label(frame1, text='y=')
       label_input_sosa_y.grid(row=0, column=0, sticky="w")
       entry_sosa_y = t.Entry(frame1, width=8)
       entry_sosa_y.grid(row=0, column=1, padx=5, pady=5)
       label_input_sosa_a= t.Label(frame1, text='x^2 +')
       label_input_sosa_a.grid(row=0, column=2, sticky="w")
       entry_sosa_a = t.Entry(frame1, width=8)
       entry_sosa_a.grid(row=0, column=3, padx=5, pady=5)
       label_input_sosa_b= t.Label(frame1, text='x +')
       label_input_sosa_b.grid(row=0, column=4, sticky="w")
       entry_sosa_b = t.Entry(frame1, width=8)
       entry_sosa_b.grid(row=0, column=5, padx=5, pady=5)
       master.mainloop()



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
        
