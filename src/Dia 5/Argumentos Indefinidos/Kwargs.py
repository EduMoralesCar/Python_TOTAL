def suma(**kwargs):
    total = 0

    # Recorremos los argumentos recibidos
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  # Verificamos si el valor es un número
            total += value
        else:
            print(f"El valor de '{key}= {value}' no es un número!!")

    return total
# Ejemplo de uso de la función suma con kwargs
print("Suma:", suma(a=1, b=2, c=3))  # Suma de números


#Ejemplo 1
print("\nEjemplo 1:")
def cantidad_atributos(**kwargs):
    return len(kwargs)
print("Cantidad de atributos:", cantidad_atributos(nombre="Aldo", edad=25, ciudad="Lima"))  # 3 atributos

# Ejemplo 2
print("\nEjemplo 2:")
def lista_atributos(**kwargs):
    return list(kwargs.items())
print("Lista de atributos:", lista_atributos(nombre="Aldo", edad=25, ciudad="Lima"))  #Resultado: [('nombre', 'Aldo'), ('edad', 25), ('ciudad', 'Lima')]
print(type(lista_atributos))

# Ejemplo 3
print("\nEjemplo 3:")
def lista_atributos_solo_valores(**kwargs):
    return list(kwargs.values())

print(lista_atributos_solo_valores(nombre="Edomocar", edad=21, Ciudad="Lima"))
print(type(lista_atributos_solo_valores)) # tipo de dato: <class 'function'>, porque es una función

# Ejemplo 4
print("\nEjemplo 4:")
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describir_persona("María", color_ojos="azules", color_pelo="rubio")