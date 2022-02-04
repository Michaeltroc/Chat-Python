from PySide2.QtWidgets import QApplication
from controllers.login import VentanaIngreso
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaIngreso()

    window.show()
    app.exec_()