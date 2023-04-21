import csv
from typing import Optional
from excepciones import *


class Estudiante:
    def __init__(self, nombre: str, apellidos: str, facultad: str, id: int, contrasena: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.facultad = facultad
        self.id = id
        self.contrasena = contrasena

    def seleccionar_producto(self):
        pass

class Gestion:
    def __init__(self):
        self.estudiantes = dict[str: Estudiante]
        self.nuevo_usuario: Estudiante = Estudiante("","","", Optional[None],"")

    def registrar_estudiante(self, nombre: str, apellidos: str, facultad: str, id: int , contrasena: str):

        if self.registrado(id) is None:
            estudiante = Estudiante(nombre, apellidos, facultad, id, contrasena)
            self.estudiantes[id] = estudiante
            self.agregar_estudiante(nombre, apellidos, facultad, id, contrasena)

        else:
            raise CuentaExistenteError("Esta cuenta está registrada")

    def registrado(self, id: int) -> Optional[Estudiante]:
        if id in self.estudiantes.keys():
            return self.estudiantes[id]
        else:
            return None

    def agregar_estudiante(self, nombre: str, apellidos: str, facultad: str, id: int, contrasena: str):
        with open("./archivos/usuarios.txt", encoding="utf8", mode="a") as file:
            file.write(f"{nombre},{apellidos},{facultad},{id},{contrasena}'\n'")

    def estaRegistrado(self, id:int):
        datos = self.consultarTodosLosEstudiantes()
        esUsuarioRegistrado = False
        for row in datos:
            print(row)
            if(row[3] == id):
                esUsuarioRegistrado = True
        return esUsuarioRegistrado

    def iniciar_sesion_estudiante(self, id: int, contrasena: str) -> bool:
        esUsuarioRegistrado = self.estaRegistrado(id)
        if(esUsuarioRegistrado):
            estudiante = self.consultarEstudiantePorId(id)
            return estudiante and estudiante.id == id and estudiante.contrasena == contrasena

        pass

    def consultarEstudiantePorId(self, id:int) -> Optional[Estudiante]:
        datos = self.consultarTodosLosEstudiantes()
        for row in datos:
            if(row[3] == id):
                nombre = row[0]
                apellidos = row[1]
                facultad = row[2]
                id = row[3]
                password = row[4]
                return Estudiante(nombre,apellidos,facultad,id,password)
        return None

    def consultarTodosLosEstudiantes(self):
        with open('./archivos/usuarios.txt', encoding='utf8') as file:
            return csv.reader(file, delimiter=",")


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

    def eliminar(self):
        pass

class Clima:
    def __init__(self, ubicacion: str):
        self.ubicacion = ubicacion

    def ingresar_localidad(self):
        pass







