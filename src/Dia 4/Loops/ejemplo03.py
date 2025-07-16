numero = 5
while numero > -1:
    print( f"Cuenta Regresiva {numero}")
    #numero -= numero - 1
    numero -= 1
print("Fin de la cuenta regresiva")
print()


valor = 50
divisibles = 0
no_divisibles = 0
while valor >= 0:
    if valor % 5 == 0:
        print(f"{valor} (Divisible por 5)")
        divisibles += 1
    else:
        print(valor)
        no_divisibles += 1
    valor -= 1

print()
print(f"Tenemos {no_divisibles} valores que no son divisibles por 5")
print(f"Tenemos {divisibles} valores que son divisibles por 5")