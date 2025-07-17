def letras_unicas_ordenadas(palabra):
    palabra = palabra.lower()          # Convierte a minúsculas
    letras = set(palabra)              # Elimina duplicados
    return sorted(letras)              # Ordena alfabéticamente

#palabra = input("Ingresa una palabra: ")
#print(letras_unicas_ordenadas(palabra))

print(letras_unicas_ordenadas(input("Ingresa una palabra: ")))