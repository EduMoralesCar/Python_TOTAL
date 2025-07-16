for numero in range(1,5):
    print(numero)

lista = list(range(1,101,10))
print(lista)
print()
# Ejemplos
ejemplo1 = list(range(2500,2586,30))
print(ejemplo1)
print()
#crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive).
ejemplo2 = list(range(3,301,10))
print(ejemplo2)
print()
# Utiliza la función range() y un loop para sumar los cuadrados de todos
# los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.
suma_cuadrados = 0
lista1 = list(range(1,16))
for numero in lista1:
    suma_cuadrados = suma_cuadrados + numero**2
print(suma_cuadrados)

# Otra manera de realizar la suma de cuadrados de 1 a 15
suma_cuadrado = sum(i**2 for i in range(1,16))
print(suma_cuadrado)