if 20 < 12:
    print('Es correcto')
else:
    print("No es correcto")



mascota = 'gato'

if mascota == 'perro':
    print('Tienes un gato')
elif mascota == 'gato':
    print('Tienes un perro')
else:
    print('No se que animal tienes')



edad = 12
calificacion = 17

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 11.5:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')


# Ejemplo de uso de operadores lógicos
num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))

if num1 > num2:
    print(f'El número {num1} es mayor que {num2}')
elif num1 < num2:
    print(f'El número {num1} es menor que {num2}')
else:
    print(f'Los números {num1} y {num2} son iguales')

