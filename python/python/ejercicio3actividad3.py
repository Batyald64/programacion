#El gerente de ventas de Mercado Libre desea habilitar Envíos Gratis para compras a partir de los 15.000
#pesos. Se necesita un programa que ingrese el monto de la compra, e informe al usuario si accede o no al
#beneficio.

monto= int(input("ingrese el valor del producto"))
if monto>15000 :
    print("el producto tiene envio gratis")
else:
    print ("el producto no le corresponde ningun beneficio")    