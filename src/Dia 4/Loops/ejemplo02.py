# Ejemplo de suma de numeros pares e impares
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares+ numero
print(f'Suma de los numeros pares {suma_pares}')
print(f'Suma de los numeros impares {suma_impares}')
