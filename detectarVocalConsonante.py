#Determinar si una letra es vocal o consonante. Tener en cuenta que la comparación de caracteres es Case Sensitive (sensible a mayúsculas y minúsculas)
listaVocales=["A","E","I","O","U"]
esVocal=False
letra= input("Ingrese la letra: ")
letra = letra.upper()
for item in listaVocales:
    if item==letra:
        esVocal=True
        break
    
if esVocal:
    print("La letra es vocal")
else:
    print("La letra no es vocal")