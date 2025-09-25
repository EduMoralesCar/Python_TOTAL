def estudiante(nombre, apellido):
    nombreCompleto = nombre + ' ' + apellido
    return nombreCompleto

user1 = estudiante('Edu', 'Morales')
print(user1)

def saludar():
    print( 'Bienvenido alumno, ' + estudiante('Edu', 'Morales'))
saludar()
