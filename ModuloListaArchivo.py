#ListaArchivo
from Archivo import abrir,cerrar,agregar,leer,modificar
import random

def criterio (x,campo):
    if campo == "nombre":
        return x.nombre
    if campo == "apellido":
        return x.apellido
    if campo == "telefono":
        return x.telefono
    if campo == "direccion":
        return x.direccion
    if campo == "":
        return x
    
class NodoLista ():
    def __init__(self):
        self.info = None
        self.sig = 0

def Lista (nombre):
    archivo = abrir (nombre)     
    agregar (archivo,0)
    cerrar (archivo)
            
def insertar (lista,x,campo):        
    l = abrir (lista)
    aux = NodoLista ()
    aux.info = x
    dato = leer(l,0)
    if (dato == 0) or (criterio (x,campo) < criterio (leer (l,dato).info,campo)):
        aux.sig = dato
        agregar (l, aux)
        modificar(l,0,len(l)-1)
    else:
        ant = leer (l,dato)
        act_pos = ant.sig
        ant_pos = dato
        if(act_pos != 0):
            act = leer(l,ant.sig)
        while (act_pos != 0) and (criterio (act.info,campo) < criterio (aux.info,campo)):
            act_pos = act.sig
            act = leer(l, act.sig)
            ant_pos = ant.sig
            ant = leer(l, ant.sig)           
        aux.sig = act_pos
        agregar (l,aux)
        ant.sig = len (l)-1        
        modificar(l,ant_pos,ant)
    cerrar (l)
    
def busqueda (lista,x,campo):
    l = abrir (lista)
    pos = leer (l,0)
    act = leer(l,pos)
    while (pos != 0) and (criterio (act.info,campo) != criterio (x,campo)):
        pos = act.sig
        act = leer(l,pos)
    if pos == 0:
        return pos
    else:
        return act.info
    cerrar (l)    
    
def eliminar (lista,el,campo):
    l = abrir (lista)
    pos = leer (l,0)
    act = leer(l,pos)
    if criterio (act.info,campo) == el:
        x = act.info
        modificar(l,0,act.sig)
    else:
        ant = leer (l,pos)
        act_pos = ant.sig
        ant_pos = pos
        if(act_pos != 0):
            act = leer(l,ant.sig)
        while (act_pos != 0) and (criterio (act.info,campo) != el):
            act_pos = act.sig
            act = leer(l, act.sig)
            ant_pos = ant.sig
            ant = leer(l, ant.sig)
        if (act != None) and (act_pos != 0):
            x = act.info
            ant.sig = act.sig
            modificar(l,ant_pos,ant)
        else:
            x = None
    return x
    cerrar (l)
    
def tamanio_lista (lista):
    l = abrir (lista)
    return len (lista)-2
    cerrar (l)
    
def llenar_lista (lista,tamanio):
    for i in range (0,tamanio):
        elemento = int (random.random ()*100)
        insertar (lista,elemento,"")

def mostrar_lista (lista):
    l = abrir (lista)
    act = leer (l,0)
    while (act != 0):
        dato = leer(l, act)
        print (dato.info)
        act = dato.sig
    cerrar (l)



def mostrar_listaGuia (lista):    #Funcion necesaria para poder mostrar la información de una persona en la agenda telefónica...
    if(not(lista_vacia(lista))):
        contactos = list()
        l = abrir (lista)
        act = leer (l,0)
        while (act != 0):    
            dato = leer(l, act)
            contactos.append(dato.info)
            act = dato.sig
        cerrar (l)
        return contactos
    else:
        return None
        
#dato.info.telefono[0:3]+'-'+dato.info.telefono[3:9]        
    
def mostrar_lista_2 (lista):
    l = abrir (lista)
    act = leer (l,0)
    while (act != 0):
        dato = leer(l, act)
        print (dato.info.nombre)
        act = dato.sig
    cerrar (l)
    
def eliminar_primer_el (lista):
    l = abrir (lista)
    pos = leer (l,0)
    if pos != 0:
        el = leer (l,pos)
        x = el.info
        modificar(l,0,el.sig)
        return x
    else:
        return None
    cerrar (l)
    
def mostrar_lista_suma (lista):
    l = abrir (lista)
    act = leer (l,0)
    suma = 0
    while (act != 0):
        dato = leer(l, act)
        print (dato.info)
        suma = dato.info + suma
        act = dato.sig
    return suma
    cerrar (l)
    
def lista_vacia (lista):
    l = abrir (lista)
    pos = leer (l,0)
    return pos == 0
    cerrar (l)

def busqueda2 (lista,x,campo): 
    if(not(lista_vacia(lista))):
        l = abrir (lista)
        vector = []
        pos = leer (l,0)
        while (pos != 0):
            act = leer(l,pos)
            if (criterio(act.info,campo) == x):
                vector.append(act.info)
            pos = act.sig    
        return vector
        cerrar (l)  
    else:
        return False


