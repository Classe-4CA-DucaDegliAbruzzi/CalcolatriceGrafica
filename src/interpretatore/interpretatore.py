from abc import ABC, abstractmethod
from .lexer import ErroreInterpretazione


class NodoBase(ABC):
    @abstractmethod
    def calcola(self, x):
        pass


def interpreta_funzione(input_utente, var_ind):
    pass
