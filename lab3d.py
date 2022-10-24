#CIRCUITO LCR
#funcion: carga de un circuito LCR en un tiempo t
import numpy as np

if __name__ == "__main__":
    R = float(input("Resistencia(R Ω):"))
    L = float(input("Autoinduccion (L H):"))
    t = float(input("tiempo (t s): "))
    q_0 = float(input("carga inicial (q_0): "))
    w_0 = float(input("pulsacion inicial (ω0): ")) #ω0
    fase_inicial = float(input("Fase inicial (ϕ0 grados): "))
    #grados a radianes
    fase_inicial = (fase_inicial * np.pi)/(180)
    
    y = R / 2*L
    #pulsacion
    w = np.sqrt(pow(w_0,2) - pow(y,2))

    q_t = q_0 * pow(np.e, -y*t) * np.sin(w*t + fase_inicial)
    print("Carga en el tiempo ", t, "(t): ", q_t)
