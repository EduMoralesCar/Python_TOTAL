texto = input("Ingrese un parrafo de un poema: ")
print(f"\nTexto ingresado:\n{texto}")
letras_favoritas = input("Ingrese 3 letras favoritas separadas por comas: ")

# Pasamos a letras minúsculas para evitar problemas de coincidencia
texto_minuscula = texto.lower()
letras_favoritas = [letra.strip().lower() for letra in letras_favoritas.split(',')]

# Contamos las ocurrencias de cada letra favorita
print("\nCantidad de ocurrencias de las letras favoritas:")
for letra in letras_favoritas:
    print(f"La letra '{letra}' aparece {texto_minuscula.count(letra)} veces.")

# primera y Ultima letra favorita
texto_completo = texto.strip()
print(f"\nPrimera letra Texto: {texto_completo[0]}")
print(f"Última letra Texto: {texto_completo[-1]}")

# Longitud del texto
texto = list(texto_minuscula)
longitud_texto = len(texto)
print(f"\nLongitud del texto: {longitud_texto} caracteres")

# Invertir el orden de las palabras
palabras_invertidas = texto[::-1]
texto_invertido = " ".join(palabras_invertidas)
print(f"\nTexto con el orden de las palabras invertido:\n{texto_invertido}")

# Verificar si la palabra "python" está en el texto
contiene_python = "python" in texto_minuscula
respuesta = {True: "Sí, la palabra 'Python' está en el texto.", False: "No, la palabra 'Python' no está en el texto."}
print(f"\n¿La palabra 'Python' está en el texto?\n{respuesta[contiene_python]}")