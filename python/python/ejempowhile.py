#realiazar la carga de valores enteros por teclado, almacenarlos en una lista
#finalizar la carga de enteros al ingresar el numero cero
#mostrar el tamaño final de la final de la lista metodo len()

enteros = []
num=int(input("ingrese un valor (0 para finalizar)"))
while num!=0:
    enteros.append(num)
    num=int(input("ingrese un valor (0 para finalizar)"))

print(enteros)
print(len(enteros))
