#realice un programa que nos permita guardar llos nombres de los alumnos de una clase
#y las notas que han obtenidos. cada alumno pueden tener distintas cantidad de notas 
#guardar la informacion dicionario cuya clave sera los nombres de los alumnos 
#y los valos seran lista de las notas de cada alumnos

#el programa me tiene que pedir cuantos alumnos a registrar y el nombre de los mismos 
#para terminar la carga de las notas debe solicitar una nota negativa.
#al finalizar la carga mostrar la lista de los alumnos y nota promedio 
#si introduce un alumno que ya existe el programa  nos dara un mensaje 

alumnos={}
cantidad= int(input("ingresa la cantidad de alumnos a registrar"))
for num in range(cantidad):
    nombre=str(input("ingrese el nombre del alumno:  "))
    while nombre in alumnos:
        print("el alumno ya existe")
        nombre=str(input("ingrese el nombre del alumno:  "))
    notas=[]
    nota=float(input("Ingrese la nota del alumno (negativo para terminar)"))
    while nota>0:
        notas.append(nota)
        nota=float(input("Ingrese la nota del alumno (negativo para terminar)"))
    alumnos[nombre]=notas.copy()

for nombre, notas in alumnos.items():
    print("se ha sacadola nota promedio  :", (nombre, sum(notas)/len(notas))  )
                 