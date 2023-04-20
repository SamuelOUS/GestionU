from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QAbstractItemView, QInputDialog
from modelo import Gestion

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

class Registro(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/ventana_registrarse.ui", self)







