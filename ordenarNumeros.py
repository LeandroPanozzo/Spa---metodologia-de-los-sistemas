lista = []
cont = 0

while cont < 3:
    try:
        valor = int(input("Ingrese un número: "))
        lista.append(valor)
        cont += 1
    except ValueError:
        print("Por favor, ingrese un número entero.")

lista.sort()

print(f"El número menor es: {lista[0]}")
print(f"El número mayor es: {lista[-1]}")
print(f"La lista completa ordenada es: {lista}")

