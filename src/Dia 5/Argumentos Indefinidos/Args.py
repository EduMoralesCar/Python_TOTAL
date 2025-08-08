# Funcion que recibe un número indefinido de argumentos y devuelve la suma de todos ellos
def suma(*args):
    total = 0

# bucle que recorre todos los argumentos recibidos
    for num in args:
        total += num
    return total

# Ejemplo de uso de la función suma
print(suma(1,2,3,4,5,6,7,8,9,10))
print(suma(10, 20, 30))


# Ejemplo 01
# Suma de los cuadrados de los argumentos
print("\nEjemplo 1:")
def suma_cuadrados(*args):
    total = 0

    for num in args:
        total += num ** 2
    return total

print("Suma de los cuadrados:")
print(suma_cuadrados(1, 2, 3))


# Ejemplo 02
# Suma de los valores absolutos de los argumentos
print("\nEjemplo 2:")
def suma_absolutos(*args):
    total = 0

    for num in args:
        total += abs(num) # abs() devuelve el valor absoluto del número
    return total

# Ejemplo de uso de la función suma_absolutos
print("Suma de los valores absolutos:")
print(suma_absolutos(1, 2, 3, -4))


# Ejemplo 03
# Agrupando nombre y números
print("\nEjemplo 3:")
def numeros_persona(nombre, *args):
    total = 0
    for num in args:
        total += num
    return f"{nombre}, la suma de tus números es {total}"

# Ejemplo de uso correcto:
print(numeros_persona("Aldo", 1, 2, 3, 4))
