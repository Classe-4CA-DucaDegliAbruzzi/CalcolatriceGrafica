"""
Precedenza operatori:

__root__: signed_expr
signed_expr: signed_factor [('+' | '-') factor]
expr: factor [('+' | '-') factor]
signed_factor: signed_implied_mul [('*' | '/') implied_mul]
factor: implied_mul [('*' | '/') implied_mul]
signed_implied_mul: signed_power [power]
implied_mul: power [power]
signed_power: signed_value ['^' value]
power: value ['^' value]
signed_value: ('+' | '-')? power
value: literal | '(' signed_expr ')'
literal: num_literal | 'pi' | 'e' | 'x' | func_call
base_arg_func_call: base_arg_func_name ('_' value)? call_argument
one_arg_func_call: one_arg_func_name call_argument
base_arg_func_name: 'rt' | 'log'
call_argument: '(' signed_expr ')' | implied_mul
one_arg_func_name: 'sin' | 'cos' | 'tan' | 'arcsin' | 'arccos' | 'arctan' | 'sqrt' | 'ln'
num_literal: (0-9)+ ['.' (0-9)+]
"""

from abc import ABC, abstractmethod
import math
from .lexer import ErroreInterpretazione, TipoToken, Token

FUNZIONI = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'arcsin': math.asin,
    'arccos': math.acos,
    'arctan': math.atan,
    'sqrt': math.sqrt,
    'ln': math.log,
    'abs': abs,
    'sign': lambda x: -1 if x < 0 else 1 if x > 0 else 0,
    'rt': lambda num, index=2: num ** (1 / index),
    'log': math.log
}

FUNZIONI_CON_BASE = {'rt', 'log'}


class NodoBase(ABC):
    @abstractmethod
    def calcola(self, x):
        pass

    def __repr__(self):
        attrs = list(self.__dict__.keys())
        attrs = [f"{attr}: {getattr(self, attr)}" for attr in attrs if not attr.startswith("__")]
        return self.__class__.__name__ + "(" + ", ".join(attrs) + ")"


class NodoVar(NodoBase):
    def calcola(self, x):
        return x


class NodoValore(NodoBase):
    def __init__(self, valore):
        self.valore = valore

    def calcola(self, x):
        return self.valore


class NodoNeg(NodoBase):
    def __init__(self, valore: NodoBase):
        self.valore = valore

    def calcola(self, x):
        valore = self.valore.calcola(x)
        if valore is None:
            return None
        return -valore


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

        if self.op == TipoToken.PIU:
            return valore_sx + valore_dx
        elif self.op == TipoToken.MENO:
            return valore_sx - valore_dx
        elif self.op == TipoToken.PER:
            return valore_sx * valore_dx
        elif self.op == TipoToken.DIVISO:
            if valore_dx == 0:
                return None
            return valore_sx / valore_dx
        elif self.op == TipoToken.POTENZA:
            if valore_sx == valore_dx == 0:
                return None
            try:  # pow a differenza di ** non crea numeri complessi
                risultato = math.pow(valore_sx, valore_dx)
            except ValueError:
                return None
            return risultato
        else:
            raise NotImplementedError(f"{self.__class__.__name__} non implementata per {self.op}")


class NodoFunzione(NodoBase):
    def __init__(self, nome_funzione, argomento: NodoBase, base: NodoBase | None = None):
        self.nome_funzione = nome_funzione
        self.argomento = argomento
        self.base = base

    def calcola(self, x):
        funzione = FUNZIONI.get(self.nome_funzione)
        if funzione is None:
            raise NotImplementedError(f"funzione {self.nome_funzione} non implementata")
        argomento = self.argomento.calcola(x)
        if argomento is None:
            return argomento
        try:
            if self.base is None:
                return funzione(argomento)
            base = self.base.calcola(x)
            if base is None:
                return None
            return funzione(argomento, base)
        except (ZeroDivisionError, ValueError):
            return None
        except Exception as e:
            print(f"unhandled exception: {e}")
            return None


