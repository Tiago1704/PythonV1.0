

def validacionNombre2(objeto):
        nombre = objeto.lineName.text()
        objeto.errorName.hide()
        objeto.errorNameUpper.hide()
        x = validacionNombre(nombre)
        if(x!=True):
            mostrarError(objeto,x)
            return False
        else:   
            return nombre

def validacionApellido2(objeto):
    apellido = objeto.lineApe.text()
    objeto.errorApe.hide()
    objeto.errorApeUpper.hide()
    x = validacionApellido(apellido)
    if(x!=True):
        mostrarError(objeto,x)
        return False
    return apellido

def validacionNumero2(objeto):
        numero = objeto.lineTel.text()
        objeto.errorArea.hide()
        objeto.errorDigit.hide()
        objeto.errorNum.hide()
        x = validacionNumero(numero)
        if(x!=True):
            mostrarError(objeto,x)
            return False
        else:   
            return numero          
             
def validacionDireccion2(objeto):
    direccion = objeto.lineDir.text()
    objeto.errorDir.hide()
    objeto.errorCalle.hide()
    x = validacionDireccion(direccion)    
    if(x!=True):
        mostrarError(objeto,x)
        return False
    return direccion



def mostrarError(objeto,x):
    if(x=='errorDigit'):
        objeto.errorDigit.show()
    elif(x=='errorNum'):
        objeto.errorNum.show()
    elif(x=='errorArea'):
        objeto.errorArea.show()
    elif(x=='errorName'):
        objeto.errorName.show()
    elif(x=='errorNameUpper'):
        objeto.errorNameUpper.show()      
    elif(x=='errorApe'):
        objeto.errorApe.show()
    elif(x=='errorApeUpper'):
        objeto.errorApeUpper.show()
    elif(x=='errorDir'):
        objeto.errorDir.show()
    elif(x=='errorCalle'):
        objeto.errorCalle.show()
    elif(x==""):
        objeto.errorVacio.show()


def validacionNumero(numero):
    lista_aux = ['011','220','221','223','230','260','237','249','260','261','264','266','280','291',
                 '294','299','336','341','343','345','351','362','370','376','379','380','381','385',
                 "2202","2254","2255","2323","2626","3329","3442","3541","3772","3868"]
    if(numero==""):
        return ''
    elif(not (len(numero) <= 12)):
        return  'errorDigit'
    if( not numero.isalpha() and not ('-') in numero ):       #metodo que permite saber si una cadena es numérica. 
        return  'errorNum'   
    if (not(numero[0:numero.index('-')] in lista_aux)):
        return  'errorArea'
    else:
        return True
"""elif (len(numero)==10):
        if (not(numero[0:4] in lista_aux)):  #agregar codigos de 4 digitos
            return 'errorArea'"""    
    
def validacionNombre(nombre):
    if(nombre==""):
        return ''
    elif(not(nombre.isalpha())):    #Metodo análogo a isdigit().
        return 'errorName'
    elif(nombre.isupper() or nombre.islower()):
        return 'errorNameUpper'
    else:
        return True

def validacionApellido(apellido):
    if(apellido==""):
        return ''
    elif(not(apellido.isalpha())):    #Metodo análogo a isdigit().
        return 'errorApe'
    elif(apellido.isupper() or apellido.islower()):
        return 'errorApeUpper'
    else:
        return True
    
def validacionDireccion(direccion):
    if(direccion.isalpha()):
        return 'errorDir'
    elif(direccion.isdigit()):
        return 'errorDir'
    elif(direccion.isalnum()):       #Metodo que verifica si dicha cadena es alfanumerica.
        return 'errorCalle'
    elif(direccion==""):
        return ''
    else:  #Al contrario de la validación nombre, no tengo en cuenta si la cadena empieza con mayusculas porque una calle puede empezar con un número.
        return True
