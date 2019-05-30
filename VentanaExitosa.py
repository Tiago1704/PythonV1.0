import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QIcon

class Vexito(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("operacionExito.ui",self)
        self.setMinimumSize(400,300)
        self.setMaximumSize(400,300)
        self.setWindowTitle("Operación realizada con éxito")
        self.setWindowIcon(QIcon("tel.png"))
        self.bAceptar.clicked.connect(self.close)
        self.show()
        







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Vexito()
    sys.exit(app.exec_())