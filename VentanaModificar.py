import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from ModuloListaArchivo import insertar,busqueda,eliminar
from Unit_GuiaTelefonica import Persona, f_hash
from PyQt5.QtGui import QIcon
import Interfaz_rc
from Unit_Validaciones import validacionNombre2,validacionApellido2,validacionDireccion2,validacionNumero2
from VentanaExitosa import Vexito

class Vmodificar(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Modificar_Contacto.ui",self)
        self.setMinimumSize(1146,592)
        self.setMaximumSize(1146,592)
        self.setWindowTitle("Modificar Contacto")
        self.setWindowIcon(QIcon("tel.png"))
        self.errorArea.hide()
        self.errorVacio.hide()
        self.errorDigit.hide()
        self.errorNum.hide()
        self.errorRepe.hide ()
        self.errorDir.hide()
        self.errorCalle.hide()
        self.errorApe.hide()
        self.errorName.hide()
        self.errorNoEnc.hide()
        self.errorNameUpper.hide()
        self.errorApeUpper.hide()
        self.textoNom.hide ()
        self.textoAp.hide ()
        self.textoDir.hide ()
        self.lineApe.hide ()
        self.lineName.hide ()
        self.lineDir.hide ()
        self.bModif.hide ()
        self.bRegresar.clicked.connect (self.cerrar)
        self.bBuscar.clicked.connect(self.buscar_nro)
        self.bModif.clicked.connect (self.modif)
        self.show()
        
    def buscar_nro (self):
        self.errorNoEnc.hide ()
        self.bRegresar.hide ()
        aux = Persona ()
        x = validacionNumero2(self)
        if x != False:            
            pLista = f_hash(x)
            aux.telefono = x
            res = busqueda(pLista,aux,"telefono")
            if(res !=0):  
                eliminar (pLista,x,"telefono")
                self.bBuscar.hide ()
                self.textoNom.show ()
                self.textoAp.show ()
                self.textoDir.show ()
                self.lineApe.show ()
                self.bModif.show ()
                self.lineApe.insert (res.apellido)
                self.lineName.show ()
                self.lineName.insert (res.nombre)
                self.lineDir.show ()
                self.lineDir.insert (res.direccion)
            else:
                self.errorNoEnc.show()
                    
    def modif(self):
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
    ex = Vmodificar()
    sys.exit(app.exec_())
            