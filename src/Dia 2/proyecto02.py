# Ejemplo de ventas y comisiones
print()
nombre = input("Por favor, ingrese su nombre: ")
ventas = int(input("Ingrese sus ventas totales de este mes: "))

# Ejemplo de cálculo de comisión con un 13% de comisión con 2 decimales
pago_mes = round(ventas * 0.13,2)

# Imprimir el resultado
print()
print(f"Hola {nombre}, este mes vendiste {ventas}. Por ello, tu comisión de ventas es de ${pago_mes}")
