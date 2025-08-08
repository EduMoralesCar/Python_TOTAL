# Implementación de la función
def abrir_leer(fichero):

    with open(fichero, 'r') as archivo:
        contenido = archivo.read()
    return contenido

# Función que sobre escribe el contenido del archivo
def sobrescribir(fichero):
    with open(fichero, 'w') as archivo:
        archivo.write('Bitacora de estudio del curso de Python_TOTAL.\nIncluye conceptos clave y ejercicios practicos desarrollados semanalmente en Python con Pycharm.')

# Función que agrega contenido al fichero de texto
def registro_error(fichero):
    archivo = open(fichero, 'a')
    archivo.write("\nse ha registrado un error de ejecución.")
    archivo.close()


# Abrir un archivo haciendo uso de la función
print(abrir_leer("C:/Users/edumo/PycharmProjects/Curso_Python/src/Dia 6/ArchivoFunciones_v1.txt"))
print()

sobrescribir("C:/Users/edumo/PycharmProjects/Curso_Python/src/Dia 6/ArchivoFunciones_v2.txt")
mi_archivo = open('ArchivoFunciones_v2.txt')
print(mi_archivo.read())
print()

registro_error("C:/Users/edumo/PycharmProjects/Curso_Python/src/Dia 6/ArchivoFunciones_v2.txt")
mi_archivo = open('ArchivoFunciones_v2.txt')
print(mi_archivo.read())
print()
