from ModuloListaArchivo import Lista,insertar, eliminar, busqueda,mostrar_listaGuia,busqueda2
from Unit_Validaciones import validacionNumero2,validacionNombre2,validacionApellido,validacionDireccion2



    
class Persona():   #Simulación de un registro.
    nombre = ''
    apellido = ''
    direccion = ''
    telefono = ''
    
    



def busqueda_apellido():  #modificar
    while(True):
        contactos = list()
        #print("Ingrese el apellido del contacto:" )
        apellido = validacionApellido()
        try:    
            for elemento in listas_aux:
                contactos.append(busqueda2(elemento,apellido,"apellido"))
        except:        
            if(len(contactos)!=0):
                i=1
                for elemento in contactos:
                    print(i,')')
                    ver_contacto(elemento)
                    i+=1
            else:
                input("")
        
                              #Fin menús.

uno11 = "Ciudad Autónoma de Buenos Aires"
Lista(uno11)
dos20  = "Merlo"
Lista(dos20)
dos21  = "La Plata"
Lista(dos21)   
dos23  = "Mar del Plata"
Lista(dos23)
dos30  = "Pilar"
Lista(dos30)
dos36  = "Junín"
Lista(dos36)
dos37  = "Moreno"
Lista(dos37)
dos49  = "Tandil"
Lista(dos49)
dos60  = "San Rafael"
Lista(dos60)
dos61  = "Mendoza"
Lista(dos61)
dos64  = "San Juan"
Lista(dos64)
dos66  = "San Luis"
Lista(dos66)
dos80  = "Trelew"
Lista(dos80)
dos91 = "Bahía Blanca"
Lista(dos91)
dos94 = "San Carlos de Bariloche"
Lista(dos94)
dos99 = "Neuquén"
Lista(dos99)
tres36 = "San Nicolás de los Arroyos"
Lista(tres36)
tres41 = "Rosario"
Lista(tres41)
tres43 = "Paraná"
Lista(tres43)
tres45 = "Concordia"
Lista(tres45)
tres51 = "Córdoba"
Lista(tres51)
tres62 = "Resistencia"
Lista(tres62)
tres70 = "Formosa"
Lista(tres70)
tres76 = "Posadas"
Lista(tres76)
tres79 = "Corrientes"
Lista(tres79)
tres80 = "La Rioja"
Lista(tres80)
tres81 = "San Miguel de Tucumán"
Lista(tres81)
tres85 = "Santiago del Estero"
Lista(tres85)

dos0dos = "González Catán"
Lista (dos0dos)
dos5cuatro = "Pinamar"
Lista (dos5cuatro)
dos5cinco = "Villa Gesell"
Lista (dos5cinco)
tres2tres = "Luján"
Lista (tres2tres)
seis2seis = "La Paz"
Lista (seis2seis)

tres2nueve = "San Pedro"
Lista (tres2nueve)
cuatro4dos = "Concepción del Uruguay"
Lista (cuatro4dos)
cinco4uno = "Villa Carlos Paz"
Lista (cinco4uno)
siete7dos = "Paso de los Libres"
Lista (siete7dos)
ocho6ocho = "Cafayate"
Lista (ocho6ocho)

one = [uno11] #region bsas.               
two = [dos20,dos21,dos23,dos30,dos36,dos37,dos49,dos60,dos61,dos64,dos66,dos80,dos91,dos94,dos99]
three = [tres36,tres41,tres43,tres45,tres51,tres62,tres70,tres76,tres79,tres80,tres81,tres85]  
two2 = [dos0dos,dos5cuatro,dos5cinco,tres2tres,seis2seis]
three2 = [tres2nueve,cuatro4dos,cinco4uno,siete7dos,ocho6ocho]
lIndice = [one,two,three,two2,three2]
listas_aux = [uno11,dos20,dos21,dos23,dos30,dos36,
              dos37,dos49,dos60,dos61,dos64,dos66,dos80,
              dos91,dos94,dos99,tres36,tres41,tres43,
              tres45,tres51,tres62,tres70,tres76,tres79,tres80,tres81,
              tres85,dos0dos,dos5cuatro,dos5cinco,tres2tres,seis2seis,tres2nueve,cuatro4dos,cinco4uno,siete7dos,ocho6ocho]

def f_hash(num):
    indice = int(num[0])-1    #convertimos valor
    lista = lIndice[indice]     #accedemos a la lista
    clave = num[1:num.index('-')]
    if (len (clave) == 2):
        if (indice == -1):
            indice = 0
            lista = lIndice[indice]  #int(num[1:3]
        elif (indice == 1):
            indice = insercion_2(int (clave) - 20)
        elif (indice == 2):
            indice = insercion_3(int(clave) - 36)
    else:
        if (indice == 1):
            lista = lIndice[3]
            indice = insercion_2_2 (int (clave)-202)
        elif (indice == 2):
            lista = lIndice[4]
            indice = insercion_3_2 (int (clave)-329)
    return lista[indice]
            
 
def insercion_2(indice):      #Inserción de región 2.
    numeros = {               #Imitacion de un switcher mediante un diccionario.
        0: '0',
        1: '1',
        3: '2',
        10: '3',
        16: '4',
        17: '5',
        29: '6',
        40: '7',
        41: '8',
        44: '9',
        46: '10',
        60: '11',
        71: '12',
        74: '13',
        79: '14',
    }
    return int(numeros.get(indice))

def insercion_3(indice):      #Inserción de región 3.
    numeros = {               
        0: '0',
        5: '1',
        7: '2',
        9: '3',
        15: '4',
        26: '5',
        34: '6',
        40: '7',
        43: '8',
        44: '9',
        45: '10',
        49: '11',
    }
    return int(numeros.get(indice))
    
def insercion_2_2(indice):      #Inserción de región 2 con 4 digitos
    numeros = {               
        0: '0',
        52: '1',
        53: '2',
        121: '3',
        424: '4'
    }
    return int(numeros.get(indice))    
    
def insercion_3_2(indice):      #Inserción de región 3 con 4 digitos
    numeros = {               
        0: '0',
        113: '1',
        212: '2',
        443: '3',
        539: '4'
    }
    return int(numeros.get(indice))    