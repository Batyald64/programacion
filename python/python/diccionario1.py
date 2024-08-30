#escribir un programa que pregunt al usuario 
#el nombre, edad, direccion y lo guarde en un diccionario
# mostrar por pantalla el diccionario...

nombre= str(input( "ingrese el nombre"))
edad= int(input( "ingrese la edad"))
direccion= str (input( "direccion"))

usuario= {"nombre":nombre, "edad":edad,"direccion":direccion}

print(usuario)

print (usuario["nombre"], "tiene",usuario["edad"],"años y vive en la direccion",usuario["direccion"])