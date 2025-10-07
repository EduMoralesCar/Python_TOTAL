import numpy as np

matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

matriz_producto = np.dot(matriz1, matriz2)
print("Producto de matrices:\n", matriz_producto)


# Operaciones Basicás
print("\nElemento [0,1]:", matriz1[0, 1])
print("Fila 1:", matriz1[1, :])
print("Columna 2:", matriz1[:, 2])
print("Submatriz 2x2:\n", matriz1[0:2, 0:2])
