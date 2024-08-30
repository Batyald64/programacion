#Elabora programa que ingrese la nota del alumno, y evalué mostrando diversos mensajes: si 9≤N≤10
#🡪”Golpe de Suerte”, si 7≤N<9 🡪”Buen Machete”, si 5≤N<7 🡪”Ponele Onda”,si 0≤N<5 🡪”Ya fué”, para otros
#valores “Ingresa entre 0 y 10 bobina”.

nota= input("ingresa la nota del alumno")
if nota>=10:
    print ("golpe de suerte")
elif nota>7:
    print ("buen machete")
elif nota>5:
    print ("ya fue")
else:
    print("Ingresa entre 0 y 10 bobina")