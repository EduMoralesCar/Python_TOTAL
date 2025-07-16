edad = input("Ingrese su edad: ")
edad = int(edad)
autizado_licencia = input("¿Tiene autización de licencia de conducir? (si/no): ").strip().lower()

if edad >= 18 and autizado_licencia == "si":
    print('Puede conducir')
elif edad >= 60:
    print("No puedes conducir. Necesitas un certificado médico")
elif 16 <= edad <= 17 and autizado_licencia == "no":
    print("Puedes conducir con un permiso de aprendizaje")
else:
    print("No puedes conducir por el momento")