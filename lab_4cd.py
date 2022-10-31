
import math
"""
3. Implementar un código computacional para la solución de la segunda
ley de Kepler.
4. Implementar un código computacional para determinar la solución de
la tercera ley de Kepler para cualquier planeta que describa una órbita
elíptica."""

def SegundaKepler(L,M,t):
    return L/2*M*t

def TerceraKepler(K, r):
    return math.sqrt(K*(r**3))

if __name__ == "__main__":
    opc = 0
    while True:
        print("Leyes de Kepler"
        "\n(1)2da ley o Ley de areas"
        "\n(2)3ra ley o Ley de periodos"
        "\n(0) Salir")
        opc = int(input("Opc: "))
        if(opc == 1):
            L = float(input("Momento angular (L): "))
            t = float(input("tiempo (t): "))
            M = float(input("masa (m Kg): "))
            print("Momento lineal es: ", SegundaKepler(L,M,t))
        elif(opc == 2):
            m = float(input("masa del planeta (m Kg): "))#masa
            G = 6.673 * pow(10, -11) #En N(m)^2/(Kg)^2
            k = 4 * math.pi**2 / m*G # constante
            r = float(input("Radio o semieje mayor de la órbita del planeta (r): "))
            print("El Periodo es: ", TerceraKepler(k, r))
        elif(opc == 0):
            break
        else:
            print("Escoge una opcion valida")

    
