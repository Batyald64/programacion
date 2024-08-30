est1 = input ("ingrese el nombre del estadio")
capac1= input ("ingrese la capacidad")

est2 = input ("ingrese el nombre del estadio")
capac2= input ("ingrese la capacidad")

est3 = input ("ingrese el nombre del estadio")
capac3= input ("ingrese la capacidad")

MayorCapacidad = capac1

if capac2>MayorCapacidad:
    MayorCapacidad = capac2
    print("el estadio ", capac2, "es el mayor capacidad ", est2)
elif capac3>MayorCapacidad:
    capac3=MayorCapacidad
    print("el estadio ", capac3, "es el mayor capacidad ",est3)
else:
    print("el estadio ", capac1, "es el mayor capacidad ", est1)