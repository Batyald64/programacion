#items () devuelve las key (claves)y values (valores) del diccionario
d={"a":1, "b":2, "c":3, "d": 4 } 
id=d.items ()
print(id)
#print(d.items())

#key() devuelve la lista de las key (claves)

k=d.keys() #devuelve la lsita de claves
print(k)
print(list(k)) #imprime como lista

#values() devuelve una lista los valores del diccionario

v=d.values()
print(v)#muesta los valores
print(list(v)) #imprime como lista

#pop() busca y elimina la clave que se pasa como parametro y devuelve su valor asociado

#d.pop()
#print(d)

#popitem () busca y elimina claves aleatorias

d.popitem()
print(d)

#update() se llama sobre el diccionario y tiene como entrada otro diccionario

d2={"b":2, "c":3, "d":4, "e":5}

d.update(d2)
print(d)