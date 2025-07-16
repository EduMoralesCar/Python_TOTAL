from random import randint

intentos = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensando en un número entre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    respuesta = int(input("Cuál es el numero?: "))
    intentos += 1

    if respuesta < numero_secreto:
        print('Mi numero es mas alto')
    if respuesta > numero_secreto:
        print('Mi numero es mas bajo')
    if respuesta == numero_secreto:
        print(f"\nFelicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break
if respuesta != numero_secreto:
    print(f"\nLo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")