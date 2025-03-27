'''
if aninados
estructuras selectivas
se encuentra dentro
de otro if
syntax:
if condicion:
    if condicion:
        if condicion:
             bloque de instr
    else:
        if condicion:
             bloque de instr
        else:
                 bloque de instr
else: 
  bloque de instruccione                                

'''

#Ejemplo 1:
# Modifcaion de ejercicio de votacion
# ahora solo puede votar si es mayor de edad 
#pero si tiene doucmento.
#mostrar explicaciones en los otros casos 
edad = int(input("ingrese su edad"))
if edad >= 18:
    documento = input("Tiene documento? (si/no):")
    if documento == "si":
        print("Usted puede votar")
    else:
        print("Usted no puede votar")
        print("Porque no tiene documento")
else:
    print("Usted no puede votar")
    print("Porque es menor de edad")
