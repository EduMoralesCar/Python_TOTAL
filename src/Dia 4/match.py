'''serie = input('Ingrese el ID de la serie: ')

match serie:
    case "N-01":
        print('Samsung')
    case "N-02":
        print('Nokia')
    case "N-03":
        print('Motorola')
    case "N-04":
        print('Lenovo')
    case _:
        print('No esxiste el producto, vuelve intentarlo denuevo.')'''


# Ejemplo: diccionario
cliente = {'nombre': 'Edu Morales',
           'edad': 45,
           'ciudad': 'Lima',
           'ocupación': 'Universitario'}

pelicula = {'titulo': 'Asesinos',
            'ficha tecnica': {'Protagonistas': 'Antonio Banderas y Silvestre Stallone',
                              'directores': 'Lilly Wachowski y Lana Wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupación': ocupacion}:
            print("Es un cliente:")
            print(f"{nombre} tiene {edad} años y actualmente es un estudiante {ocupacion} ")

        case {'titulo': titulo,
              'ficha tecnica': {'Protagonistas': protagonistas,
                                'directores': directores}}:
            print("Esto es una pelicula:")
            print(f"Llamada {titulo}, protagonisado por {protagonistas} con su directores {directores}")

        case _:
            print("\nesta variable a un no esta definido correctamente.")