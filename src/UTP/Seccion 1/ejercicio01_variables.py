# Ejercicio 01: 
# escribir un programa en Python que solicite el nombre de un alumno 
# y tres calificaciones (enteros). El programa debe calcular y mostrar 
# el promedio (con dos decimales) con el siguiente formato: 
# (ejemplo) “Juan, su promedio es: 16.50”

nombre = input("Ingrese su nombre: ")

nota1 = int(input("Ingrese nota 1: "))
nota2 = int(input("Ingrese nota 2: "))
nota3 = int(input("Ingrese nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3.0

print(f"{nombre}, su promedio es {promedio}")
print(f"{nombre}, su promedio es " + "{0:.2f}".format(promedio))
print(f"{nombre}, su promedio es {promedio:.2f}")
print(f"{nombre}, su promedio es %.2f" % promedio)
