from enum import Enum, auto


class ErroreInterpretazioneEsportato:
    def __init__(self, _):
        raise TypeError("non si può creare un'istanza di ErroreInterpretazione")

    def msg(self):
        pass


class ErroreInterpretazione(ErroreInterpretazioneEsportato):
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
        if parte.isalpha():
            lista_token.append(Token(TipoToken.IDENT, parte))
        elif isinstance(parte, int) or isinstance(parte, float):
            lista_token.append(Token(TipoToken.NUMERO, parte))
        else:
            tipo = SIMBOLO_A_TIPO_TOKEN.get(parte)
            if tipo is None:
                return ErroreInterpretazione(f"simbolo sconosciuto '{parte}'")
            lista_token.append(Token(tipo))

    lista_token.append(Token(TipoToken.FINE_FUNZIONE))
    return lista_token


def traduttore(stringa):
    return []
