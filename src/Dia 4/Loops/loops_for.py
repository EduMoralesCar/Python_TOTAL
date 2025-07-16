nombres = ['Ximena', 'Brittany', 'Mila', 'Maddi', 'Keyla', 'Yatziri']

for elementos in nombres:
    print('Bienvenido ' + elementos)


print('\n')


palabra = 'HOLA'
for letra in palabra:
    print(letra)


# Ejemplo de suma de numeros pares e impares otro manera de realizar la misma condicion
print('\nintento de realizar la prueba de num % 2 == 1 (valores impares)')
lista = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sumaPares = 0
sumaImpares = 0
for numero1 in lista:
    if numero1 % 2 == 1:
       sumaImpares = sumaImpares + numero1
    else:
        sumaPares = sumaPares + numero1
print(f'Suma de los numeros pares {sumaPares}')
print(f'Suma de los numeros impares {sumaImpares}')