#escribir un programa simulando una cesta de compras. el programa debe preguntar que articulo y su 
#precio y añadir el par al diccionario, hasta que el usuario decida terminar
#despues mostrar por la pantalla la lista de la compra y el costo total. con siguentes formatos
#lista de compras.
#articulo     precio
#ej1          $2.5
#ej2          $3.5

cesta={}
cantidaddeprocutos=int(input("ingrese la cantidad de articulos"))

for articulos in range(cantidaddeprocutos):
    articulos= str(input("ingrese el nombre del articulo"))
    precio= float (input("ingrese el valor"))
    cesta[articulos]=precio

print ("la lista de compra es: ")

for articulos, precio in cesta.items():
    print (articulos, precio)
     
total=sum(cesta.values())
print("el costo total es de  :",total )
