"""CREA UN PROGRAMA CON EL CUAL PODAMOS GUARDAR LOS NOMBRES Y LAS INDENTIFICACIONES DE MULTIPLES PERSONAS
(NO SABEMOS CUANTAS) SIN PERDER NINGUNA DE ELLAS. EL USUARIO ES EL ENCARGADO DE SUMINISTRAR LA INFORMACION
DE CADA PERSONA. EL USUARIO INGRESA LA CANTIDAD DE PERSONAS QUE DESEA AGREGAR"""


nombres=[]
identificaciones=[]

tamaño = int(input("ingrese la cantidad de nombres que desea agregar: "))

for i in range(tamaño):
    print( "ingrese el nombre de la persona", i+1)
    nombre= input("Nombre: ")
    identificacion= input("identificacion: ")
    
    nombres.append (nombre)
    identificaciones.append (identificacion)

print (nombres)
print (identificaciones)


for i in range(tamaño):
    print("mostrar los valores agregados: ", i+1)
    print("mostrar el nombre agregado: ", nombres[i])
    print( "mostrar su identificacion: ",identificaciones[i])

