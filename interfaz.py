from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QAbstractItemView, QInputDialog
from modelo import Gestion
from excepciones import *

class Ventana_principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/ventana_principal.ui", self)
        self.__botones()
        self.registro = Registro()

    def __botones(self):
        self.Registrar_Button.clicked.connect(self.abrir_registro)

    def abrir_registro(self):
        self.registro.exec()

    def abrir_iniciar_sesion(self):
        pass

    def abrir_papeleria(self):
        pass


class Registro(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/ventana_registrarse.ui", self)

    def datos_registro(self):

        try:
            nombre = self.lineEdit_Nombre.text()
            apellidos = self.lineEdit_Apellidos.text()
            facultad = self.lineEdit_facultad.text()
            id = self.lineEdit_id.text()
            contrasena = self.lineEdit_contrasena.text()

        except EspaciosSinRellenar as err:

            mensaje= QMessageBox(self)
            mensaje.setWindowTitle("Debes rellenar todos los campos para finalizar el registro")
            mensaje.exec()




class Iniciar_Sesion(QDialog):
    pass


class Papeleria(QDialog):
    pass

class Calendario(QDialog):
    pass

class Clima(QDialog):
    pass





