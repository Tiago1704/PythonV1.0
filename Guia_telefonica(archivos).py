from ModuloListaArchivo import Lista,insertar, eliminar, busqueda,mostrar_listaGuia
from Unit_GuiaTelefonica import agregarContacto,busqueda_apellido,imprimirEleccion,modificar_contacto,mostrarGuia,imprimirOpciones,ver_contacto,eliminar_contacto,busqueda_tel
from Unit_Validaciones import validacionNumero2



while (True):
    imprimirOpciones()
    opcionMenu = input("Elige una opción >>>> ")
    if(opcionMenu=="1"):
        print("")
        agregarContacto()
    elif (opcionMenu=="2"):
        print("")
        mostrarGuia()
    elif (opcionMenu=="3"):
        telefono = validacionNumero2()
        x,y = busqueda_tel(telefono)
        if(x!=False):
            while(True):
                ver_contacto(x)
                imprimirEleccion()
                tecla = input("Qué desea hacer? ")
                if(tecla=='1'):
                    modificar_contacto(x.telefono)
                    break
                elif(tecla=='2'):
                    z = eliminar(y,x.telefono,"telefono")
                    if(z!=None):
                        print("")
                        print(">>> Contacto eliminado con éxito\n")
                        break
                    else:
                        print("El contacto no se encuentra en la guía teléfonica\n")
                        break
                elif(tecla=='3'):
                    break
                else:
                    print ("")
                    input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        else:
            print("el contacto no se encuentra en la guía telefónica\n")            
    elif opcionMenu=="4":
        print("")
        busqueda_apellido()
    elif opcionMenu=="5":
        telefono = validacionNumero2()
        modificar_contacto(telefono)
    elif opcionMenu=="6":
        print("")
        x = eliminar_contacto()
        if(x!=None):
            print("CONTACTO ELIMINADO CON ÉXITO...")
        else:
            print("El contacto no se encuentra en la guía teléfonica\n")    
    elif opcionMenu=="7":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
            





