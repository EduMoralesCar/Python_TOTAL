# Postulación a un curso de programación
conocimiento_python = input("¿Conoces Python? (si/no): ").strip().lower()
conocimiento_ingles = input("¿Conoces inglés? (si/no):").strip().lower()

# Validación de la entrada de conocimiento de Python
if conocimiento_python == 'si':
    conocimiento_python = True
else:
    conocimiento_python = False

# Validación de la entrada de conocimiento de inglés
if conocimiento_ingles == 'si':
    conocimiento_ingles = True
else:
    conocimiento_ingles = False

# Impresión de los resultados
print()
# Evaluación de la postulación
if conocimiento_python and conocimiento_ingles == True:
    print("¡Felicidades! Cumples con los requisitos para postular al curso de programación.")
elif conocimiento_python == True and conocimiento_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif conocimiento_python == False and conocimiento_ingles == True:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Lo sentimos,para postularte, necesitas saber programar en Python y tener conocimientos de inglés")