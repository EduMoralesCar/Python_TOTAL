def chequear_cifras(lista):
    for numero in (lista):
        if numero in range(1, 100):
            return "El numero " + str(numero) + " está en el rango de 1 a 100"
        else:
            return "El numero " + str(numero) + " no está en el rango de 1 a 100"

resultado = chequear_cifras([1078,67,34])
print(resultado)