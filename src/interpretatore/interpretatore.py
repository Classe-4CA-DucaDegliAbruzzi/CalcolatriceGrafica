from abc import ABC, abstractmethod
from .lexer import ErroreInterpretazione, TipoToken


class NodoBase(ABC):
    @abstractmethod
    def calcola(self, x):
        pass


class NodoBinario(NodoBase):
    def __init__(self, nodo_sx, nodo_dx, op):
        self.nodo_sx = nodo_sx
        self.nodo_dx = nodo_dx
        self.op = op

    def calcola(self, x):
        valore_sx = self.nodo_sx.calcola(x)
        if isinstance(valore_sx, ErroreInterpretazione):
            return valore_sx
        
        valore_dx = self.nodo_dx.calcola(x)
        if isinstance(valore_dx, ErroreInterpretazione):
            return valore_sx

        if self.op.tipo == TipoToken.PIU:
            return valore_sx + valore_dx
        elif self.op.tipo == TipoToken.MENO:
            return valore_sx - valore_dx
        else:
            raise NotImplementedError(f"{self.__class__.__name__} non implementata per {self.op}")


def interpreta_funzione(input_utente, var_ind):
    pass
