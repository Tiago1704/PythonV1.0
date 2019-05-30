import sys
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget,QTableWidgetItem,QAbstractItemView
from ventanaAgregar import Vagregar
from VentanaBusquedaTel import Vbusqueda_tel
from VentanaModificar import Vmodificar
from VentanaMostrar import Vmostrar
from VentanaEliminar import Veliminar
from PyQt5.QtCore import Qt
import Interfaz_rc
from Unit_GuiaTelefonica import Persona,listas_aux
from ModuloListaArchivo import insertar,busqueda, mostrar_listaGuia

class MainMenu(QMainWindow):
    
    def __init__(self):
        super().__init__()
        loadUi("Menu_guia.ui",self)
        self.setMinimumSize(1276,862)
        self.setMaximumSize(1276,862)
        self.setWindowTitle("Guía Telefónica")
        self.setWindowIcon(QIcon("tel.png"))
        self.bAgregar.clicked.connect(self.agregar)
        self.bSalir.clicked.connect(self.salir)
        self.bBusTel.clicked.connect(self.busTel)
        self.bModificar.clicked.connect(self.modificar)
        self.bListar.clicked.connect(self.mostrar)
        self.bEliminar.clicked.connect(self.eliminar)
        self.bOtherSide.clicked.connect(self.volverBuscar)
        self.tabla.verticalHeader().setVisible(False)
        self.bOtherSide.hide()
        self.tabla.hide()
        self.errorCity.hide()
        self.textoTitle.hide()
        self.tabla.setWordWrap(False)
        nombreColumnas = ("Apellido","Nombre", "Dirección", "Teléfono")
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)
        self.tabla.setRowCount(0)
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.setEditTriggers (QAbstractItemView.NoEditTriggers)
        self.show()        
        
    def agregar(self):
        vent_2=Vagregar()
        vent_2.exec_()
    
    def eliminar (self):
        vent_3=Veliminar()
        vent_3.exec_()
    
    def busTel(self):
        vent_4=Vbusqueda_tel()
        vent_4.exec_()
    
    def modificar(self):
        vent_5=Vmodificar()
        vent_5.exec_()
    
    def volverBuscar(self):
        self.textoTitle.hide()
        self.tabla.hide()
        self.tabla.clearContents()
        self.bOtherSide.hide()
        self.regiones.show()
        self.bListar.show()
    
    def salir(self):
        sys.exit()
            
    def mostrar(self):
        self.regiones.hide()
        self.bListar.hide()
        self.errorCity.hide()
        index = obtenerLista(self.regiones.currentIndex())
        contactos = mostrar_listaGuia(listas_aux[index])
        if(contactos == None):
            self.errorCity.show()
            self.regiones.show()
            self.bListar.show()
        else:
            self.errorCity.hide()
            self.textoTitle.setText(''+' CONTACTOS DE '+self.regiones.currentText().upper()+': ')
            self.textoTitle.show()
            self.tabla.show()
            self.bOtherSide.show()
            self.listado(contactos)
    

    def listado(self, vector): 
        row = 0
        for contacto in vector:    
            self.tabla.setRowCount(row + 1)
            self.tabla.setItem(row, 0, QTableWidgetItem(contacto.apellido))
            self.tabla.setItem(row, 1, QTableWidgetItem(contacto.nombre))
            self.tabla.setItem(row, 2, QTableWidgetItem(contacto.direccion))
            self.tabla.setItem(row, 3, QTableWidgetItem(contacto.telefono))
            row += 1    
        

def obtenerLista(indice):      
    numeros = {               
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38
    }
    return numeros.get(indice)        

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    sys.exit(app.exec_())
    


