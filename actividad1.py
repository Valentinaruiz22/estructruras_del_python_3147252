motor_encendido = True

temperatura = int(input("cual es la temperatura del motor"))

if  temperatura > 80:
    motor_encendido = False
    print("temperatura es muy alta, se apagara el motor ")
else:
    print("La temperatura es baja, el motor sigue encendido")
