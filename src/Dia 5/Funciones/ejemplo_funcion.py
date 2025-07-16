precio_cafe = [('cafe americano', 1.50), ('cafe con leche', 2.00), ('cafe irlandes', 3.00)]

# Identicar el cafe mas caro
def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
    return (cafe_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precio_cafe)
print(f"El café más caro es '{cafe}' con un precio de ${precio:.2f}")