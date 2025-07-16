def potencia(num1,num2):
    resultado = num1**num2
    return resultado
total = potencia(3,4)
print(total)

# Ejemplo 1
def invertir_palabra(palabra):
    palabra = palabra.upper()
    invertir = palabra[::-1]
    return invertir
palabra = "sofocado"
print(invertir_palabra(palabra))


# Ejemplo 2
def mutliplicar(num1, num2):
    resultado = num1 * num2
    return resultado
valores = mutliplicar(int('5'), int('10'))
print(valores)