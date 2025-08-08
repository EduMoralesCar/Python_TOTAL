import random

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def evaluar_jugada(dado1, dado2):
    suma = dado1 + dado2
    if suma <= 6:
        return f"La suma de tus dados es {suma}. Lamentable"
    elif 6 < suma < 10:
        return f"La suma de tus dados es {suma}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma}. Parece una jugada ganadora"

mensaje = "¡Buena suerte!"
dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1, dado2))
print(mensaje)
