# funcion con parametros y argumentos 
def informacion(mensaje):
    print (f"mensaje:{mensaje}")

informacion("hola mundo")
informacion("hoy es viernes")
informacion("ultima clase")

#parametro por defecto

def suma(a,b=2):
    print (a+b)
    

suma(3) # resultado 5 y toma por defecto el segundo parametro
suma(5,8) # resultado 13 - se remplaza el valor de b=2 por b=8