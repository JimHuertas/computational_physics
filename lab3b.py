#MOVIMIENTO ARMONICO FORZADO
#funcion: desplazamiento X
import numpy as np

if __name__ == "__main__":
    m = float(input("masa (m N): "))
    f_0 = float(input("Fuerza inicial (F0 N): "))
    w_0 = float(input("pulsacion inicial (ω0): ")) #ω0
    w = float(input("puslacion actual (ω): ")) #ω
    t = float(input("tiempo (t s): "))
    b = float(input("b: "))
    fase_inicial = float(input("Fase inicial (ϕ0 grados): "))
    #grados a radianes
    fase_inicial = (fase_inicial * np.pi)/(180)
    #amplitud A
    A = (f_0/m) / np.sqrt(pow(pow(w,2) 
        - pow(w_0,2),2) 
        + pow((b*w)/m, 2))

    desplazamiento = A * np.cos(w*t + fase_inicial)
    print("Desplazamiento de un MAF, en un tiempo t: ", desplazamiento)