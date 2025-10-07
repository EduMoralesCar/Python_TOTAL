def mi_generador():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# Uso
valor = mi_generador()
print((next(valor))) # Imprime 1
print((next(valor))) # Imprime 2

print() # Línea en blanco para separar las salidas

# Usando el generador
for valor in mi_generador():
    print(valor)

