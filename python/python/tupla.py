#las tuplas son  similiar a la listas pero tiene  difencias 1) no son mutables
#2) una vez creada no se puede modificar o agregar elementos 
#3) las tuplas llevan parentesis y coma, en cambio la listas llevan corchetes

tupla =("python", "javascript","c", "c++")

print(tupla) #imprime tupla
print(type(tupla)) 
print(len(tupla))
print(tupla[0])

for i in tupla: #iterar la tupla
    print(i)