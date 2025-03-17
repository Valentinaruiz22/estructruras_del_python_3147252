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
if edad >=18:
    print("puedes votar")
elif edad == 17:
    print("puedes votar el proximo año")
elif edad < 17:
    print("no puedes votar aun")
print("Fin del programa")