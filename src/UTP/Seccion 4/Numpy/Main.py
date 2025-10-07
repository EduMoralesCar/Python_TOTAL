import numpy as np

notas = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
promedio = np.mean(notas)
print(notas, "\nPromedio:", promedio)


# Arreglo de 1 dimensión
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("\nArreglo de 1 dimensión:")
print(arr1)

# Arreglo de 2 dimensiones
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArreglo de 2 dimensions:")
print(arr2)

# Matriz 3x3 de ceros
matriz_ceros = np.zeros((3, 3))
print("\nMatriz 3x3 de ceros:")
print(matriz_ceros)

# Matriz 2x4 de unos
matriz_unos = np.ones((2, 4))
print("\nMatriz 2x4 de unos:")
print(matriz_unos)

# Matriz de 3x2 con aleatorios
matriz_aleatorios = np.random.rand(3, 2)
print("\nMatriz 3x2 con aleatorios:")
print(matriz_aleatorios)

# Valores 0-10 con paso 2
valores_paso = np.arange(0, 10, 2)
print("\nValores de 0 a 10 con paso 2:")
print(valores_paso)

# 5 valores equidistantes entre 0-10
valores_equidistantes = np.linspace(0, 10, 5)
print("\n5 valores equidistantes entre 0 y 10:")
print(valores_equidistantes)
