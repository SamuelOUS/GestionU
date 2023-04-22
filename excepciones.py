class Error(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class CuentaExistenteError(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class ContrasenaInvalida(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class EspaciosSinRellenar(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class RecibeNumeros(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)
