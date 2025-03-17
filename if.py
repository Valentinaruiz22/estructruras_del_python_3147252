'''
Estructura de control if:
se utiliza para tomar decisiones 
basadas en expresiones condicionales
'''
#ejemplo:1 if SIMPLE
edad = int (input("Ingresa tu edad:"))
documento = input ("Tienes documento?(si/no):")
#condicional: si la edad es mayor o igual a 18 
if edad > 18 and documento =='si':
    #codigo para cuando es mayor de 18
    print("Eres mayor de edad y tienes documento, puedes votar")
else:
    #codigo para cuando es menor de 18
    print("Eres menor de edad o no tines documento, no puedes votar")
    #codigp que se ejecuta siempre 
    print("Fin del programa")