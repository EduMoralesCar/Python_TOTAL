for indice, numero in enumerate(range(10, 20)):
    print(indice, numero)

# Enumerar una lista
lista = ['a', 'b', 'c', 'd']
misTuples = list(enumerate(lista))
print(misTuples)

print()
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

print()
lista_indices = list(enumerate("Python"))
print(lista_indices)