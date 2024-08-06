#AGREGAR, ELIMINAR, MODIFICAR
tupla=()
seguir = True
lista=list(tupla)

while seguir:
    valor = input("Ingrese el valor que desea, o presione 'n' para salir: ")
    if valor == "n":
        seguir = False
    elif valor.isdigit():
        lista.append(int(valor))
    else:
        print("Ingresó un valor no válido")

tupla=tuple(lista)

print("1- ver lista completa")
print("2- valor maxima")
print("3- valor minimo")
print("4- valores pares")
print("5- valores impares")
print("6- Agregar")
print("7- Eliminar")
print("8- Modificar")

opcion= input("Elija lo que desea hacer:")
if(opcion.isdigit()):
    opcion=int(opcion)
    if(opcion==1):
        print("Lista final:", tupla)
    elif opcion == 2:
        if tupla:
            print(f"Valor máximo: {max(tupla)}")
        else:
            print("La lista está vacía.")
    elif opcion == 3:
        if tupla:
            print(f"Valor mínimo: {min(tupla)}")
        else:
            print("La lista está vacía.")
    elif(opcion==4):
        print("valores pares:")
        for item in tupla:
            if(item%2==0):
                print(item)
    elif(opcion==5):
        print("valores impares:")
        for item in tupla:
            if(item%2==1):
                print(item) 
    elif(opcion==6):
        nuevoValor=input("Ingrese el valor que desea agregar: ")
        if(nuevoValor.isdigit()):
            lista.append(int(nuevoValor))
            tupla=tuple(lista)
            print("Lista actualizada: ", tupla)
        else:
            print("ingrese un numero")
    elif(opcion==7):
        nuevoValor=input("Ingrese el valor que desea eliminar: ")
        if(nuevoValor.isdigit()):
            nuevoValor=int(nuevoValor)
            if nuevoValor in lista:
                lista.remove(nuevoValor)
                tupla=tuple(lista)    
                print("Lista actualizada: ", tupla)
        else:
            print("ingrese un numero")
    elif(opcion==8):
        valorModificar=input("Ingrese el valor que desea modificar: ")
        if(valorModificar.isdigit()):
            valorModificar=int(valorModificar)
            if valorModificar in lista:
                nuevoValor=input("ingrese el nuevo valor: ")
                if nuevoValor.isdigit():
                    indice= lista.index(valorModificar)
                    lista[indice]=int(nuevoValor)
                    tupla=tuple(lista)   
                    print("Lista actualizada:", tupla)
                else:
                    print("Ingrese un número válido.")
            else:
                print("El valor no está en la lista.")
        else:
            print("ingrese un numero")
    else:
        print("Ingreso un valor incorrecto")    
else:
    print("No ingreso un numero")
