'''
if en cascada:
Estructura de control que permite
evaluar varias condiciones en 
cascada, es decir, si la primera
condicion no se cumple, 
se evalua la siguiente 
y asi sucesivamente.
'''
#Ejemplo 1:




edad = int(input("ingresa tu edad:"))
if edad > 18:
    print("puedes votar")
elif edad == 18:
    print("Bienvenido ciudadano puedes votar con la contraseña")
elif edad < 17:
 print("no puedes votar aun") 
elif  edad > 10:
    print("Eres muy peque, tienes registro civil")
elif edad < 17:
 print("no puedes votar aun") 
print("Fin del programa")
