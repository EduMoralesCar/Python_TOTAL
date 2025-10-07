import pandas as pd
#print(pd.__version__)

df = pd.read_csv("C:/Users/edumo/Documents/PycharmProjects/Python_TOTAL/src/UTP/Seccion 4/Panda/contactos.csv")
print(df)

# Propiedades Basicas de Panda
print("\nPropiedades Basicas de Panda")
print("Tipo de datos:\n", df.dtypes) # Tipos de datos
print("\nIndices:", df.index)
print("\nDimensiones:", df.shape)
print("\nPrimeras dos Filas:\n", df.head(2)) # Primeras dos filas
print("\nUltimas dos Filas:\n", df.tail(2)) # Ultimas dos filas