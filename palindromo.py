# input("") permite al usuario ingresar un valor por consola
# Consigna,
# A partir de un string ingresado por consola
# determinar si dicho string es palindromo
# Palindromo: alreves y normal se escriben igual, neuquen, jojo
cadena = input("Ingrese una cadena de texto: ")
print("Esta es una cadena:", cadena)

listaString= list(cadena)
listaString.reverse()

reversa= ''.join(listaString)

if cadena== reversa:
    print("Es palindromo")
else :
    print("no es palindromo")