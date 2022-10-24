#MOVIMIENTO ARMONICO SIMPLE
#funcion: desplazamiento X
import numpy as np
import matplotlib.pyplot as plt

def MAS_t(amplitud, pulsacion, fase_inicial, tiempo):
    return amplitud * np.cos((pulsacion * tiempo) + fase_inicial) 

if __name__ == "__main__":
    A = float(input("Amplitud (A cm): "))
    periodo = float(input("periodo (T s): "))
    pulsacion = 2*np.pi/periodo
    fase_inicial = float(input("Fase inicial (ϕ0 grados): "))
    #grados a radianes
    fase_inicial = (fase_inicial * np.pi)/(180)
    t = int(input("tiempo (t s): "))
    print("Posicion X en el tiempo (t): ", t, " = ", MAS_t(A, pulsacion, fase_inicial, t))

    x = t = np.arange(0.0, float(t), 0.01)
    y = A*np.cos(pulsacion*t+fase_inicial)
    plt.plot(x,y)
    plt.xlabel('tiempo t (s)')
    plt.ylabel('desplazamiento x (cm)')
    plt.title("Desplazamiento X tiempo")
    plt.show()






    
