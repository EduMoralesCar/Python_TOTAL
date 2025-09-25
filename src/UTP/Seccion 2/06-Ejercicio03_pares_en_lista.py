# Escribir una función que devuelva los números pares de una lista.

# metodo tradicional
def obtener_pares(lista):
    """
    Devuelve una lista con los números pares obtenidos 
    a partir de la lista proporcionada
    :param lista: lista de entrada
    :return: lista conteniendo números pares
    """
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# método optimizado
def obtener_pares_v2(lista):
    """
    Devuelve una lista con los números pares obtenidos a partir de la lista proporcionada
    :param lista: lista de entrada
    :return: lista conteniendo números pares
    """
    return [numero for numero in lista if numero % 2 == 0]

lista_numeros = [3, 15, 4, 16, 8, 21, 9, 44, 23, 28, 16]
print(obtener_pares(lista_numeros))
print(obtener_pares_v2(lista_numeros))
print(obtener_pares_v2([1, 3, 5, 7]))

'''
Una comprensión de lista (o list comprehension) es una forma 
compacta y eficiente de crear listas en Python. Permite construir 
una nueva lista aplicando una expresión a cada elemento de una 
secuencia (como una lista, rango, etc.), opcionalmente filtrando 
esos elementos mediante una condición.
'''