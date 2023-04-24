import csv
from typing import Optional
from excepciones import *


class Estudiante:
    def __init__(self, nombre: str, apellidos: str, facultad: str, id: str, contrasena: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.facultad = facultad
        self.id = id
        self.contrasena = contrasena

    def seleccionar_producto(self):
        pass

class Gestion:
    def __init__(self):
        self.estudiantes = {}
        self.nuevo_usuario: Estudiante = Estudiante("","","","","")

    def registrar_estudiante(self, nombre: str, apellidos: str, facultad: str, id: str , contrasena: str):

        if self.estaRegistrado(id) is False:
            estudiante = Estudiante(nombre, apellidos, facultad, id, contrasena)
            self.estudiantes[id] = estudiante
            self.agregar_estudiante(nombre, apellidos, facultad, id, contrasena)
        else:
            raise CuentaExistenteError("Esta cuenta está registrada")

    def agregar_estudiante(self, nombre: str, apellidos: str, facultad: str, id: str, contrasena: str):
        estudiante = Estudiante(nombre, apellidos, facultad, id, contrasena)
        self.estudiantes[id] = estudiante
        self.estudiantes[contrasena] = estudiante
        with open("./archivos/usuarios.txt", encoding="utf8", mode="a") as file:
            file.write(f"{nombre},{apellidos},{facultad},{id},{contrasena}\n")

    def consultarTodosLosEstudiantes(self):
        with open('./archivos/usuarios.txt', encoding='utf8') as file:
            return csv.reader(file, delimiter="-")

    def estaRegistrado(self, id: str):
        with open("./archivos/usuarios.txt", "r") as file:
            lineas = file.readlines()
        esUsuarioRegistrado = False
        for linea in lineas:
            campos = linea.split(',')
            if len(campos) >= 4 and campos[3] == str(id):
                esUsuarioRegistrado = True
                break
        return esUsuarioRegistrado

    def iniciar_sesion(self, id: str, contrasena: str):
        if id == "" or contrasena == "":
            raise EspaciosSinRellenar("debe lllenar todos los datos del ingreso")

        if self.estaRegistrado(id) == False:
            raise CuentaNoExiste("esta cuenta no esta registrada")

        if self.contrasena_correcta(contrasena) == False:
            raise ContrasenaIncorrecta("la contraseña no es correcta")
        else:
            return True

    def contrasena_correcta(self, contrasena: str):
        with open("./archivos/usuarios.txt", "r") as file:
            lineas = file.readlines()
        contrasena_correcta = False
        for linea in lineas:
            campos = linea.strip().split(',')
            if len(campos) > 4 and campos[4] == str(contrasena):
                contrasena_correcta = True
                break
        return contrasena_correcta

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







