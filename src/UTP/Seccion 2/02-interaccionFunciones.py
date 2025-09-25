import random

# Lanzamos 3 dados
def lanzarDados():
    return random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

def evaluarJugada(dado1, dado2, dado3):
    suma = dado1 + dado2 + dado3
    if suma <= 6:
        return f"Suma de dados: {suma}.\nGanaste!!"
    elif 6 < suma < 10:
        return f"Suma de dados: {suma}.\nEstuviste cerca de ganar!!"
    else:
        return f"Suma de dados: {suma}.\nPerdiste!!"

mensaje = "¡Buena Suerte!"
dado1, dado2, dado3 = lanzarDados()
print(evaluarJugada(dado1, dado2, dado3))
print(mensaje)