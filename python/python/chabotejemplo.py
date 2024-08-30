#ejemplo de chatbot con diccionario
#definimos el diccionario

respuesta={
    "bien":"me alegra oir eso",
    "adios":"¿adios! que tengas un buen dia",
    "hola": "como te llamas"
}

while True:
    entrada= input("yo:  ").lower ()
    if entrada in respuesta:
        print("bot:  ", respuesta[entrada])
    else:
        print("bot: no entiendo")
    if entrada == "adios":
        break    
    