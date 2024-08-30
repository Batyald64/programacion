cola=[]
pila=[]

def agregar_elemento():
    print ("recuerda que son valores numericos al agregar")
    print ("agrega un elemento a la cola")
    elemento= float(input("Agregar elemento a la cola"))
    cola.append(elemento)
    menu_cola()
    
def Mostrar_cola():
    print("la cola es: ", cola)
    menu_cola()
           
def Eliminar_cola():
    cola.pop(0)
    print (" el elemento de la cola se elimino correctamente")
    menu_cola()
   
def menu_cola():

    print("1- agregar un elemento")
    print("2- mostrar cola")
    print("3- eliminar elemento")
    print("4- salir del menu")
    
    opcion= int(input("opcion: "))
    
    if opcion == 1:
        agregar_elemento()
    elif opcion==2:
        Mostrar_cola()
    elif opcion==3:
        Eliminar_cola()
    elif opcion==4:
        print("terminando el programa")
        exit()

def agregar_elemento_pila():
    print ("recuerda que son valores numericos al agregar")
    print ("agrega un elemento a la cola")
    elemento= float(input("Agregar elemento a la cola"))
    pila.append(elemento)
    menu_pila()
    
def Mostrar_pila():
    print("la cola es: ", pila)
    menu_cola()
           
def Eliminar_pila():
    pila.pop()
    print (" el elemento de la cola se elimino correctamente")
    menu_cola()
   
def menu_pila():

    print("1- agregar un elemento")
    print("2- mostrar cola")
    print("3- eliminar elemento")
    print("4- salir del menu")
    
    opcion= int(input("opcion: "))
    
    if opcion == 1:
        agregar_elemento_pila()
    elif opcion==2:
        Mostrar_pila()
    elif opcion==3:
        Eliminar_pila()
    elif opcion==4:
        print("terminando el programa")
        exit()

def menu_principal():
    print ("1- menu cola")
    print ("2- menu pila")
    print ("3- salir")
    
    opcion= int(input("opcion: "))
    
    if opcion == 1:
        menu_cola()
    elif opcion==2:
        menu_pila()
    elif opcion==3:
        print("terminando el programa")
        exit()

menu_principal ()