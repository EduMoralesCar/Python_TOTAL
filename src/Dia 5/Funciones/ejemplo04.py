
lista_numeros = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
suma = []
def suma_numeros_menores(lista):
    total = 0
    for numero in lista:
        if 0 < numero and numero < 5:
            total += numero
            suma.append(numero)

    no_sumados = [numero for numero in lista if not (0 < numero < 5)]
    print("Los siguientes valores no se suman:", no_sumados)

    return total

print("La suma es:", suma_numeros_menores(lista_numeros))
print(suma)