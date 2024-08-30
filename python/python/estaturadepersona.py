#almacenar la altura de 6 personas (valores float)
#obtener el promedio de la altura de la mismas
#contar cuantas personas son mas altas que el promedio  de la estatura y
#cuantas son mas bajas que el promedio

print ("ingresa 6 alturas de diferentes personas")

alturas=[]

for i in range(6):
    alturas.append(float(input("ingrese la altura de 6 personas")))

promedio= sum(alturas)/6
bajos_promedio = 0
i=0
for i in range(6):
    if alturas [i]< promedio:
       bajos_promedio= bajos_promedio + 1 

print("el promedio de las alturas es: ", promedio)
print ("la cantidad de promedio bajo es: ", bajos_promedio)

