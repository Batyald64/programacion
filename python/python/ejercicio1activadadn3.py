punto1= int(input("ingrese el primer valor  "))
punto2= int(input("ingrese el segundo valor  "))
punto3= int(input("ingrese el tecer valro" ))


if punto1>100:
    print ("el primer pedido tiene envio gratis")
else:
    print ("el pedido no tiene envio gratis")

if punto2>100:
    print ("el segundo pedido tiene envio gratis")
else:
    print ("el pedido no tiene envio gratis")

if punto3>100:
    print ("el tercer pedido tiene envio gatis")
else:
    print ("el pedido no tine en envio gratis")

print("la cantidad total de los pedido es: ")
pt = print (punto1+punto2+punto3)
