"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.

Ejemplo01:
Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error,
imprima en pantalla el mensaje: "Error inesperado". En caso contrario,
deberá limitarse a mostrar el resultado de la suma entre los dos números.
"""


def suma(num1, num2):

    try:
        print(num1 + num2)
    except:
        print("\nHa ocurrido un error!!")

suma(5, '3')
suma(5, 3)