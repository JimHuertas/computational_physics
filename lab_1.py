from distutils.log import error

def MRU_d (V, t):
    if(V, t > 0):
        return V * t
    else:
        error

def MRUV_d(V, t, a):
    if(V, t > 0):
        return (V*t)+(1/2)*a*pow(t,2)

def MRUV_Vf(V, t, a): 
    if(V,t > 0):
        return (V*t)+(a*t)

def main():
    while(True):
        opc = int(input('Que desea calcular\n(1) Distancia(d) en MRU\n(2) Distancia(d) en MRUV\n(3) Velocidad Final(Vf) en MRUV\n(0) Salir\nOpcion: '))
        if(opc == 1):
            V = float(input('Velocidad(m/s): '))
            t = float(input('Tiempo(s): '))
            print("\n \nResultado: ",MRU_d(V,t), "m\n\n")
        elif(opc == 2):
            V = float(input('Velocidad(m/s): '))
            t = float(input('Tiempo(s): '))
            a = float(input('Aceleracion (s): '))
            print("\n \nResultado: ",MRUV_d(V,t,a), "m\n\n")
        elif(opc == 3):
            V = float(input('Velocidad(m/s): '))
            t = float(input('Tiempo(s): '))
            a = float(input('Aceleracion (s): '))
            print("\n \nResultado: ",MRUV_Vf(V,t,a), "m/s\n\n")
        else:
            break

main()
