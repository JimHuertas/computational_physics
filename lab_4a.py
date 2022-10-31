""" LABORATORIO IV"""
"""
2. A partir de la segunda ley de movimiento de Newton y la ley de gra-
vitación universal realice un código que permita determinar el valor de
la gravedad para cualquier planeta del sistema planetario solar.
"""

#Gravedad de los planetas sstema solar
from time import sleep


def fuerza_gravedad():
    f = 0 #Fuerza de la gravedad 
    masa_sol = 1.989 * pow(10,30)
    masa_2 = float(input("Masa del planeta(Kg): "))
    r = float(input("distancia entre ambas masas (m): "))
    G = 6.672 * pow(10, -11) #En N(m)^2/(Kg)^2
    
    #Las leyes de Newton del movimiento y la ley de la Gravedad
    f = (G*masa_sol*masa_2)/pow(r,2)
    print("Fuerza de Gravedad:", "%.4g" % f, " N(m)^2/(Kg)^2")

def fuerza_gravedad_planetas():
    masa_sol = 1.989 * pow(10,30)
    masa_planeta = 0.0
    G = 6.672 * pow(10, -11) #En N(m)^2/(Kg)^2
    r = 0.0 #En Km
    print("de que planeta deseas saber su Fuerza de Gravedad:\n",
            "\t(1) Mercurio.\n",
            "\t(2) Venus.\n"
            "\t(3) Tierra.\n"
            "\t(4) Marte.\n"
            "\t(5) Júpiter.\n"
            "\t(6) Saturno.\n"
            "\t(7) Urano.\n"
            "\t(8) Neptuno.\n"
            "\t(0) Salir")
    while True:
        opc = int(input("Opc: "))
        match(opc):
            case (1):#Mercurio
                masa_planeta = 3.285 * pow(10, 23)
                r = 5.79 * pow(10,10)
                f = (G * masa_sol*masa_planeta)/pow(r,2)
                print("Fuerza de Gravedad de Mercurio: ", "%.4g" % f)
            case (2): #Venus
                masa_planeta = 4.83 * pow(10, 24)
                r = 1.08 * pow(10,11)
                f = (G * masa_sol*masa_planeta)/pow(r,2)
                print("Fuerza de Gravedad de Venus: ", "%.4g" % f)
            case (3): #Tierra
                masa_planeta = 5.98 * pow(10, 24)
                r = 1.49 * pow(10, 11)
                f = (G * masa_sol*masa_planeta)/pow(r,2)
                print("Fuerza de Gravedad de Tierra: ", "%.4g" % f)
            case (4): #Marte
                masa_planeta = 6.40 * pow(10, 23)
                r = 2.28 * pow(10,11)
                f = (G * masa_sol*masa_planeta)/pow(r,2)
                print("Fuerza de Gravedad de Marte: ", "%.4g" % f)
            case (5): #Jupiter
                masa_planeta = 1.90 * pow(10, 27)
                r = 7.78 * pow(10,11)
                f = (G * masa_sol*masa_planeta)/pow(r,2)
                print("Fuerza de Gravedad Jupiter: ", "%.4g" % f)
            case (6): #Saturno
                masa_planeta = 5,98 * pow(10, 26)
                r = 1.43 * pow(10,12)
                f = (G * masa_sol*masa_planeta)/pow(r,2)
                print("Fuerza de Gravedad de Saturno: ", "%.4g" % f)
            case (7): #Urano
                masa_planeta = 8,67 * pow(10, 25)
                r = 2.87 * pow(10,12)
                f = (G * masa_sol*masa_planeta)/pow(r,2)
                print("Fuerza de Gravedad de Urano: ", "%.4g" % f)
            case (8): #Neptuno
                masa_planeta = 1.05 * pow(10, 26)
                r = 4.50 * pow(10,12)
                f = (G * masa_sol*masa_planeta)/pow(r,2)
                print("Fuerza de Gravedad de Neptuno: ", "%.4g" % f)
            case(0):
                break
            case _:
                print("Elige una opcion valida")
        sleep(2)
    return 0


if __name__ == "__main__":

    while True:
        opc = 0
        print("(1) Consultar Fuerza entre Gravedad de los planetas al sol (Sistema Solar)")
        print("(2) Consultar la Fuerza de Gravedad de un planeta (En el sistema solar)")
        opc = int(input("Opc: "))
        if(opc == 1 or opc == 2):
            if(opc == 2):
                fuerza_gravedad()
            elif(opc == 1):
                fuerza_gravedad_planetas()
        else:
            print("Error elige una opcion valida")

    

