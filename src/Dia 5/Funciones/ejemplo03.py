
def todos_dispositivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True

lista_numeros = [1, 2, 3, 4, 5, 6, -7, 8, 9, 10]
resultado = todos_dispositivos(lista_numeros)
print(f"\nValores de los numeros: {lista_numeros}")
print( "Todos los números son positivos?\nResultado:", resultado)
