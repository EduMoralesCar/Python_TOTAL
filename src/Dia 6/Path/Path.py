from pathlib import Path

# Crear un objeto Path para el directorio actual
directorio = Path('.')

# Verficar si existe el Archivo
archivo = directorio / 'fichero.txt'
print('¿Existe el archivo?', archivo.exists())

# Listar todo los archivos '.txt' en el directorio
for f in directorio.glob('*.txt'):
    print('Archivo encontrado:', f)


# Devuelve la ruta del directorio base del usuario
ruta_base = Path.home()
print(ruta_base)


# Creamos una ruta Relativa que nos permite llegar a un Archivo
ruta = Path('src')/'Dia 6'/'Path'/'Prueba.txt'
print(ruta)


# Creamos una ruta Absoluta que nos permite llegar a un Archivo
ruta = Path.home()/'src'/'Dia 6'/'Path'/'Prueba.txt'
print(ruta)