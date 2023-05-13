class Error(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class CuentaExistenteError(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class ContrasenaIncorrecta(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class EspaciosSinRellenar(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class CuentaNoExiste(Error):
    def __init__(self, mensaje):
        super().__init__(mensaje)
