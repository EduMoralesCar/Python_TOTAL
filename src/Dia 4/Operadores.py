
# Operadores de comparación
dato1 = "Welcome!!" == "Bienvenido!!"
dato2 = 10 == (2+3)*2
print(f"\nEl enunciado del dato1 es: {dato1}" + "\n" + f"El enunciado del dato2 es: {dato2}")

# operadores logicos
frase = ("""
        Cuando algo es lo suficientemente importante,
        lo haces incluso si las probabilidades de que
        salga bien no te acompañan
        """)
print("\n Frase: ")
print(frase)

# Operadores lógicos
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool= palabra1 and palabra2 not in frase
print(f"La palabra {palabra1} y {palabra2} no estan en la 'frase'?\nRespuestas: {mi_bool}")
print("------------------------------------------------------")
palabra3 = "suficientemente"
palabra4 = "probabilidades"
mi_bool2 = palabra3 and palabra4 in frase
print(f"La palabra {palabra3} y {palabra4} estan en la 'frase'?\nRespuesta: {mi_bool2}")
