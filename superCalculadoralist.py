# Calculadora
# Opciones:
# 1 - Sumar todos los elementos de una lista
# 2 - Encontrar el maximo
# 3 - Encontrar el minimo
# 4 - Filtrar por pares
# 5 - Filtrar por impares
### Ingrese los valores de la lista por pantalla, y ademas la lista puede tener cualquier tamanio
# input()
lista = []
seguir = True

while seguir:
    valor = input("Ingrese el valor que desea, o presione 'n' para salir: ")
    if valor == "n":
        seguir = False
    elif valor.isdigit():
        lista.append(int(valor))
    else:
        print("Ingresó un valor no válido")

print("1- sumar todos los elementos de la lista")
print("2- encontrar el maximo")
print("3- encontrar el minimo")
print("4 filtrar por pares")
print("--------------------------------------------")
opcion=input("elija una opcion:")
if(opcion.isdigit()):
    opcion=int(opcion)

    if(opcion==1):
        suma = sum(lista)
        print(f"La suma de todos los elementos de la lista es: {suma}")
    elif(opcion==2):
        print(f"valor maximo {max(lista)}")
    elif(opcion==3):
        print(f"valor minimo {min(lista)}")
    elif(opcion==4):
        print("valores pares:")
        for item in lista:
            if(item%2==0):
                print(item)
    elif(opcion==5):
        print("valores impares:")
        for item in lista:
            if(item%2==1):
                print(item)
    else:
        print("Eligio una opcion no valida")
else:
    print("ingrese una opcion valida")

    