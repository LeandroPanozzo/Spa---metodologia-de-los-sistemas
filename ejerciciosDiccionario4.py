# *Crear una función que reciba una lista de diccionarios, cada uno representando a una persona con nombre y 
# edad. La función debe devolver una lista ordenada de personas por edad.
def ordenar_personas_por_edad(lista_personas):
    #El parámetro key en sorted() permite definir la función de clave que se usará para la ordenación.
    #lambda persona: persona['edad'] es una función anónima que toma un diccionario persona y devuelve su valor asociado a la clave 'edad'
    return sorted(lista_personas, key=lambda persona: persona['edad'])

# Diccionario de personas con dos claves: 'nombre' y 'edad'
personas = [
    {'nombre': 'Ana', 'edad': 25},
    {'nombre': 'Juan', 'edad': 30},
    {'nombre': 'Pedro', 'edad': 20},
    {'nombre': 'María', 'edad': 28}
]

personas_ordenadas = ordenar_personas_por_edad(personas)
print(personas_ordenadas)