class Parser:
    def __init__(self, lista_token, var_ind):
        self.lista_token = lista_token
        self.var_ind = var_ind
        self.idx = 0

    def avanti(self):
        self.idx += 1

    @property
    def tok(self) -> Token:
        return self.lista_token[self.idx]

    def interpreta(self):
        expr = self.expr(True)
        if isinstance(expr, ErroreInterpretazione):
            return expr
        if self.tok != TipoToken.FINE_FUNZIONE:
            return ErroreInterpretazione("funzione non valida")

    def expr(self, signed):
        nodo_sx = self.factor(signed)
        if isinstance(nodo_sx, ErroreInterpretazione):
            return nodo_sx

        while self.tok in (TipoToken.PIU, TipoToken.MENO):
            op = self.tok.tipo
            self.avanti()
            nodo_dx = self.factor(False)
            if isinstance(nodo_dx, ErroreInterpretazione):
                return nodo_dx
            nodo_sx = NodoBinario(nodo_sx, nodo_dx, op)

        return nodo_sx

    def factor(self, signed):
        nodo_sx = self.implied_mul(signed)
        if isinstance(nodo_sx, ErroreInterpretazione):
            return nodo_sx

        while self.tok in (TipoToken.PER, TipoToken.DIVISO):
            op = self.tok.tipo
            self.avanti()
            nodo_dx = self.implied_mul(False)
            if isinstance(nodo_dx, ErroreInterpretazione):
                return nodo_dx
            nodo_sx = NodoBinario(nodo_sx, nodo_dx, op)

        return nodo_sx

    def implied_mul(self, signed):
        nodo_sx = self.power(signed)
        if isinstance(nodo_sx, ErroreInterpretazione):
            return nodo_sx

        while True:
            idx = self.idx
            nodo_dx = self.power(False)
            if isinstance(nodo_dx, ErroreInterpretazione):
                self.idx = idx
                return nodo_sx
            nodo_sx = NodoBinario(nodo_sx, nodo_dx, TipoToken.PER)

    def power(self, signed):
        if signed:
            nodo_sx = self.signed_value()
        else:
            nodo_sx = self.value()
        if isinstance(nodo_sx, ErroreInterpretazione):
            return nodo_sx

        if self.tok != TipoToken.POTENZA:
            return nodo_sx
        self.avanti()
        nodo_dx = self.value()
        if isinstance(nodo_dx, ErroreInterpretazione):
            return nodo_dx

        nodo_sx = NodoBinario(nodo_sx, nodo_dx, TipoToken.POTENZA)
        curr_node = nodo_sx

        while self.tok == TipoToken.POTENZA:
            self.avanti()
            nodo_dx = self.value()
            if isinstance(nodo_dx, ErroreInterpretazione):
                return nodo_dx
            curr_node.r_node = NodoBinario(curr_node.nodo_dx, nodo_dx, TipoToken.POTENZA)
            curr_node = curr_node.nodo_dx

        return nodo_sx

    def signed_value(self):
        negative = False
        if self.tok == TipoToken.PIU:
            self.avanti()
        elif self.tok == TipoToken.MENO:
            negative = True
            self.avanti()
        value_node = self.power(False)
        if isinstance(value_node, ErroreInterpretazione):
            return value_node
        if negative:
            return NodoNeg(value_node)
        else:
            return value_node

    def value(self):
        if self.tok == TipoToken.PAREN_SX:
            self.avanti()
            expr = self.expr(True)
            if self.tok != TipoToken.PAREN_DX:
                return ErroreInterpretazione(f"prevista ')'")
            self.avanti()
            return expr
        return self.literal()

    def literal(self):
        if self.tok == TipoToken.NUMERO:
            node = NodoValore(self.tok.valore)
            self.avanti()
            return node
        elif self.tok == (TipoToken.IDENT, self.var_ind):
            self.avanti()
            return NodoVar()
        elif self.tok == (TipoToken.IDENT, 'pi'):
            self.avanti()
            return NodoValore(math.pi)
        elif self.tok == (TipoToken.IDENT, 'e'):
            self.avanti()
            return NodoValore(math.e)
        elif self.tok == TipoToken.IDENT and self.tok.valore in FUNZIONI_CON_BASE:
            func = self.tok.valore
            self.avanti()
            if self.tok == TipoToken.TRATTINO_BASSO:
                self.avanti()
                base = self.value()
                if isinstance(base, ErroreInterpretazione):
                    return base
            else:
                base = None
            argomento = self.func_arg()
            if isinstance(argomento, ErroreInterpretazione):
                return argomento
            return NodoFunzione(func, argomento, base)
        elif self.tok == TipoToken.IDENT and self.tok.valore in FUNZIONI:
            func = self.tok.valore
            self.avanti()
            argomento = self.func_arg()
            if isinstance(argomento, ErroreInterpretazione):
                return argomento
            return NodoFunzione(func, argomento)
        else:
            return ErroreInterpretazione(f"previsto un valore")

    def func_arg(self):
        if self.tok == TipoToken.PAREN_SX:
            return self.value()
        else:
            return self.implied_mul(False)


def interpreta_funzione(input_utente, var_ind):
    lista_token = []
    parser = Parser(lista_token, var_ind)
    return parser.interpreta()
