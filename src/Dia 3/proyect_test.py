texto = input("Introduce un texto: ")
letras = []
texto = texto.lower()

letras.append(input("Ingres la primera letra favorita: ").lower())
letras.append(input("Ingres la segunda letra favorita: ").lower())
letras.append(input("Ingres la tercera letra favorita: ").lower())

print()

print("CANTIDAD DE LETRAS REPETIDAS")
for letra in letras:
    print(f"La letra '{letra}' aparece {texto.count(letra)} veces.")

print()

print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en el texto.")

print()

print("PRIMERA Y ULTIMA LETRA DEL TEXTO")
if len(texto) > 0:
    print(f"La primera letra del texto es: '{texto[0]}'")
    print(f"La última letra del texto es: '{texto[-1]}'")

print()

print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"El texto invertido es:\n'{texto_invertido}'")

print()

print("VERIFICACIÓN DE LA PALABRA 'PYTHON'")
if "python" in texto:
    print("Sí, la palabra 'Python' está en el texto.")
else:
    print("No, la palabra 'Python' no está en el texto.")
