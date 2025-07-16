dato = set((1,2,3,4,5,6,7))
print(type(dato))
print(dato)
print(dato.issubset(dato))

print()
sorteo = {"camila", "Margarita", "Axel","Jorge", "Miguel", "Monica"}
print(f"Lista Completa del sorteo:\n{sorteo}\n")
print("Eliminamos un elemento al azar: "+ sorteo.pop())
print()
print(f"Lista Completa despues de la eliminación:\n{sorteo}\n")
# Realizamos la Agregacion de un dato
sorteo.add("Edomocar")
print(f"Agremos un nombre llamado 'Edomocar':\n{sorteo} ")

# Eliminamos un elemento con el método discard
sorteo.discard("Miguel")
print(f"Eliminamos el nombre 'Miguel':\n{sorteo} ")
# Eliminamos un elemento con el método remove
sorteo.remove("Axel")
print(f"Eliminamos el nombre 'Axel':\n{sorteo} ")