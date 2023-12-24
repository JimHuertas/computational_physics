#Serie Leibniz para pi

#Metodo de montecarlo para pi
import numpy as np
import random


#Valores de integraciony valor teorico
a = 0 
b = np.pi
N = 1000
vteo = 2 

#Matriz de ceros de largo N
ar = np.zeros(N)

#Iteracion sobre cada valor de la matriz ar y l e asignamos un valor aleatorio que va de 0 a pi
for i in range(len(ar)):
    ar[i] = random.uniform(a,b)

#Variable que almacene la suma de las funciones 
integral = 0.0

#Definir la funcion que vamos a integrar
def f(x):
    return np.sin(x)

#Funcion que itere y sume los valores diferentes de X
for i in ar:
    integral += f(i)
res = (b-a)/float(N)*integral
erel = ((vteo-res)/vteo)*100

#Solucion de la integral
print("Para el numero de iteraciones {}.".format(N))
print("El valor calculado analiticamente es {}.".format(vteo))
print("EL valor calculado por Metodo Monte Carlo es {}.".format(res))
print("EL error relativo es {}.".format(erel))


def main():
    a=0


if __name__ == "__main__":
    main()