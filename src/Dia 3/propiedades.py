# Definición del poema como cadena multilínea
texto1 = """\t\t\tAmor es un fuego que
            arde sin ver, es herida que
            duele y no se siente; es un
            sueño del que me
            despierto y que al
            depertar, no tenga nada."""

# Imprime el poema
print("Poema de Amor:\n" + texto1)

# Prueba de búsqueda de palabras usando booleanos
print("\nExiste la palabra 'siente' en el Poema de Amor: ", "siente" in texto1)
print("Existe la palabra 'sol' en el Poema de Amor: ", "sol" in texto1)
print()
print("No existe la palabra 'siente' en el Poema de Amor: ", "siente" not in texto1)
print("No existe la palabra 'sol' en el Poema de Amor: ", "sol" not in texto1)

# Muestra la longitud del poema en caracteres
print("\nLogitud de caracteres en el texto:", len(texto1))

# Muestra la longitud del poema en palabras
print("Logitud de palabras en el texto:", len(texto1.split()))