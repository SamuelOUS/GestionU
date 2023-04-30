import sys
from PyQt5.QtWidgets import QApplication
from interfaz import *

if __name__ == '__main__':

    app = QApplication(sys.argv)
    inicio = Papeleria_Ventana()
    inicio.show()
    sys.exit(app.exec())


