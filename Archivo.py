
import shelve

def abrir (archivo):
    return shelve.open (archivo)
        
def cerrar (archivo):
    archivo.close ()

def agregar (archivo,dato):
    try:
        archivo[str(len(archivo))] = dato
        return True 
    except:
        return None
        
def leer (archivo,pos):
    try:
        return archivo[str(pos)]
    except:
        return None
        
def modificar (archivo,pos,dato):
    try:
        archivo[str(pos)] = dato
        return True
    except:
        return None