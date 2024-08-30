"""elif puede verificar varias condiciones al incluir
una o mas verificaciones de elif despues de la declaracion if inicial.
solo se ejecutara una condicion"""

edad = 8
if edad>9:
    print ("la edad es1 ",edad)
elif edad > 5:
    print("la edad es2  ", edad)
elif edad > 6:
    print("la edad es3  ", edad)
else:
    print ("la edad es4: ", edad)