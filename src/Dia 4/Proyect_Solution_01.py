import random

def juego_adivina_numero():
    nombre = input("¡Hola! ¿Cómo te llamas?: ")
    print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número\n")

    numero_secreto = random.randint(1,100)
    intentos_restantes = 8

    while intentos_restantes > 0:
        try:
            respuesta = int(input("Elige un número entre 1 y 100: "))

            if respuesta < 1 or respuesta >100:
                print("Has elegido un número que no está permitido. Por favor, intenta nuevamente.")
                continue

            if respuesta < numero_secreto:
                print("Incorrecto. El número que has elegido es menor al número secreto.")
            elif respuesta > numero_secreto:
                print("Incorrecto. El número que has elegido es mayor al número secreto.")
            else:
                print(f"¡Felicidades, {nombre}! Has adivinado el número secreto ({numero_secreto}) en {9 - intentos_restantes} intento(s).")
                break

            intentos_restantes -= 1

            if intentos_restantes > 0:
                print(f"Te quedan {intentos_restantes} intento(s).")
            else:
                print(f"\nLo siento, {nombre}. Se te acabaron los intentos. El número secreto era {numero_secreto}.")

        except ValueError:
            print("Por favor, ingresa un número válido.")
if __name__=="__main__":
    juego_adivina_numero()