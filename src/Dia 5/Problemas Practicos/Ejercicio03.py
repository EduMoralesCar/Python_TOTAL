def tiene_doble_cero(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True                         # Encontramos un par de ceros consecutivos
    return False                                # No se encontraron ceros consecutivos

# Ejemplos de prueba
print(tiene_doble_cero(5, 6, 1, 0, 0, 9, 3, 5))  # True
print(tiene_doble_cero(6, 0, 5, 1, 0, 3, 0, 1))  # False