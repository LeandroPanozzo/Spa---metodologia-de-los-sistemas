#Imprimir los números de un rango en orden inverso. El inicio y el fin del rango es ingresado por el usuario
lista=[]
valor=-1
while(valor!=0):
    valor= int(input("Ingrese los valores, 0 para salir: "))
    if(valor==0):
        break
    else:
        lista.append(valor)
        
lista.reverse()
print(f"El orden inverso sera: {lista}")