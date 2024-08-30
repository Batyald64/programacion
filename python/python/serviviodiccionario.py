#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y 
# el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, 
# pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura 
# y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el 
# número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar 
# por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.


facturas={}
numfactura=0
monto_pagado=0
def agregar_facturas():
    print ("ingrese el numero de facturas")
    numfactura= int (input ("factura: "))
    
    while numfactura in facturas:
        print ("factura ya existente")
        numfactura= int(input ("factura: "))
        
    print ("ingrese el costo de la factura: ")
    costo= float (input("monto: "))
    facturas [numfactura]= costo
    monto= sum(facturas.values())
   
    print("la factura fue agregada correctamente")
    print("sus facturas pendientes de pagos", facturas)
    print(" montos facturas pendientes", monto)


def pagar_factura():
    print ("ingrese el numero de factura a pagar: ")
    numfactura= int (input("numero de factura:  "))
    
    if numfactura in facturas:
        
        print ("factura encontrada")
        print ("costo de la factura: ", facturas [numfactura])
        print ("ingrese el monto pagado: ")
        
        monto_pagado= float (input("monto pagado: "))
        monto_pagado= facturas.pop(numfactura)
        
        print ("la factura fue pagada correctamente")
        print ("cantidad cobrada hasta el momento: ", sum(facturas.values())- monto_pagado)
        print ("cantidad pendiente de cobro: ", sum(facturas.values()) )
        print (facturas)




def terminar():
    
    print ("terminando el programa")
    print ("cantidad cobrada hasta el momento: ", sum(facturas.values())- monto_pagado)
    print ("cantidad pendiente de cobro: ", sum(facturas.values()) )
    print ("facturas pendientes de pagos", facturas)
    print ("gracias por utilizar el programa")


while True:
    print ("Menu")
    print ("1. Agregar factura")
    print ("2. Pagar factura")
    print ("3. Terminar")
    opcion= int (input("seleccione una opcion: "))
    
    if opcion == 1:
        agregar_facturas()
        
    elif opcion == 2:
        pagar_factura()
        
    elif opcion == 3:
        terminar()
        break
    
    else:
     print ("opcion incorrecta")
    





    
    