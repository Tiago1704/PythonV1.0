import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from ModuloListaArchivo import insertar,busqueda,eliminar
from Unit_GuiaTelefonica import Persona, f_hash
from PyQt5.QtGui import QIcon
import Interfaz_rc
from Unit_Validaciones import validacionNombre2,validacionApellido2,validacionDireccion2,validacionNumero2
from VentanaExitosa import Vexito

class Veliminar(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Eliminar_Contacto.ui",self)
        self.setMinimumSize(1146,592)
        self.setMaximumSize(1146,592)
        self.setWindowTitle("Eliminar Contacto")
        self.setWindowIcon(QIcon("tel.png"))
        self.errorArea.hide()
        self.errorVacio.hide()
        self.errorDigit.hide()
        self.errorNoEnc.hide ()
        self.errorNum.hide()
        self.textoNom.hide ()
        self.textoAp.hide ()
        self.textoDir.hide ()
        self.lineApe.hide ()
        self.lineName.hide ()
        self.lineDir.hide ()
        self.textoTel2.hide ()
        self.bEliminar.hide ()
        self.bBuscar.clicked.connect (self.buscar_nro)
        self.bRegresar.clicked.connect (self.cerrar)
        self.bEliminar.clicked.connect (self.eliminar)
        self.show()
        
    def buscar_nro (self):
        self.errorNoEnc.hide ()
        self.errorVacio.hide ()
        aux = Persona ()
        x = validacionNumero2(self)
        if x != False:            
            pLista = f_hash(x)
            aux.telefono = x
            res = busqueda(pLista,aux,"telefono")
            if(res !=0):  
                self.bBuscar.hide ()
                self.textoTel2.show ()
                self.textoTel.hide ()
                self.textoNom.show ()
                self.textoAp.show ()
                self.textoDir.show ()
                self.lineTel.setReadOnly (True)
                self.lineApe.show ()
                self.lineApe.insert (res.apellido)
                self.lineApe.setReadOnly (True)
                self.lineName.show ()
                self.lineName.insert (res.nombre)
                self.lineName.setReadOnly (True)
                self.lineDir.show ()
                self.lineDir.insert (res.direccion)
                self.lineDir.setReadOnly (True)
                self.bEliminar.show ()
            else:
                self.errorNoEnc.show()
                
    def eliminar (self):
        x = self.lineTel.text ()
        pLista = f_hash (x)
        eliminar (pLista,x,"telefono")
        exito = Vexito()
        exito.exec_()
        self.close()

    def cerrar (self):
        self.close ()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Veliminar()
    sys.exit(app.exec_())
            