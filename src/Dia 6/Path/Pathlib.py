from pathlib import Path

carpeta = Path("C:/Users/edumo/PycharmProjects/Curso_Python/src/Dia 6/Path/Prueba.txt")
print("Contenido:")
print(carpeta.read_text()) # Nos permite leer el contenido del Archivo

print() # Salto de Linea

print('Nombre:', carpeta.name) # Devuelve el nombre del Archivo
print('Terminación:', carpeta.suffix) # 'suffix' es una función, que permite ver la tipo texto '.txt'
print('Nombre sin la Terminación:', carpeta.stem)  # Nos devolvera el nombre sin la Terminación


# Verificamos si el archivo existe!!!
print()
if not carpeta.exists():
    print('El archivo no existe')
else:
    print('El archivo existe')
