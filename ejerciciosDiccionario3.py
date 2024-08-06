#Escribir una función que tome un diccionario y un valor, y devuelva una lista con todas las claves asociadas
# a ese
def encontrar_claves_por_valor(diccionario, valor_buscado):
    #for clave, valor in diccionario.items(): Itera sobre cada par clave-valor en el diccionario.
    #if valor == valor_buscado: Comprueba si el valor asociado a la clave actual es igual al valor que estamos buscando.
    claves = [clave for clave, valor in diccionario.items() if valor == valor_buscado]
    #Si la condición se cumple, la clave se agrega a la lista claves
    return claves

# Ejemplo de uso
mi_diccionario = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 40
}

valor = 10
claves = encontrar_claves_por_valor(mi_diccionario, valor)
print(claves)  # Salida: ['a', 'c']
