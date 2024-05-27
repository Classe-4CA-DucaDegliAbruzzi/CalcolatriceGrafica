"""Unico file che comprende tutto il codice della calcolatrice grafica"""

from enum import Enum, auto
from abc import ABC, abstractmethod
import abc
import math
import tkinter as tk
from tkinter import ttk


class ErroreInterpretazione:
    def __init__(self, messaggio):
        self.messaggio = messaggio

    def __repr__(self):
        return self.messaggio

    def msg(self):
        return self.messaggio


class TipoToken(Enum):
    PIU = auto()
    MENO = auto()
    PER = auto()
    DIVISO = auto()
    POTENZA = auto()
    NUMERO = auto()
    IDENT = auto()
    PAREN_TONDA_SX = auto()
    PAREN_TONDA_DX = auto()
    PAREN_QUADRA_SX = auto()
    PAREN_QUADRA_DX = auto()
    PAREN_GRAFFA_SX = auto()
    PAREN_GRAFFA_DX = auto()
    TRATTINO_BASSO = auto()

    FINE_FUNZIONE = auto()


SIMBOLO_A_TIPO_TOKEN = {
    "+": TipoToken.PIU,
    "-": TipoToken.MENO,
    "*": TipoToken.PER,
    "/": TipoToken.DIVISO,
    "^": TipoToken.POTENZA,
    "(": TipoToken.PAREN_TONDA_SX,
    ")": TipoToken.PAREN_TONDA_DX,
    "[": TipoToken.PAREN_QUADRA_SX,
    "]": TipoToken.PAREN_QUADRA_DX,
    "{": TipoToken.PAREN_GRAFFA_SX,
    "}": TipoToken.PAREN_GRAFFA_DX,
    "_": TipoToken.TRATTINO_BASSO
}


class Token:
    # l'attributo valore è utile quando si hanno token ad esempio `NUMERO` con
    # cui va salvato anche il valore del numero, quando si crea un token si
    # può non passare un secondo argomento se non si vuole specificare un valore
    # Token(TipoToken.PIU) -> non specifica un valore
    # Token(TipoToken.NUMERO, 5.0) -> specifica il valore 5
    def __init__(self, tipo, valore=None):
        self.tipo = tipo
        self.valore = valore

    def __repr__(self):
        if self.valore is None:
            return f"Token({self.tipo})"
        return f"Token({self.tipo}, {self.valore!r})"

    def __eq__(self, other):
        if isinstance(other, TipoToken):
            return self.tipo == other
        elif isinstance(other, tuple) or isinstance(other, list):
            return self.tipo == other[0] and self.valore == other[1]
        elif isinstance(other, Token):
            return self.tipo == other.tipo and self.valore == other.valore
        else:
            return NotImplemented


def crea_token(lista_parti):
    lista_token = []

    for parte in lista_parti:
        if parte.isdigit():
            lista_token.append(Token(TipoToken.NUMERO, int(parte)))
        elif parte.isalpha():
            lista_token.append(Token(TipoToken.IDENT, parte))
        else:
            tipo = SIMBOLO_A_TIPO_TOKEN.get(parte)
            if tipo is None:
                return ErroreInterpretazione(f"simbolo sconosciuto '{parte}'")
            lista_token.append(Token(tipo))

    lista_token.append(Token(TipoToken.FINE_FUNZIONE))
    return lista_token


operazioni = ['+', '-', '*', '/', '^', '_']
parentesi_sx = ['(', '[', '{']
parentesi_dx = [')', ']', '}']
funzioni = ['cos', 'sin', 'tan', 'arccos', 'arcsin', 'arctan', 'log', 'ln', 'sqrt', 'abs', 'rt', 'sign']


