
# Ejemplo de Practica Control de Flujo 2
edad = int(input('Ingrese su edad: '))
licencia = input('¿Tiene licencia de conducir? (si/no): ').strip().lower()

# Validación de la entrada de licencia
if licencia == 'si':
    licencia = True
else:
    licencia = False

# Validación de la edad y licencia
if edad >= 18:
    print('Eres mayor de edad, puedes conducir')
elif edad < 18 and licencia:
    print('Eres menor de edad, pero tienes licencia de conducir, en todo caso puedes conducir con un adulto responsable')
else:
    print('No tienes edad suficiente para conducir')
