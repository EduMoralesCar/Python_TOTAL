# Definición de un diccionario con datos de un cliente
cliente = {'id':1111, 'nombre':'Eduardo', 'apellido': 'Ramirez', 'edad':24, 'talla': 1.67, 'telefono': 930273073}

# Extracción de datos individuales del diccionario
name = cliente['nombre']
lastName = cliente['apellido']
age = cliente['edad']
identity = cliente['id']
size = cliente['talla']
phones = cliente['telefono']

# Impresión de los datos del cliente
print()
print(f"Cliente id: {identity}\nNombre y Apellido: {name} {lastName}\nEdad: {age}\nTalla: {size}\nTelefono: {phones}")
print(type(age))  # Muestra el tipo de dato de la edad
print()

# Otro ejemplo de diccionario
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
print(mi_dic)

# Insertar y actualizar elementos en el diccionario
mi_dic["pais"] = "Colombia"      # Inserta nuevo elemento
mi_dic["edad"] = 36              # Actualiza valor existente
mi_dic["ocupacion"] = "Editora"  # Actualiza valor existente
print(mi_dic)