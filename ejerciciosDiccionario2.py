#Escribir una función que tome un diccionario y un valor, y devuelva una lista con todas las claves asociadas
# a ese valor.
def encontrar_claves_por_valor(diccionario, valor):
    return [clave for clave in diccionario if diccionario[clave] == valor]

# Ejemplo de uso
mi_diccionario = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
valor_buscado = 1
claves_encontradas = encontrar_claves_por_valor(mi_diccionario, valor_buscado)
print(claves_encontradas)

