from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk


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
        self.__params: dict[str, None|tk.Entry] = {}
        parti = self.fmt.split("$")
        for parte in parti[1::2]:
            self.__params[parte] = None

    def lista_nomi(self):
        return list(self.__params.keys())

    def crea_widget(self, master):
        parti = self.fmt.split("$")
        frame = ttk.Frame(master)

        for i, parte in enumerate(parti):
            if i % 2 == 0:
                label = ttk.Label(frame, text=parte)
                label.grid(row=0, column=i)
            else:
                entry = ttk.Entry(frame, width=4, justify=tk.RIGHT)
                entry.grid(row=0, column=i)
                self.__params[parte] = entry

        return frame

    def valore(self, key):
        entry = self.__params.get(key)
        if entry is None:
            return None
        try:
            return float(entry.get())
        except ValueError:
            return None

    def validi(self):
        for param in self.lista_nomi():
            if self.valore(param) is None:
                return False
        return True
