#CIRCUITO LC
#funcion: carga de un circuito LC en un tiempo t
import numpy as np

if __name__ == "__main__":
    L = float(input("Autoinduccion (L H):"))
    C = float(input("Capacintancia (C F)"))
    t = float(input("tiempo (t s): "))
    q_0 = float(input("carga inicial (q_0): "))
    fase_inicial = float(input("Fase inicial (ϕ0 grados): "))
    #grados a radianes
    fase_inicial = (fase_inicial * np.pi)/(180)
    #pulsacion
    w = 1 / np.sqrt(L*C)
    q_t = q_0 * np.sin(w*t + fase_inicial)
    
    print("Carga en el tiempo ", t, "(t): ", q_t)