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
            return csv.reader(file, delimiter=",")

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

class Papeleria:
    def __init__(self):
        self.productos = {}
        self.__cargar_productos()
        self.carrito = Carrito()

    def __cargar_productos(self):
        with open("./archivos/productos.txt") as file:
            csv_data = csv.reader(file, delimiter=",")
            productos = {}
            for row in csv_data:
                if len(row) == 2:
                    productos[row[0]] = Producto(row[0], row[1])
            self.productos = productos

    def agregar_producto_carrito(self, producto, cantidad):
        return self.carrito.agregar_producto(producto, cantidad)

    def eliminar_producto(self, nombre):
        self.carrito.quitar_producto(nombre)

    def mostrar_factura(self):
        pass

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        producto = Item(producto, cantidad)
        self.productos.append(producto)
        return producto

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total = total + producto.calcular_subtotal()
        return total

    def quitar_producto(self, nombre):
        self.productos = [producto for producto in self.productos if producto.nombre != nombre]

class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return (self.producto.precio) * (self.cantidad)







