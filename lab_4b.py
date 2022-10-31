""" LABORATORIO IV"""
"""
2. Del problema anterior realice un código para poder determinar la den-
sidad de cualquier planeta del sistema planetario solar.
"""
import math


def to_g_cm3(a):
    a = a / pow(1,-12)
    a = '%.4g' % a
    return a

def fuerza_gravedad(masa, r):
    f = 0 #Fuerza de la gravedad 
    masa_sol = 1.989 * pow(10,30)
    G = 6.672 * pow(10, -11) #En N(m)^2/(Kg)^2
    #Las leyes de Newton del movimiento y la ley de la Gravedad
    f = (G*masa_sol*masa)/pow(r,2)
    return f

if __name__ == "__main__":
    G = 6.673 * pow(10, -11) #En N(m)^2/(Kg)^2
    masa_sol = 1.989 * pow(10,30)
    #m = 5.98 * pow(10, 24)
    r = 1.49 * pow(10, 11) #En Km
    v = math.sqrt(G*masa_sol/ r)
    P = 2 * math.pi * r / v 
    #print("P:",P)

    print("Consultar Fuerza entre Gravedad de los planetas al sol (Sistema Solar)")
    masa = float(input("Masa del planeta: "))
    r = float(input("Radio del planeta: "))
    volumen = (4/3)*math.pi * r**3 #4/3 πr³
    densidad =masa/volumen
    print("Densidad del planeta es: ", to_g_cm3(densidad))
    
    # constante de proporcionalidad
    G_K = 4 * pow(math.pi,2)/G
    #velocidad radial
    #volumen del planeta
    volumen = 4/3 * math.pi * pow(r, 3)

    #DENSIDAD
    #Periodo de traslacion
    P = (2 * math.pi * r)/v
    m = 9.8 * pow(r,2) / G 
    M = G_K * pow(r,3)/pow(P,2)