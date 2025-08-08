# Abrimos el Archivo Prueba
mi_archivo = open('Prueba.txt')

# Imprimimos con el metodo read()
print(mi_archivo.read())
mi_archivo.close() # Cerramos el archivo


# Abrimos el Archivo Denuevo
mi_archivo = open('Prueba.txt')

# Imprimimos con el metodo readline()
print()
primera_linea = mi_archivo.readline()
print('Primera linea:\n', primera_linea)

# Imprimimos con el metodo readlines()
print()
todas_lineas = mi_archivo.readlines()
todas_lineas = todas_lineas.pop()
print('Ultima linea:\n', todas_lineas)
