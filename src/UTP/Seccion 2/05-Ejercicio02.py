'''
Crear una funcion que calcule el área
de un círculo dado su radio.

Sabemos:
        Area = π . r²
'''

# Solucion 1

import math

def area_circulo(radio):
    if radio >= 0:
        return math.pi * pow(radio, 2)
    else:
        return "Radio no valido"

resultado = area_circulo(100)
print(resultado)


print() # Salto de linea

# Solucion 2
def areaCirculo(radio):
    if radio >= 0:
        return math.pi * pow(radio, 2)
    else:
        return "Radio no valido"

try:
    print(area_circulo(100))
    print(area_circulo(14))
    print(area_circulo(18.5))
except Exception as e:
    print(e)