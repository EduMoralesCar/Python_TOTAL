texto1 = "Welcome of student"
# Indices: W e l c o m e   o f     s  t  u  d  e  n  t
#          0 1 2 3 4 5 6 7 8 9 10  11 12 13 14 15 16 17

# Obtenemos el índice 5 ('m')
resultado1 = texto1[5]

# Usamos f-string para formatear correctamente
print(f"\nMostramos la letra del indice '{5}' que es: {resultado1}")

resultado2 = texto1.index("f")
print(f"Mostramos el indice de la letra 'f' que es: {resultado2}")

resultado3 = texto1.index("e",7)
print(f"El valor del indice de la letra 'e' apartir del indice {7} es el siguiente: {resultado3}")



# Ejemplo 1
texto2 = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print()
# Imprimimos el primer resultado que inicia del indice 0
resultado4 = texto2.index("práctica")
print(f"Indice de la primera aparición de la palabra 'práctica' es el {resultado4}")

# Imprimimos el primer resultado que inicia del  ultimo indice
resultado5 = texto2.rindex("práctica")
print(f"Indice de la última aparición de la palabra 'práctica' es el {resultado5}")


