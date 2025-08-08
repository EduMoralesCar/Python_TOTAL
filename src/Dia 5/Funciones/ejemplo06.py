import random

# Lista de ejemplo
lista_numeros = [10, 20, 30, 40, 50]

# Función que lanza una moneda
def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

# Función que evalúa el resultado del lanzamiento
def probar_suerte(resultado_moneda, lista):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista

# Ejemplo de uso
resultado = lanzar_moneda()
lista_resultado = probar_suerte(resultado, lista_numeros)

print("Resultado del lanzamiento:", resultado)
print("Lista final:", lista_resultado)
