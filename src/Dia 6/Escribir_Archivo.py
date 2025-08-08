archivo = open('prueba1.txt', 'w')  # Modo Escritura

# Agreamos Información
archivo.write('1. Ing. Sistemas\n')
archivo.write('2. Ing. Software\n')
archivo.write('3. Ing. Forence\n')

archivo = open('prueba1.txt', 'a')  # Agregar más Información al final

# Agreamos Información
archivo.write('4. Ing. Ciberseguridad\n')
archivo.write('5. Ing. Informatica\n')

archivo.close()  # Cerramos

archivo = open('prueba1.txt', 'r')  # Modo Lectura

# Imprimir en la Pantalla
lineas_texto = archivo.read()
print('Información:')
print(lineas_texto)
