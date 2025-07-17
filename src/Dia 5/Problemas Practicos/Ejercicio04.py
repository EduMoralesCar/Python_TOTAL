def contar_primos(numero):
    primos = []

    for num in range(2, numero + 1):
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
            print(num)
    return len(primos)

# Ejemplo de uso
print("Cantidad de primos encontrados:", contar_primos(10))  # Cambia el número según sea necesario