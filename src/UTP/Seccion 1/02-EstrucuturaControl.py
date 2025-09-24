# Ejemplo01 (if)
while True:
    # Entrada de datos
    try:
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))

        # Evaluacion de los numeros
        if a > b:
            print(b, 'es mayor que', a)
        elif a < b:
            print(a, 'es menor que', b)
        else:
            print(a, 'es igual a', b)
        break
    except ValueError:
        print("Error: Debe ingresar solo números enteros.")

print()  # Salto de linea

# Ejemplo02 (for)
# Entrada de datos
unidades = int(input("Ingrese unidades: "))

# Calculamos el importe a pagar
# and (y), or (o), not (negación)
if unidades >= 1 and unidades <= 25:
    importeCompra = unidades * 27.7
elif unidades >= 26 and unidades <= 50:
    importeCompra = unidades * 25.5
elif unidades >= 51 and unidades <= 75:
    importeCompra = unidades * 23.5
elif unidades >= 76:
    importeCompra = unidades * 21.5

# Calculamos el importe de descuento
if unidades > 50:
    importeDescuento = 0.15 * importeCompra
else:
    importeDescuento = 0.05 * importeCompra
    # Calcular el importe a pagar
    importePago = importeCompra - importeDescuento
    # Salida de resultados
    print("Importe de compra:", importeCompra)
    print("Importe de descuento:",
          importeDescuento)
    print("Importe a pagar:", importePago)

print()  # Salto de linea

# Ejemplo03 (While)
print('While controlado por conteo')
print("---------------------------")
print("Sumador hasta el 10")
sum = 0
num = 1

while sum <= 10:
    sum += num  # sum = sum + num
    num += 1  # num = num + 1

print("La suma es ", (sum))
