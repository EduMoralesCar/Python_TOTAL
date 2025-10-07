import pandas as pd

dic_datos = {
    'id': [1, 2, 3, 4],
    'codigo': ['A1', 'B2', 'C3', 'D4'],
    'nombre': ['Mouse', 'Teclado', 'Camara', 'Audifono'],
    'precio': [None, 30000, 40000, 50000],
    'cantidad': [5, 10, 15, 20]
}

df = pd.DataFrame(dic_datos)
print(df)

# Detectar valores nulos
print("\nDetectar valores nulos:\n", df.isnull())