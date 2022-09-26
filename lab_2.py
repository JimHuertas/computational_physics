#MAQUINA DE ATWOOD

from ast import Constant


masa1 = float(input("Peso 1: "))
masa2 = float(input("Peso 2: ")) 
aceleracion = 0
gravedad = 9.8
peso1 = masa1 * gravedad
peso2 = masa2 * gravedad
if masa1 == masa2:
    print('No existe aceleracion, por tanto es igual a 0')
elif masa1 > masa2:
    aceleracion = ((masa1-masa2)/(masa1+masa2))*gravedad
    tension = peso1 - (masa1*aceleracion)
    print('Asceleracion (a): ', round(aceleracion, 4), ' m/s^2')
    print('Tension (T):   \t', round(tension, 4), ' N')
elif masa2 > masa1:
    aceleracion = ((masa1-masa2)/(masa1+masa2))*gravedad
    tension = peso2 - (masa2*aceleracion)
    print('Asceleracion (a): ', round(aceleracion, 4))
    print('Tension (T):   \t', round(tension, 4), ' N')


    