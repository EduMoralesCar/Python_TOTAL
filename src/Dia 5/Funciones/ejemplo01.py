# Ejemplo de función que suma dos números
def suma():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")
# Llamada a la función suma
suma()

# Ejemplo de función que resta dos números
def resta():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    resultado = a - b
    print(f"La resta de {a} y {b} es: {resultado}")
resta()

# Ejemplo de función que permite elegir entre suma o resta
def operacion():
    if input("¿Deseas realizar una suma o una resta? (s/r): ").lower() == 's':
        suma()
    else:
        resta()
operacion()

