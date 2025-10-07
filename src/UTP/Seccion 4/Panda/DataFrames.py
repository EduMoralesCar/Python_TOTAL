import pandas as pd

diccionario = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [23, 34, 45, 29],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

dataframe = pd.DataFrame(diccionario)
print(dataframe)

#Seleccionar Columnas
print("\nSeleccionar una columna (Nombre):\n", dataframe['Nombre'])
print("\nSeleccionar varias columnas (Nombre y Ciudad):\n", dataframe[['Nombre', 'Ciudad']])

#Seleccionar Filas
print("\nSeleccionar una fila (fila 2):\n", dataframe.iloc[2])
print("\nSeleccionar varias filas (filas 1 a 3):\n", dataframe.iloc[1:4])

# Filtrar Datos
print("\nFiltrar datos (Edad > 30):\n", dataframe[dataframe['Edad'] > 30])
print("\nFiltrar datos (Ciudad == 'Madrid'):\n", dataframe[dataframe['Ciudad'] == 'Madrid'])

# Agregar Nueva Columna
dataframe['Salario'] = [3000, 4000, 5000, 3500]
print("\nDataFrame con nueva columna (Salario):\n", dataframe)

dataframe['Profesión'] = ['Ingeniera', 'Médico', 'Abogado', 'Arquitecta']
print("\nDataFrame con nueva columna (Profesión):\n", dataframe)

# Modificar Valores
dataframe["Edad"] = dataframe["Edad"] + 2
print("\nEdad Actualizado +2 años:\n", dataframe)

# Eliminar Columna
dataframe = dataframe.drop('Salario', axis=1)
print("\nDataFrame sin la columna Salario:\n", dataframe)

# Eliminar Fila
dataframe = dataframe.drop(2, axis=0)
print("\nDataFrame sin la fila 2:\n", dataframe)