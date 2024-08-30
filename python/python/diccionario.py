#diccionarios me permite almacenar valores de distintos tipos de datos y estan formados por llave (key)y valor
# estructura de datos mutables
# los diccionarios llevan llaves {} y la coma (clave:valor, )

diccionario = {
    "nombre" : "juan",
    "apellido" : "perez",
    "edad" : 35,
    "estatura" : 1.75,
    "peso" : 70,
    "hobbies" : ["leer", "dormir", "comer"],
    "direccion" : {
        "calle" : "calle 1",
        "numero" : 123}
    }
print (diccionario)

diccionario1=dict([
    ("nombre", "juan"), ("edad", "35"), ("estatura", "175"), 
])
print(diccionario1)

print (diccionario["edad"])
