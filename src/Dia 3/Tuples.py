# Ejemplo de uso de tuplas en Python
tuple1 = (1,2,3,4)
print(type(tuple1))

tuple2 = ('Este tiene', 5, 'partes')
print(tuple2)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(type(mi_lista))
print(mi_lista)

print()
tuple3 = ("Aldo", "Morales", 23, 1995)
tuple3 = list(tuple3)
print(tuple3)

print()
mi_tupla1 = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(f"Contamos la Cantidad de veces que aparece el valor 2 en la siguiente lista:\n{mi_tupla1}")

# Imprimir la cantidad de veces que aparece el valor 2 en la tupla
print("\nLa cantidad de veces que aparece es:", mi_tupla1.count(2))
#print(mi_tupla1.count(2))