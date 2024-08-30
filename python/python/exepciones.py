#errores de sintaxis ejemplo o errores de interpretacion  syntaxError
# exepciones : mensajes de error:  1. zeroDivisionError (division por cero), 2.  NameError (name no definido)
# 3. typeError 


while True:
    try:
        x= int (input("ingrese un numero:  "))
        break
    except ValueError:
        print ("ingreso no valido!!!")
    except NameError:
        print ("variable no definida")
    except ZeroDivisionError:
        print ("division por cero")

   
valorw= input("ingrese un numero")
              
#type error 
try:
        div= valorw / 0
except ZeroDivisionError:
        print ("division por cero")
except TypeError:
        print ("Error de tipo de dato")
        print (x)

def division_cero():
    x=10/0
    
try:
    division_cero()
except ZeroDivisionError as err:
    print ("Error de division por cero: ", err)


