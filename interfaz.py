from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QPushButton, QInputDialog
from modelo import *
from excepciones import *

class Ventana_principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/ventana_principal.ui", self)
        self.__botones()
        self.registro = Registro()
        self.gestion = Gestion()
        self.registro.lista.append(self.gestion)

    def __botones(self):
        self.Registrar_Button.clicked.connect(self.abrir_registro)


    def abrir_registro(self):
        self.registro.exec()

    def abrir_iniciar_sesion(self):
        pass

    def abrir_seleccion(self):
        pass

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
        self.lista = []
        self.__botones()

    def __botones(self):
        self.pushButton.accepted.connect(self.registro_ventana)
        self.pushButton.rejected.connect(self.cerrar)

    def cerrar(self):
        pass

    def registro_ventana(self):

        try:
            if self.lineEdit_Nombre.text() != "" and self.self.lineEdit_Apellidos.text() != "" and self.lineEdit_facultad.text() != "" and self.lineEdit_id.text() != "" and self.lineEdit_contrasena.text() != "":
                nombre = self.lineEdit_Nombre.text()
                apellidos = self.lineEdit_Apellidos.text()
                facultad = self.lineEdit_facultad.text()
                id = self.lineEdit_id.text()
                contrasena = self.lineEdit_contrasena.text()
                self.lista[0].registrar_estudiante(nombre, apellidos, facultad, id, contrasena)

                mensaje = QMessageBox(self)
                mensaje.setWindowTitle("")
                mensaje.setText("Registrado con exito")
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.exec()

            else:
                mensaje = QMessageBox(self)
                mensaje.setWindowTitle("Debes rellenar todos los campos para finalizar el registro")
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.exec()


        except EspaciosSinRellenar as err:

            mensaje= QMessageBox(self)
            mensaje.setWindowTitle("Debes rellenar todos los campos para finalizar el registro")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText(err.mensaje)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.exec()



    def datos_registro(self):

            nombre = self.lineEdit_Nombre.text()
            apellidos = self.lineEdit_Apellidos.text()
            facultad = self.lineEdit_facultad.text()
            id = self.lineEdit_id.text()
            contrasena = self.lineEdit_contrasena.text()
            self.gestion.registrar_estudiante(nombre, apellidos, facultad, id, contrasena)


class Iniciar_Sesion(QDialog):
    pass


class Papeleria(QDialog):
    pass

class Calendario(QDialog):
    pass

class Clima(QDialog):
    pass





