#Calcular el descuento de una compra. Si la compra es mayor o igual de $100, el descuento será de 10%. Si es menor, 5%. Mostrar el monto final a pagar.
valor = float(input("ingrese el monto: "))

if(valor>=100):
    descuento = valor*0.10
else:
    descuento= valor*0.05
    
    
total= valor-descuento
print(f"El monto a pagar es: {total}")