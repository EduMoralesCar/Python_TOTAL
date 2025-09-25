'''
Escribir una función que devuelva los numeros pares de una lista
'''

# Lista
numeros = [1,2,3,4,5,6,7,8,9]
lista = [2,15,3,16,8,21,9,44,23,28,16,29]

def numPares(numeros):
    resultado = []
    for num in numeros:
        if num % 2 == 0:
            resultado.append(num)
    return resultado

def numImpares(numeros):
    resultado = []
    for num in numeros:
        if num % 2 != 0:
            resultado.append(num)
    return resultado


# Imprimimos las listas de numeros
print('Lista de numeros:\n', numeros, '\n', lista, '\n')

print("Numeros Pares:\n",
      numPares(numeros), '\n',
      numPares(lista))

print() # Salto de linea

print("Numeros Impares:\n",
      numImpares(numeros), '\n',
      numImpares(lista))
