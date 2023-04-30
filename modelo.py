import csv
from excepciones import *

class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre: str = nombre
        self.precio: float = precio

    def __str__(self):
        return f"Producto: {self.nombre} ------ Precio: {self.precio}"

class Estudiante:
    def __init__(self, nombre: str, apellidos: str, facultad: str, id: str, contrasena: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.facultad = facultad
        self.id = id
        self.contrasena = contrasena
        self.carrito = Carrito()

    def agregar_producto(self, producto: Producto, cantidad: int):
        self.carrito.agregar_item(producto, cantidad)

    def total(self):
        return self.carrito.total()


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


class Papeleria:
    def __init__(self):
        self.productos = {}
        self.__cargar_productos()
        self.carrito = Carrito()
        self.estudiante_actual: Estudiante = Estudiante("","","","","")

    def __cargar_productos(self):
        with open("./archivos/productos.txt") as file:
            csv_data = csv.reader(file, delimiter=",")
            productos = {}
            for row in csv_data:
                if len(row) == 2:
                    productos[row[0]] = Producto(row[0], row[1])
            self.productos = productos

    def agregar_producto_carrito(self, producto, cantidad: int):
        return self.estudiante_actual.agregar_producto(producto, cantidad)

    def eliminar_producto(self, nombre):
        self.carrito.eliminar(nombre)

    def mostrar_factura(self):
        return self.carrito.items

    def total(self):
        total = self.estudiante_actual.total()
        return total

class Carrito:
    def __init__(self):
        self.items = []
        self.valor_total = 0

    def agregar_item(self, producto, cantidad):
        item = Item(producto, cantidad)
        self.items.append(item)
        return item

    def total(self):
        total = 0
        for objeto in self.items:
            total += objeto.cantidad * float(objeto.producto.precio)
        return total

    def eliminar(self, nombre):
        self.items.pop(nombre)


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad: int = cantidad

    def __str__(self):
        return f"NOMBRE = {self.item}     CANTIDAD = {self.cantidad}"

class Calendario:
    def __init__(self, dia: int, mes: int, año: int):
        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        return f"Dia: {self.dia} ---Mes: {self.mes}---- Año: {self.año}"











