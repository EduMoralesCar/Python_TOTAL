nombres = ['Aldo', 'Omar', 'Edu', 'Odon', 'Pedro']
edades = (28,29,20,30,31)
ciudades = ['Lima', 'Huaraz', 'Huari', 'Chiclayo', 'Trujillo']

combinados = list(zip(nombres,edades,ciudades))

for nombres,edades,ciudades in combinados:
    print(f"{nombres} tiene {edades} años y actualmente vive en la ciudad de {ciudades}.")

print()

from tabulate import tabulate

nombres = ['Aldo', 'Omar', 'Edu', 'Odon', 'Pedro']
edades = (28, 29, 20, 30, 31)
ciudades = ['Lima', 'Huaraz', 'Huari', 'Chiclayo', 'Trujillo']

combinados = list(zip(nombres, edades, ciudades))

# Crear la tabla
tabla = tabulate(combinados, headers=["Nombre", "Edad", "Ciudad"], tablefmt="grid")
print(tabla)