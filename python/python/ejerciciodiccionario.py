#hacer un  codigo para manejar una base datos de una empresa. habra un diccionario principal 
#en el que la clave de cada cliente sera DNI y el valor sera otro diccionario con los datos del clientes (nombres, apellidos, correo)
#el programa debe preguntar al usuario por una opcion del siguiente menu (1)añadir cliente, 2) eliminar cliente , 3) mostrar cliente
#4) terminar

#a) pedir lo datos necesarios, agregar  un cliente nuevo y mostrar  el diccionario
#b)pedir un dni y eliminar cliente. en cada que exista, debe avisar por mensaje
#c)pedir el dni y mostrar los datos en un mensaje (nombre, apellido y correo) . mostrar un error si no lo encuentra
#d)vaciar el diccionario, mostrandolo y mostrar mensaje de despedida.

clientes={}
cantidadclientes=int(input("ingresa la cantidad de clientes que ingresaras"))

for persona in range(cantidadclientes):
    nombre=str(input("ingrese el nombre: "))
    while nombre in clientes:
       print("el cliente ya esta ingresado")
       nombre=str(input("ingrese el nombre: "))
    dnir=[]
    dni=float(input("ingrese el documento de identificacion: "))
    while dni>0:
        dnir.append(dni)
        dni=float(input("ingrese el documento de identificacion: "))
    clientes[nombre]=dnir.copy
