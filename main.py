import sys
from PyQt5.QtWidgets import QApplication
from interfaz import Ventana_principal

if __name__ == '__main__':

    app = QApplication(sys.argv)
    inicio = Ventana_principal()
    inicio.show()
    sys.exit(app.exec())
