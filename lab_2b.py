#2 : Un móvil de masa m recorre una distancia d en un tiempo t, 
# al inicio tiene una velocidad inicial vi y una 
# velocidad final vf . Escriba un código que determine 
# la fuerza que describe el móvil al momento de realizar 
# el cambio de velocidad y grafique el proceso.

import matplotlib.pyplot as plt

"""2da ley de Newton"""
def fuerza(masa, aceleracion):
    return masa*aceleracion

masa = float(input("Masa (m): ", ))
velocidad_ini = float(input("Velocidad Inicial (V_0): "))
velocidad_final = float(input("Velocidad Final (V_f): "))
tiempo = float(input("tiempo (t): "))



vector_fuerza = []
vector_tiempos = []

#recorrido del tiempo desde 0s hasta t segundos
for i in range(0, int(tiempo)):
    vector_tiempos.append(i)
    aceleracion = 0
    if(i==0): 
        aceleracion = velocidad_ini
    else:
        aceleracion = (velocidad_final - velocidad_ini)/i
    vector_fuerza.append(fuerza(masa, aceleracion))
fig, ax = plt.subplots()


ax.plot(vector_tiempos, vector_fuerza, marker = 'o')
plt.show()

