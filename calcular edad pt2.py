try:
    edad1 = int(input("Ingrese la edad de la primer persona: "))
    edad2 = int(input("Ingrese la edad de la segunda persona: "))

    if edad1 > edad2:
        print("La primer persona es mayor")
    elif edad1 < edad2:
        print("La segunda persona es mayor")
    else:
        print("Tienen la misma edad")

except ValueError:
    print("Por favor, ingrese números válidos para las edades.")
