from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from modelo import *
from excepciones import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Ventana_principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/ventana_principal.ui", self)
        self.__botones()
        self.registro = Registro()
        self.seleccion = Seleccion()

    def __clear(self):
        self.ingresar_id.clear()
        self.ingresar_contrasena.clear()

    def __botones(self):
        self.Registrar_Button.clicked.connect(self.abrir_registro)
        self.Iniciar_Button.clicked.connect(self.iniciar_sesion)

    def abrir_registro(self):
        self.registro.exec()

    def iniciar_sesion(self):

        try:
            if self.ingresar_id.text() == "" and self.ingresar_contrasena.text() == "":

                mensaje = QMessageBox(self)
                mensaje.setWindowTitle("AVISO")
                mensaje.setText("Debes rellenar todos los campos para iniciar sesión")
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.exec()
            else:
                id = self.ingresar_id.text()
                contrasena = self.ingresar_contrasena.text()

                gestion = Gestion()
                self.gestion.iniciar_sesion_estudiante(id, contrasena)
                self.seleccion.exec()
                self.__clear()


        except ContrasenaInvalida as err:

            mensaje_ventana = QMessageBox(self)
            mensaje_ventana.setWindowTitle("Error")
            mensaje_ventana.setIcon(QMessageBox.Warning)
            mensaje_ventana.setText(err.mensaje)
            mensaje_ventana.setStandardButtons(QMessageBox.Ok)
            mensaje_ventana.exec()
            self.Txt_clave.clear()

    def abrir_papeleria(self):
        pass

    def abrir_calendario(self):
        pass

    def abrir_clima(self):
        pass

class Registro(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/ventana_registrarse.ui", self)
        self.__botones()
        self.__clear()

    def __botones(self):
        self.Boton_registrar.accepted.connect(self.registro_ventana)

    def __clear(self):
        self.lineEdit_Nombre.clear()
        self.lineEdit_Apellidos.clear()
        self.lineEdit_facultad.clear()
        self.lineEdit_id.clear()
        self.lineEdit_contrasena.clear()

    def registro_ventana(self):

        try:
            if self.lineEdit_Nombre.text() != "" and self.lineEdit_Apellidos.text() != "" and self.lineEdit_facultad.text() != "" and self.lineEdit_id.text() != "" and self.lineEdit_contrasena.text() != "":
                nombre = self.lineEdit_Nombre.text()
                apellidos = self.lineEdit_Apellidos.text()
                facultad = self.lineEdit_facultad.text()
                id = self.lineEdit_id.text()
                contrasena = self.lineEdit_contrasena.text()

                gestion = Gestion()
                gestion.agregar_estudiante(nombre, apellidos, facultad, id,contrasena)

                mensaje = QMessageBox(self)
                mensaje.setWindowTitle("NOTIFICACIÓN")
                mensaje.setText("Registrado con exito")
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.exec()
                self.__clear()


            else:
                mensaje = QMessageBox(self)
                mensaje.setWindowTitle("AVISO")
                mensaje.setText("Debes rellenar todos los campos para finalizar el registro")
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.exec()


        except CuentaExistenteError as err:

            mensaje= QMessageBox(self)
            mensaje.setWindowTitle("La cuenta ya existe")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText(err.mensaje)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.exec()

class Seleccion(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/ventana_seleccion.ui", self)


class Papeleria(QDialog):
    pass

class Calendario(QDialog):
    pass

class Clima(QDialog):
    pass





