class ErroreInterpretazione:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return self.message

    def msg(self):
        return self.message
