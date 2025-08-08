# Ejemplo 1
def usd_a_eur(numero):
    dolares = 0.90
    resultado = numero * dolares
    return resultado
usd = float(input("Ingrese la cantidad en USD: "))
valor = usd_a_eur(usd)
print(f"{usd} Dolares equivale a {valor:.2f} Euros")

print()

# Ejemplo 2
def sol_a_dolar(numero):
    dolar = 3.55
    resultado = numero * dolar
    return resultado
dolar = int(input("Ingrese la cantidad en USD: "))
valor_sol = sol_a_dolar(dolar)
print(f"{dolar} Dolares equivale a {valor_sol:.2f} Soles")