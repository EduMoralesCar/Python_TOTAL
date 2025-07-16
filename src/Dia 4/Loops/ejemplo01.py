# Ejemplo de bucle for en Python
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f"Hola {alumno}")

# EJemplos de suma de numeros en una lista
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_total = 0
for numero in lista_numeros:
    suma_total = suma_total + numero
print(f'\nToda la suma de la lista de los numeros es de {suma_total}')
