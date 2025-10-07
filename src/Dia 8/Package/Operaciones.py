numeros = [1,2,3,4,5,6,7,8,9,10]

# Funciones para realizar operaciones con la lista de números
# Imprimir números pares
def numPares():
    '''for num in numeros:
        if num % 2 != 0:
            print(num)'''
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(pares)

# Imprimir números impares
def numImpares():
    impar = list(filter(lambda x: x % 2 != 0, numeros))
    print(impar)

# Imprimir la longitud de la lista
def longitudLista():
    print(len(numeros))

# Imprimir la suma de los números en la lista
def sumaLista():
    print(sum(numeros))
