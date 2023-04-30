from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QWidget, QAbstractItemView, QInputDialog
from PyQt5.uic import loadUi
from modelo import *
from excepciones import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Ventana_principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui/ventana_principal.ui", self)
        self.setFixedSize(self.size())
        self.__botones()
        self.registro = Registro()
        self.gestion = Gestion()
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
            estudiante = self.ingresar_id.text()
            contrasena = self.ingresar_contrasena.text()
            self.gestion.iniciar_sesion(estudiante, contrasena)
            self.__clear()


        except EspaciosSinRellenar as err:
            mensaje_ventana = QMessageBox(self)
            mensaje_ventana.setWindowTitle("ERROR")
            mensaje_ventana.setIcon(QMessageBox.Warning)
            mensaje_ventana.setText(err.mensaje)
            mensaje_ventana.setStandardButtons(QMessageBox.Ok)
            mensaje_ventana.exec()

        except CuentaNoExiste as err:
            mensaje_ventana = QMessageBox(self)
            mensaje_ventana.setWindowTitle("ERROR")
            mensaje_ventana.setIcon(QMessageBox.Warning)
            mensaje_ventana.setText(err.mensaje)
            mensaje_ventana.setStandardButtons(QMessageBox.Ok)
            mensaje_ventana.exec()

        except ContrasenaIncorrecta as err:

            mensaje_ventana = QMessageBox(self)
            mensaje_ventana.setWindowTitle("ERROR")
            mensaje_ventana.setIcon(QMessageBox.Warning)
            mensaje_ventana.setText(err.mensaje)
            mensaje_ventana.setStandardButtons(QMessageBox.Ok)
            mensaje_ventana.exec()


        else:
            self.seleccion.exec()


class Registro(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/ventana_registrarse.ui", self)
        self.setFixedSize(self.size())
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
                print("-------------------")
                gestion.registrar_estudiante(nombre,apellidos, facultad, id, contrasena)


                mensaje_registro = QMessageBox(self)
                mensaje_registro.setWindowTitle("NOTIFICACIÓN")
                mensaje_registro.setText("Registrado con exito")
                mensaje_registro.setStandardButtons(QMessageBox.Ok)
                mensaje_registro.exec()
                self.__clear()
            else:
                mensaje = QMessageBox(self)
                mensaje.setWindowTitle("AVISO")
                mensaje.setText("Debes rellenar todos los campos para finalizar el registro")
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.exec()

        except CuentaExistenteError as err:

            mensaje = QMessageBox(self)
            mensaje.setWindowTitle("ERROR")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setText(err.mensaje)
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.exec()
            self.__clear()


class Seleccion(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/ventana_seleccionar.ui", self)
        self.setFixedSize(self.size())
        self.papeleria = Papeleria_Ventana()
        self.calendario = Ventana_Calendario()

        self.__botones()

    def __botones(self):
        self.Boton_Papeleria.clicked.connect(self.abrir_papeleria)
        self.Boton_calendario.clicked.connect(self.abrir_calendario)
        self.Boton_cerrar.clicked.connect(self.cerrar_sesion)

    def cerrar_sesion(self):
        self.close()

    def abrir_papeleria(self):
        self.papeleria.exec()

    def abrir_calendario(self):
        self.calendario.show()

    def abrir_clima(self):
        pass


class Papeleria_Ventana(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("gui/papeleria.ui", self)
        self.setFixedSize(self.size())
        self.papeleria = Papeleria()
        self.__botones()
        self.__cargar_datos()

    def __botones(self):

        table_model = QStandardItemModel()
        table_model.setHorizontalHeaderLabels(["PRODUCTO", "CANTIDAD", "TOTAL"])
        self.tableView_carrito.setModel(table_model)
        self.tableView_carrito.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_carrito.setColumnWidth(0,200)
        self.tableView_carrito.setColumnWidth(1, 100)
        self.tableView_carrito.setColumnWidth(2, 160)

        self.list_view_productos.setModel(QStandardItemModel())

        self.Boton_agregar_carrito.clicked.connect(self.agregar_producto_carrito)

    def agregar_producto_carrito(self):
        cantidad , ok = QInputDialog.getInt(self, "Agregar libro a carrito", "Cantidad", 1)
        if ok:
            model = self.list_view_productos.model()
            value = model.itemFromIndex(self.list_view_productos.selectedIndexes()[0])
            item = self.papeleria.agregar_producto_carrito(value.producto, cantidad)
            self.agregar_tabla(item)
            self.actualizar_total()

    def agregar_tabla(self, item):
        sub_total =item.calcular_subtotal()
        celda_1 = QStandardItem(item.producto.nombre)
        celda_2 = QStandardItem(item.cantidad)
        celda_3 = QStandardItem(sub_total)

        model = self.tableView_carrito.model()
        model.appendRow([celda_1, celda_2, celda_3])

    def actualizar_total(self):
        total = self.papeleria.carrito.calcular_total()
        self.lineEdit_total.setText("${:,,.2f}").format(total)

    def __cargar_datos(self):
        productos = list(self.papeleria.productos.values())
        for producto in productos:
            item = QStandardItem(str(producto))
            item.producto = producto
            item.setEditable(False)
            self.list_view_productos.model().appendRow(item)

class Ventana_Calendario(QWidget):
    def __init__(self):
        super(Ventana_Calendario, self).__init__()
        uic.loadUi("gui/calendario_principal.ui", self)
        self.calendarWidget.selectionChanged.connect(self.cambiar_dia)
        self.cambiar_dia()
        self.saveButton.clicked.connect(self.agregar_evento)
        self.addButton.clicked.connect(self.eliminar)

    def cambiar_dia(self):
        print("EL DIA DEL CALENDARIO FUE CAMBIADO")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("FECHA: ", dateSelected)

    def agregar_evento(self):

        if self.taskLineEdit.text() == "":
            messageBox = QMessageBox()
            messageBox.setText("DEBE RELLENAR PARA AGENDAR")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()

        else:
            fecha = self.calendarWidget.selectedDate().toPyDate()
            messageBox = QMessageBox()
            messageBox.setText("AGREGADO A LA AGENDA")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()


    def eliminar(self):
        newTask = str(self.taskLineEdit.text())
        date = self.calendarWidget.selectedDate().toPyDate()

        messageBox = QMessageBox()
        messageBox.setText("ELIMINADO DE LA AGENDA")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

        self.taskLineEdit.clear()





