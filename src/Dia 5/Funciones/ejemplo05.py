# lista original:
lista_numeros = [1, 2, 15, 7, 2]

# Funcion para reducir la lista
def reducir_lista(lista):
    lista_sin_duplicados = list(set(lista))
    lista_sin_duplicados.remove(max(lista_sin_duplicados))

    return lista_sin_duplicados

# Funcion para calcular el promedio
def promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# Ejecutar las funciones
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)

# Imprimir resultados
print(f"Lista original: {lista_numeros}")
print(f"Lista reducida: {lista_reducida}")
print(f"Promedio de la lista reducida: {resultado_promedio:.2f}")