#*Crear una función que reciba un diccionario y devuelva una lista ordenada de las claves.
def ordenar_claves(diccionario):
    return sorted(diccionario.keys())

# Ejemplo de uso
mi_diccionario = {'c': 3, 'a': 1, 'b': 2}
claves_ordenadas = ordenar_claves(mi_diccionario)
print(claves_ordenadas)
