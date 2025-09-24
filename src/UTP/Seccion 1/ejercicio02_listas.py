listaPaises = ['Perú', 'Argentina', 'Chile', 'Brasil', 'Colombia', 'Venezuela']

print(listaPaises)

listaPaises.append('Bolivia')
listaPaises.append('Cuba')

print(listaPaises)

listaPaises.insert(2, 'Ecuador')
listaPaises.insert(2, 'Ecuador')  # Pueden repetirse los elementos
listaPaises.insert(5, 'El Salvador')
print(listaPaises)

listaPaises.extend(['México', 'Estados Unidos', 'Canadá'])
print(listaPaises)

listaPaises.sort()
print(listaPaises)

listaPaises.reverse()
print(listaPaises)

listaPaises.remove('Chile')
listaPaises.remove('Estados Unidos')
# listaPaises.remove('Francia') # Error! elemento no existe
print(listaPaises)

print(len(listaPaises))

# Hacemos uso de bucles para recorrer la lista
# Usamos la estructura while
i = 0
while i < len(listaPaises):
    print(listaPaises[i])
    i += 1

# Recorrido de colección
for pais in listaPaises:
    print(pais)

# Recorrido usando un rango
for i in range(0, len(listaPaises)):
    print(listaPaises[i])

# Formateando la salida
print("Lista numerada")
for idx in range(0, len(listaPaises)):
    print(f"{idx + 1}. {listaPaises[idx]}")
