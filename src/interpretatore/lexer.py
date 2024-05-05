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
    NUMERO = auto()

    # per aggiungere un tipo di token scrivere NOME = auto()


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
