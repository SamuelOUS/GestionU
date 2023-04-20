import csv
from typing import Optional


class Estudiante:
    def __init__(self, nombre: str, apellidos: str, facultad: str, id: int, contrasena: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.facultad = facultad
        self.id = id
        self.contrasena = contrasena

    def seleccionar_gestion(self):
        pass

    def seleccionar_producto(self):
        pass

class Gestion:
    def __init__(self):
        self.estudiantes = dict[str: Estudiante] = {}

    def registrar_estudiante(self, nombre: str, apellidos: str, facultad: str, id: int, contrasena: str):

        if self.registrado(id) is None:
            estudiante = Estudiante(nombre, apellidos, facultad, id, contrasena)
            self.estudiantes[id] = estudiante
            self.agregar_estudiante(nombre, apellidos, facultad, id, contrasena)

            #else:
            #raise CuentaExistenteError("esta cuenta ya esta registrada")

    def registrado(self, id: int) -> Optional[Estudiante]:
        if id in self.estudiantes.keys():
            return self.estudiantes[id]
        else:
            return None

    def agregar_estudiante(self, nombre: str, apellidos: str, facultad: str, id: int, contrasena: str):
        with open ("archivos/usuarios", encoding="utf8", mode="a") as file:
            file.write(f"{nombre}-{apellidos}-{facultad}-{id}-{contrasena}")


class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} ------ Precio: {self.precio}"

class Carrito:
    def __init__(self):
        self.producto = []
        self.valor_total= 0

    def agregar_carrito(self, Producto):
        pass

    def comprar_producto(self):
        pass

    def calcular_total(self):
        pass

    def eliminar_producto(self):
        pass

    def mostrar_factura(self):
        pass


class Calendario:
    def __init__(self, dia: int, mes: int, año: int):
        self.dia = dia
        self.mes = mes
        self.año= año

    def crear_evento(self):
        pass

    def agregar_evento(self):
        pass

    def eliminar_evento(self):
        pass

class Clima:
    def __init__(self, ubicacion: str):
        self.ubicacion = ubicacion

    def ingresar_localidad(self):
        pass

    def mostrar_clima(self):
        pass






