monedas = 5
while monedas > 0:
    print(f"tengo {monedas} monedas")
    #monedas = monedas - 1
    monedas -= 1

respuesta = 's'
while respuesta == 's':
    respuesta = input('¿Quieres seguir continuando? (s/n): ')
    respuesta = 's'

    numero  = 10
    while numero > 0:
        print(f"Conteo regresivo: {numero}")
        numero -= 1
    respuesta = input('¿Quieres seguir continuando? (s/n): ')
    if respuesta == 's':
        print('\n¡Continuemos!')
    elif respuesta == 'n':
        print('\n¡Gracias!')
        break
    else:
        print('\nEs incorrecto!!, ingrese nuevamente (s/n)')
        respuesta = 's'

    if respuesta == 'n':
        print('\n¡Gracias!')
    elif respuesta != 's':
        print('\nEs incorrecto!!, ingrese nuevamente (s/n)')
        respuesta = 's'