#MAQUINA DE ATWOOD
#1 : Escriba un código donde se emplee máquina de Atwood 
# para determinar la magnitud de la aceleración de dos 
# objetos y la tensión en la cuerda sin peso.
masa1 = float(input("Peso 1:\t\t\t"))
masa2 = float(input("Peso 2:\t\t\t")) 
aceleracion = 0
gravedad = 9.8
peso1 = masa1 * gravedad
peso2 = masa2 * gravedad
if masa1 == masa2:
    print('No existe aceleracion, por tanto es igual a 0')

elif masa1 > masa2:
    aceleracion = ((masa1-masa2)/(masa1+masa2))*gravedad
    tension = peso1 - (masa1*aceleracion)
    print('Aceleracion (a):\t-', round(aceleracion, 4), ' m/s^2')
    print('Tension (T):\t\t', round(tension, 4), ' N')

elif masa2 > masa1:
    aceleracion = ((masa2-masa1)/(masa1+masa2))*gravedad
    tension = peso2 - (masa2*aceleracion)
    print('Aceleracion (a):\t', round(aceleracion, 4), 'm/s^2')
    print('Tension (T):\t\t', round(tension, 4), ' N')
    