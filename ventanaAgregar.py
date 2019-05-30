import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from ModuloListaArchivo import insertar,busqueda
from Unit_GuiaTelefonica import Persona, f_hash
from PyQt5.QtGui import QIcon
import Interfaz_rc
from Unit_Validaciones import validacionNombre2,validacionApellido2,validacionDireccion2,validacionNumero2
from VentanaExitosa import Vexito

class Vagregar(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Agregar_Contacto.ui",self)
        self.setMinimumSize(1146,592)
        self.setMaximumSize(1146,592)
        self.setWindowTitle("Agregar Contacto")
        self.setWindowIcon(QIcon("tel.png"))
        self.errorArea.hide()
        self.errorVacio.hide()
        self.errorDigit.hide()
        self.errorNum.hide()
        self.errorDir.hide()
        self.errorCalle.hide()
        self.errorApe.hide()
        self.errorName.hide()
        self.errorRepe.hide()
        self.errorNameUpper.hide()
        self.errorApeUpper.hide()
        self.bRegresar.clicked.connect (self.cerrar)
        self.bListo.clicked.connect(self.agregarContacto)
        self.show()
        
    
    def agregarContacto(self):
        self.errorRepe.hide ()
        aux = Persona()
        x1 = validacionNumero2(self)
        x2 = validacionNombre2(self)       
        x3 = validacionApellido2(self)        
        x4 = validacionDireccion2(self)
        if(x1!=False and x2!=False and x3!=False and x4!=False):
            aux.telefono = x1
            aux.nombre = x2
            aux.apellido = x3
            aux.direccion = x4    
            pLista = f_hash(aux.telefono)
            if(busqueda(pLista,aux,"telefono")==0):     
                insertar(pLista,aux,"apellido")     
                exito = Vexito()
                exito.exec_()
                self.close()
            else:
                self.errorRepe.show()
                
    def cerrar (self):
        self.close ()            



    
    
    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Vagregar()
    sys.exit(app.exec_())
            