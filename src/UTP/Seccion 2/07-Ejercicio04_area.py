import math
# Crear una función que calcule el área de un círculo dado su radio.

# versión 1: validando radio y devolviendo el área o un mensaje de error
def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio
    :param radio: valor del radio
    :return: área del círculo
    """
    if radio > 0:
        return math.pi * pow(radio, 2)
    else:
        return "radio no puede ser cero o negativo"


# versión 2: validando radio y devolviendo el área o una excepción
def area_circulo_v2(radio):
    """
    Calcula el área de un círculo dado su radio
    :param radio: valor del radio
    :return: área del círculo
    """
    if radio > 0:
        return math.pi * pow(radio, 2)
    else:
        raise ValueError("radio no puede ser cero o negativo")


print(area_circulo(12))
print(area_circulo(543.65))
print(area_circulo(-55))

print(area_circulo_v2(12))
print(area_circulo_v2(543.65))


# manejando la excepción desde el cliente
try:
    print(area_circulo_v2(18.3))
    print(area_circulo_v2(-24))
except ValueError as e:
    print(e)
