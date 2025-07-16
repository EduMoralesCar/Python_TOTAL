lista = list(range(100, 500,30))
print(f"El valor mínimo y máximo de la lista: {lista}")
print("Minimo:", min(lista),"\nMaximo:", max(lista))

nombres = ['Aldo', 'Omar', 'Edu', 'Odon', 'Pedro']
print("Lista de nombres:", nombres)
print("Minimo:", min(nombres),"\nMaximo:", max(nombres))


# Ejemplo de uso de min y max con una lista de tuplas
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print("\nLa edad Minima es: ", edad_minima)
print("El ultimo Nombre es: ", ultimo_nombre)