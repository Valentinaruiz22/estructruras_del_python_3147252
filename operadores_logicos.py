'''
Operadoes lógicos 

Aquellos que operan unicamente
con valores booleanos (V F)
Acorde a las tablas 
'''

#Ejemplo 1: Operador not:
y = not True 
print("el resultado de operar con not es" ,y)

#ejemplo 2: operador and
y = False and True
print("El resultado de operador con and es" ,y)

#ejemplo 3: Operador or:
y = False or False 
print("el resultado de operar con or es" ,y)

'''
Jerarquia de predencia de operadores
(Logicos inclusive)
1.()
2.**
3.*,/,%
4.+,-
5.<,>,<=,>=,!===
6.not
7.and
8.or
9.=
'''
#ejemplo 4: Jerarqia de operadores
y = False and not True or False
print("el resultado de operar con jerarquia es" ,y)