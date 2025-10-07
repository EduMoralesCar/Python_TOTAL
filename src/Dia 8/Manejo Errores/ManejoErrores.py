def suma():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    total = num1 + num2
    print('resultado:', total)

try:
    suma()
except TypeError and ValueError:
    print("\nHa ocurrido un error!!")
else:
    print("\nOperación Exitosa!!")
finally:
    print("Gracias por usar el programa de suma\nFin del programa!!!")


# Manejo de errores en Python
# https://docs.python.org/3/tutorial/errors.html
# https://realpython.com/python-exceptions/
