def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    numeros = [num1, num2, num3]

    if suma > 15:
        print("La suma es mayor a 15, entonces devolveremos el mayor de los números:")
        return max(numeros)
    elif suma < 10:
        print("La suma es menor a 10, entonces devolveremos el menor de los números:")
        return min(numeros)
    else:
        #Para el valor intermedio, ordenamos los numeros y tomamos el segundo elemento
        print("La suma está entre 10 y 15, entonces devolveremos el número intermedio:")
        numeros.sort()
        return numeros[1]

# Ejemplo de prueba:
print(devolver_distintos(1, 2, 3))
print(devolver_distintos(5,7,3))
print(devolver_distintos(10,4,3))