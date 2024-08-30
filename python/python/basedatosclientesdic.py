#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su DNI, 
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú:
# (1) Añadir cliente, 
# (2) Eliminar cliente, 
# (3) Mostrar cliente,
# (4) Listar todos los clientes,
# (5) Listar clientes preferentes,
# (6) Terminar.
# En función de la opción elegida el programa tendrá que hacer lo siguiente:

#Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#Preguntar por el DNI del cliente y eliminar sus datos de la base de datos.
#Preguntar por el DNI del cliente y mostrar sus datos.
#Mostrar lista de todos los clientes de la base datos con su DNI y nombre.
#Mostrar la lista de clientes preferentes de la base de datos con su DNI y nombre.
#terminar el programa.

clientes = {}

def agregar_cliente():
    print("Ingrese los datos del cliente:")
    dni= float (input("ingresa el dni del cliente:  "))
    nombre= input("nombre del cliente: ")
    direccion= input("direccion del cliente: ")
    telefono= float (input("telefono del cliente: "))
    correo= input("correo del cliente: ")
    preferente= input("preferente del cliente: ")
    
    datos_clientes = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "correo": correo,
        "preferente": preferente == "s"
    }
    clientes[dni] = datos_clientes
    print("Cliente agregado correctamente")
    menu()
  
def eliminar_cliente():
    try:
        dni= float (input("ingrese el dni del cliente a eliminar:  "))
    except ValueError:
        print("DNI no válido")
        eliminar_cliente()
    if dni in clientes:
        del clientes[dni]
        print("Cliente eliminado correctamente")
    else:
        print("Cliente no encontrado")
        eliminar_cliente()
    menu()

def mostrar_cliente():
    dni= float (input("ingrese el dni del cliente a mostrar:  "))
    if dni in clientes:
        print ("los datos del cliente solicitado son: ")
        print(clientes[dni])
    else:
        print("Cliente no encontrado")
        mostrar_cliente()
    menu()

def listar_clientes():
    print("Listado de todos los clientes:")
    for dni, datos in clientes.items():
        print(f"DNI: {dni}, Nombre: {datos['nombre']}")
    menu()

def listar_clientes_preferentes():
    print("Listado de clientes preferentes:")
    for dni, datos in clientes.items():
        if datos["preferente"]:
            print(f"DNI: {dni}, Nombre: {datos['nombre']}")
    menu()

def menu():
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    opcion= int (input("seleccione una opcion: "))
    
    if opcion == 1:
        agregar_cliente()
    elif opcion == 2:
        eliminar_cliente()
    elif opcion == 3:
        mostrar_cliente()
    elif opcion == 4:
        listar_clientes()
    elif opcion == 5:
        listar_clientes_preferentes()
    elif opcion == 6:
        print("terminando el programa")
        exit()

menu()