def traduttore(stringa):
    i = 0
    stringa_tradotta = ''
    while i < len(stringa):
        if stringa[i].isalpha():
            stringa_tradotta += stringa[i]

        elif stringa[i] in parentesi_sx or stringa[i] in parentesi_dx:
            stringa_tradotta += ' ' + stringa[i] + ' '

        elif stringa[i] == '_' or stringa[i] in operazioni:
            stringa_tradotta += ' ' + stringa[i] + ' '

        elif stringa[i].isdigit():
            stringa_tradotta += stringa[i]

        i += 1

    Num = True
    stringa_corretta = ''
    k = 0

    while k < len(stringa_tradotta):
        if stringa_tradotta[k].isdigit():
            stringa_corretta += stringa_tradotta[k]
            Num = True

        elif stringa_tradotta[k] == ' ':
            stringa_corretta += stringa_tradotta[k]
            Num = False

        elif stringa_tradotta[k].isalpha and Num:
            stringa_corretta += ' ' + stringa_tradotta[k]
            Num = False

        elif stringa_tradotta[k].isalpha and not Num:
            stringa_corretta += stringa_tradotta[k]
            Num = False

        elif stringa_tradotta[k] in operazioni:
            Num = False
        k += 1

    lista_tradotta = stringa_corretta.split()
    return lista_tradotta


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
call_argument: '(' signed_expr ')' | '[' signed_expr ']' | '{' signed_expr '}' | implied_mul
one_arg_func_name: 'sin' | 'cos' | 'tan' | 'arcsin' | 'arccos' | 'arctan' | 'sqrt' | 'ln'
num_literal: (0-9)+ ['.' (0-9)+]
"""

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

PARENS = {
    TipoToken.PAREN_TONDA_SX: TipoToken.PAREN_TONDA_DX,
    TipoToken.PAREN_QUADRA_SX: TipoToken.PAREN_QUADRA_DX,
    TipoToken.PAREN_GRAFFA_SX: TipoToken.PAREN_GRAFFA_DX
}


def tok_a_simbolo(tok):
    if tok == TipoToken.PIU:
        return "+"
    elif tok == TipoToken.MENO:
        return "-"
    elif tok == TipoToken.PER:
        return "*"
    elif tok == TipoToken.DIVISO:
        return "/"
    elif tok == TipoToken.POTENZA:
        return "^"
    elif tok == TipoToken.NUMERO:
        return f"numero {tok.valore}"
    elif tok == TipoToken.IDENT:
        return f"{tok.valore!r}"
    elif tok == TipoToken.PAREN_TONDA_SX:
        return "("
    elif tok == TipoToken.PAREN_TONDA_DX:
        return ")"
    elif tok == TipoToken.PAREN_QUADRA_SX:
        return "["
    elif tok == TipoToken.PAREN_QUADRA_DX:
        return "]"
    elif tok == TipoToken.PAREN_GRAFFA_SX:
        return "{"
    elif tok == TipoToken.PAREN_GRAFFA_DX:
        return "}"
    elif tok == TipoToken.TRATTINO_BASSO:
        return "_"
    elif tok == TipoToken.FINE_FUNZIONE:
        return "fine funzione"
    else:
        return str(tok)


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
            except (ValueError, OverflowError):
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
        return expr

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
        if self.tok.tipo in PARENS.keys():
            paren = self.tok.tipo
            self.avanti()
            expr = self.expr(True)
            if self.tok != PARENS[paren]:
                return ErroreInterpretazione(f"prevista '{tok_a_simbolo(PARENS[paren])}',"
                                             " trovato '{tok_a_simbolo(self.tok)}'")
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
            return ErroreInterpretazione(f"previsto un valore, trovato '{tok_a_simbolo(self.tok)}'")

    def func_arg(self):
        if self.tok.tipo in PARENS.keys():
            return self.value()
        else:
            return self.implied_mul(False)


def interpreta_funzione(input_utente, var_ind):
    lista_parti = traduttore(input_utente)
    if isinstance(lista_parti, ErroreInterpretazione):
        return lista_parti
    lista_token = crea_token(lista_parti)

    if isinstance(lista_token, ErroreInterpretazione):
        return lista_token
    parser = Parser(lista_token, var_ind)
    return parser.interpreta()


class Tela:
    def __init__(self, canvas):
        self.canvas = canvas
        self.range_x = (-5.0, 5.0)
        self.range_y = (-5.0, 5.0)
        self.colore = "black"
        self.spessore = 1

    def w(self):
        return int(self.canvas.cget("width"))

    def h(self):
        return int(self.canvas.cget("height"))

    def x_tela_a_x_piano(self, x_tela):
        return ((x_tela * (self.range_x[1] - self.range_x[0])) / self.w()) + self.range_x[0]

    def y_tela_a_y_piano(self, y_tela):
        return (((y_tela - self.h()) * (self.range_y[1] - self.range_y[0])) / (-self.h())) + self.range_y[0]

    def x_piano_a_x_tela(self, x_piano):
        return (x_piano - self.range_x[0]) * self.w() / (self.range_x[1] - self.range_x[0])

    def y_piano_a_y_tela(self, y_piano):
        return ((y_piano - self.range_y[0]) / (self.range_y[1] - self.range_y[0])) * (0 - self.h()) + self.h()

    def linea(self, p1, p2):
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], width=self.spessore, fill=self.colore)

    def linee(self, punti):
        # Disegna le linee connesse dai punti
        for i in range(len(punti) - 1):
            x1, y1 = punti[i]
            x2, y2 = punti[i + 1]
            self.linea((x1, y1), (x2, y2))

    def ellisse(self, p1, p2):
        self.canvas.create_oval(p1[0], p1[1], p2[0], p2[1], width=self.spessore, outline=self.colore)

    def disegna_sfondo(self):

        prev_spessore = self.spessore
        prev_colore = self.colore

        self.colore = "grey"
        self.spessore = 1

        # Disegna linee per ogni unità intera del piano
        for i in range(int(self.range_x[0]) - 1, int(self.range_x[1]) + 1):
            x = self.x_piano_a_x_tela(i)
            y_start = self.y_piano_a_y_tela(self.range_y[0])
            y_end = self.y_piano_a_y_tela(self.range_y[1])
            self.linea((x, y_start), (x, y_end))

        for i in range(int(self.range_y[0]) - 1, int(self.range_y[1]) + 1):
            y = self.y_piano_a_y_tela(i)
            x_start = self.x_piano_a_x_tela(self.range_x[0])
            x_end = self.x_piano_a_x_tela(self.range_x[1])
            self.linea((x_start, y), (x_end, y))

        self.colore = "black"
        self.spessore = 2
        # Disegna assi x e y
        x_assi_start = (0, self.y_piano_a_y_tela(0))
        x_assi_end = (self.w(), self.y_piano_a_y_tela(0))
        self.linea(x_assi_start, x_assi_end)

        y_assi_start = (self.x_piano_a_x_tela(0), 0)
        y_assi_end = (self.x_piano_a_x_tela(0), self.h())
        self.linea(y_assi_start, y_assi_end)

        self.colore = prev_colore
        self.spessore = prev_spessore

    def disegna_numeri(self):
        # Disegna i numeri nell'asse x
        for i in range(int(self.range_x[0]), int(self.range_x[1]) + 1):
            if i != 0:
                x = self.x_piano_a_x_tela(i)
                y = self.y_piano_a_y_tela(0)
                self.canvas.create_text(x, y + 10, text=str(i), fill="black")

        # Disegna i numeri nell'asse y
        for i in range(int(self.range_y[0]), int(self.range_y[1]) + 1):
            if i != 0:
                x = self.x_piano_a_x_tela(0)
                y = self.y_piano_a_y_tela(i)
                self.canvas.create_text(x - 10, y, text=str(i), fill="black")

        # Disegna lo zero
        x0 = self.x_piano_a_x_tela(0)
        y0 = self.y_piano_a_y_tela(0)
        self.canvas.create_text(x0 - 10, y0 + 10, text="0", fill="black")

    def pulisci(self):
        self.canvas.delete("all")


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
        self.dictionary: dict[str, tk.Entry | None] = {}
        for i in self.parti[1::2]:
            self.dictionary[i] = None

    def lista_nomi(self):
        return list(self.dictionary.keys())

    def crea_widget(self, master):
        frame = ttk.Frame(master)
        for i, parte in enumerate(self.parti):
            if i % 2 == 0:
                label_input_sosa1 = ttk.Label(frame, text=parte)
                label_input_sosa1.grid(row=0, column=i, sticky='w')
            else:
                entry_sosa1 = ttk.Entry(frame, width=4, justify=tk.RIGHT)
                entry_sosa1.grid(row=0, column=i, padx=5, pady=5)
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
        frame = ttk.Frame(master)
        label_input_sosa = ttk.Label(frame, text='f(' + self.fmt + ') =')
        label_input_sosa.grid(row=0, column=0, sticky="w")
        self.__entry = ttk.Entry(frame, width=40)
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

    def valore(self, x):
        if not self.validi():
            return None
        return self.__func.calcola(x)

    def validi(self):
        if self.__entry is None:
            return False
        self.__update_func()
        return self.__func is not None


class BaseGrafico(abc.ABC):
    def __init__(self, tela):
        self.tela = tela
        self.param = self.crea_param()  # metodo che mi restituisce l'input dei parametri

    @abc.abstractmethod
    def crea_param(self):
        pass

    @abc.abstractmethod
    def disegna(self):
        pass


class BaseGraficoFunzioneX(BaseGrafico, abc.ABC):
    @abc.abstractmethod
    def crea_param(self):
        pass

    @abc.abstractmethod
    def funzione(self, x, parametri):
        pass

    def disegna(self):
        if not self.param.validi():
            return

        lista_nomi = self.param.lista_nomi()
        dizionario = {}  # questo dizionario associa i nome dei parametri al suo valore
        for nome in lista_nomi:
            dizionario[nome] = self.param.valore(nome)

        lista_punti = []
        for x_pixel in range(0, self.tela.w()):
            x_piano = self.tela.x_tela_a_x_piano(x_pixel)  # x_tela è uguale a x_pixel
            y_piano = self.funzione(x_piano, dizionario)
            y_pixel = self.tela.y_piano_a_y_tela(y_piano)
            punto = (x_pixel, y_pixel)
            lista_punti.append(punto)
        self.tela.linee(lista_punti)


class BaseGraficoFunzioneY(BaseGrafico, abc.ABC):
    @abc.abstractmethod
    def crea_param(self):
        pass

    @abc.abstractmethod
    def funzione(self, y, parametri):
        pass

    def disegna(self):
        if not self.param.validi():
            return

        lista_nomi = self.param.lista_nomi()
        dizionario = {}  # questo dizionario associa i nome dei parametri al suo valore
        for nome in lista_nomi:
            dizionario[nome] = self.param.valore(nome)

        lista_punti = []
        for y_pixel in range(0, self.tela.h()):
            y_piano = self.tela.y_tela_a_y_piano(y_pixel)  # y_tela è uguale a y_pixel
            x_piano = self.funzione(y_piano, dizionario)
            x_pixel = self.tela.x_piano_a_x_tela(x_piano)
            punto = (x_pixel, y_pixel)
            lista_punti.append(punto)
        self.tela.linee(lista_punti)


class Parabola(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputCaselle("y = $a$x^2 + $b$x + $c$")

    def funzione(self, x, parametri):
        a = parametri["a"]
        b = parametri["b"]
        c = parametri["c"]
        return a * x ** 2 + b * x + c


class Retta(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputCaselle("y = $m$x + $q$")

    def funzione(self, x, parametri):
        m = parametri["m"]
        q = parametri["q"]
        return m * x + q


class FunzioneX(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputFunzione("x")

    def funzione(self, x, parametri):
        return self.param.valore(x)


class FunzioneY(BaseGraficoFunzioneY):
    def crea_param(self):
        return InputFunzione("y")

    def funzione(self, y, parametri):
        return self.param.valore(y)


class Seno(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputCaselle("y = $a$ * sin($w$ * x)")

    def funzione(self, x, parametri):
        a = parametri["a"]
        w = parametri["w"]
        return a * math.sin(w * x)


class Coseno(BaseGraficoFunzioneX):
    def crea_param(self):
        return InputCaselle("y = $a$ * cos($w$ * x)")

    def funzione(self, x, parametri):
        a = parametri["a"]
        w = parametri["w"]
        return a * math.cos(w * x)


class Applicazione:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calcolatrice")
        self.root.resizable(False, False)

        self.tela = None

        self.range_x_min_entry = None
        self.range_x_max_entry = None
        self.range_y_min_entry = None
        self.range_y_max_entry = None

        self.valore_entry = None
        self.valore_label = None
        self.funz_da_selezionare = None

        self.funzioni = {
            "y = mx + q": Retta,
            "y = ax^2 + bx + c": Parabola,
            "y = a*sin(wx)": Seno,
            "y = a*cos(wx)": Coseno,
            "y = f(x)": FunzioneX,
            "x = f(y)": FunzioneY
        }

        self.grafico_default = "y = mx + q"

        self.frame_parametri = None
        self.widget_parametri = None
        self.grafico = None
        self.grafico_corrente = ""

        self.frame_argomento_funz = None

        self.crea_ui()
        self.aggiorna()

    def crea_ui(self):
        self.root.columnconfigure(0, weight=1)

        controlli = ttk.Frame(self.root)
        controlli.grid(row=0, column=0, sticky=tk.EW)
        controlli.columnconfigure(0, weight=1)

        grafico = tk.Canvas(self.root, bg="white", width=500, height=500)
        grafico.grid(row=1, column=0)
        self.tela = Tela(grafico)
        self.tela.colore = "red"
        self.tela.spessore = 2

        prima_riga = ttk.Frame(controlli)
        prima_riga.grid(row=0, column=0, sticky=tk.EW)
        prima_riga.columnconfigure(0, weight=0)
        prima_riga.columnconfigure(1, weight=0)
        prima_riga.columnconfigure(2, weight=1)

        self.funz_da_selezionare = ttk.Combobox(
            prima_riga,
            width=30,
            values=list(self.funzioni.keys())
        )
        self.funz_da_selezionare.grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.funz_da_selezionare.insert(0, self.grafico_default)
        self.funz_da_selezionare["state"] = "readonly"

        ttk.Button(
            prima_riga,
            text="Imposta",
            command=self.imposta
        ).grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)

        ttk.Button(
            prima_riga,
            text="Aggiorna",
            command=self.aggiorna
        ).grid(row=0, column=2, sticky=tk.E, padx=5, pady=2)

        seconda_riga = ttk.Frame(controlli)
        seconda_riga.grid(row=1, column=0, sticky=tk.EW)

        self.frame_parametri = ttk.Frame(seconda_riga)
        self.frame_parametri.grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)

        self.frame_argomento_funz = ttk.Frame(seconda_riga)
        self.frame_argomento_funz.grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
        ttk.Label(self.frame_argomento_funz, text="f(").pack(side=tk.LEFT)
        self.valore_entry = ttk.Entry(self.frame_argomento_funz, width=3, justify=tk.RIGHT)
        self.valore_entry.pack(side=tk.LEFT)
        ttk.Label(self.frame_argomento_funz, text=") =").pack(side=tk.LEFT)
        self.valore_label = ttk.Label(self.frame_argomento_funz, text="")
        self.valore_label.pack(side=tk.LEFT)
        self.imposta()

        terza_riga = ttk.Frame(controlli)
        terza_riga.grid(row=2, column=0, pady=2)

        self.range_x_min_entry = ttk.Entry(terza_riga, width=4, justify=tk.RIGHT)
        self.range_x_min_entry.insert(0, str(self.tela.range_x[0]))
        self.range_x_max_entry = ttk.Entry(terza_riga, width=4, justify=tk.RIGHT)
        self.range_x_max_entry.insert(0, str(self.tela.range_x[1]))
        self.range_y_min_entry = ttk.Entry(terza_riga, width=4, justify=tk.RIGHT)
        self.range_y_min_entry.insert(0, str(self.tela.range_y[0]))
        self.range_y_max_entry = ttk.Entry(terza_riga, width=4, justify=tk.RIGHT)
        self.range_y_max_entry.insert(0, str(self.tela.range_y[1]))

        ttk.Label(terza_riga, text="Range x [").pack(side=tk.LEFT)
        self.range_x_min_entry.pack(side=tk.LEFT)
        ttk.Label(terza_riga, text=";").pack(side=tk.LEFT)
        self.range_x_max_entry.pack(side=tk.LEFT)
        ttk.Label(terza_riga, text="]             Range y [").pack(side=tk.LEFT)
        self.range_y_min_entry.pack(side=tk.LEFT)
        ttk.Label(terza_riga, text=";").pack(side=tk.LEFT)
        self.range_y_max_entry.pack(side=tk.LEFT)
        ttk.Label(terza_riga, text="]").pack(side=tk.LEFT)

    def aggiorna(self):
        try:
            x_min = float(self.range_x_min_entry.get())
            x_max = float(self.range_x_max_entry.get())
            y_min = float(self.range_y_min_entry.get())
            y_max = float(self.range_y_max_entry.get())
            if x_max <= x_min or y_max <= y_min:
                raise ValueError
            self.tela.range_x = (x_min, x_max)
            self.tela.range_y = (y_min, y_max)
        except ValueError:
            pass

        self.tela.pulisci()
        self.tela.disegna_sfondo()
        try:
            if self.grafico is not None:
                self.grafico.disegna()
        except Exception:
            pass
        self.tela.disegna_numeri()

        if self.grafico and isinstance(self.grafico.param, InputFunzione):
            try:
                val = float(self.valore_entry.get())
            except ValueError:
                return
            risultato = self.grafico.param.valore(val)
            if risultato is None:
                return
            self.valore_label.configure(text=f"{risultato:.6g}")

    def imposta(self):
        if self.funz_da_selezionare.get() == "":
            return
        if self.funz_da_selezionare.get() == self.grafico_corrente:
            return

        if self.widget_parametri is not None:
            self.widget_parametri.destroy()
        self.grafico = self.funzioni[self.funz_da_selezionare.get()](self.tela)
        self.widget_parametri = self.grafico.param.crea_widget(self.frame_parametri)
        self.widget_parametri.pack()
        self.grafico_corrente = self.funz_da_selezionare.get()

        if isinstance(self.grafico.param, InputFunzione):
            self.frame_argomento_funz.grid(column=1, row=0)
        else:
            self.frame_argomento_funz.grid_forget()

    def run(self):
        self.root.mainloop()


def main():
    app = Applicazione()
    app.run()


if __name__ == '__main__':
    main()
