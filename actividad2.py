# Describcion: actividad2
'''
Elabore un programa en python
que determine si uted puede:
a) casarse
b) comprometerse 
c) quedarse soltero
con base en las siguientes 
caracteristicas (variables):
-estado civil (string =
        "soltero", "casado","compromtico")
-edad(int)
-temperamento(string =
         "buena persona","mala persona"
-fisico(string= "lindo/a", "feo/a")
'''
estado_civil =input("ingresa tu estado civil:(soltero/casado/comprometido)")
edad = int(input("ingresa tu edad:"))
tempermento= input("ingresa tu temperamento:(buena persona/mala persona)")
fisico = input("ingresa el fisico:(lindo/a/feo/a)")
salario= int( input("ingresa tu salario:(2000000/3000000"))

if estado_civil == "casado" or estado_civil == "compromtido":
    print("no puedes casarte con esa persona,porue ya tiene compromiso")
elif edad < 18:
    print("no puedes acercarte a esta persona, porque no tienes la suficiente edad")
elif tempermento == "mala persona":
    print("no puedes acercarte a esta persona, porque  te genera stress")
elif fisico == "feo":
    print ("no puedes acercarte a esta persona, porque no te atrae fisicamente ")
elif salario < 2000000:
    print("no puedes acercarte a esta persona porque no tienes la suficiente capacidad financiera")
else:
    print("puedes acercarte a esta persona")
print("fin del pograma")

