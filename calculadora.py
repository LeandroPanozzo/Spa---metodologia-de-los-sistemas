# Tarea: Calculadora Básica en Python

# Descripción:

# Les dejo gente un lindo ejercicio para practicar y empezar a darle forma a los programas que vayan armando en Python:

# Desarrolla una calculadora básica que permita realizar las siguientes operaciones matemáticas:

#     Suma
#     Resta
#     Multiplicación 
#     División

# Requisitos:

#     El programa debe solicitar al usuario los dos números con los que desea realizar la operación y la operación que desea realizar.
#     El programa debe mostrar el resultado de la operación de forma clara y concisa.
#     El programa debe repetir el proceso hasta que el usuario decida salir.
#     El programa debe manejar errores de entrada, como ingresar valores no numéricos o intentar dividir por cero.

def switch_case(opcion, valor1, valor2):
        if opcion=="1":
            suma= valor1+valor2
            return f"la suma sera: {suma}"
        elif opcion=="2":
            resta= valor1-valor2
            return f"la resta sera: {resta}"
        elif opcion=="3":
            multiplicacion= valor1*valor2
            return f"el valor de la multiplicacion sera: {multiplicacion}"
        elif opcion=="4":
            if valor2!=0:
                division= valor1/valor2
                return f"el valor de la division sera: {division}"
            else:
                return "no se puede dividir por 0"
        elif opcion=="5":
            return "Salir"
        else:
            return "Opcion no valida"
        
def obtenerNumero(mensaje):
    while True:
        try:
            entrada= input(mensaje)
            numero= float(entrada) # Intenta convertir la entrada a float
            return numero
        except ValueError:
            print("debe ingrear un valor valido")
            

print("calculadora de python")
while True:
    print("------------------------------------------------------------")
    valor1=obtenerNumero("Ingrese el valor 1")
    valor2= obtenerNumero("Ingrese el valor 2")
    opcion=input(" 1- suma \n 2- resta \n 3- multiplicacion  \n 4- division \n 5- salir")
    
# Verifica si la opción seleccionada es numérica y está dentro del rango válido
#isdigit() es un método de las cadenas en Python que retorna True si todos los caracteres de la cadena son dígitos 
# (0-9), de lo contrario retorna False
#1 <= int(opcion) <= 5 verifica si el valor entero resultante está entre 1 y 5, inclusive. Es decir, verifica
# si opcion es un número entero válido dentro del rango permitido para las opciones de la calculadora (del 1
# al 5).
    if opcion.isdigit() and 1<= int(opcion) <=5:
        resultado=switch_case(opcion, valor1, valor2)
        print(resultado)
        if opcion == "5":
            print("Saliendo del programa...")
            break
    else:
            print("Error: Debes seleccionar una opción válida (1-5).")
        
