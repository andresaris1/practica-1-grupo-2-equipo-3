from ExepcionC1 import ExepcionC1

class UsuarioNoEncontradoError(ExepcionC1):
    def __init__(self):
        super().__init__("UsuarioNoEncontradoError----")