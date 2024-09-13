def to_list(tupla):
    lista = []  
    for elemento in tupla:  
        lista.append(elemento)  
    return lista  

tupla = (1, 2, 3, 4)
lista = to_list(tupla)
print(lista)  


#usando el metodo list:
tupla = (1, 2, 3, 4)
lista = to_list(tupla)
print(lista)  # Salida: [1, 2, 3, 4]
