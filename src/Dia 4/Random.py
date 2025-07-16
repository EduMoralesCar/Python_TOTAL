from random import *

aleatorio01 = randint(1,50)
print("Un numero Random del 1 a 50: ", aleatorio01)

aleatorio02 = uniform(1,10)
print("Un numero Random del 1 a 10: ", aleatorio02)

# Redondeo del numero decimal de aleatorio de uniform
aleatorio03 = round(uniform(12,45),2)
print("Un numero Random del 12 a 45: ", aleatorio03)

# Metodo choice
colores = ['azul', 'rojo', 'verde', 'amarillo', 'negro']
aleatorio04 = choice(colores)
print(f"\nLista de Colores: {colores}\n", "Color Random: ",aleatorio04)

# Metodo shuffle, aleatorio en los numero de orden
numeros = list(range(5,45,5))
shuffle(numeros)
print()
print(numeros)