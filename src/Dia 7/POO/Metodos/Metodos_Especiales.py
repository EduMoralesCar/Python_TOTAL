
class Producto:
    def __init__(self, nombre, precio): # Inicializador del objeto
        self.nombre = nombre
        self.precio = precio

    def __str__(self): # Define como se se imprimirá el objeto
        return f"Producto: {self.nombre}, Precio: ${self.precio}"

    def __eq__(self, other): # Permite comparar dos objetos de la clase Producto
        return self.nombre == other.nombre and self.precio == other.precio

    def __add__(self, other): # suma los precios de dos objetos de la clase Producto
        return self.precio + other.precio


# Ejemplo de uso
p1 = Producto("Laptop", 1200)
p2 = Producto("Laptop", 1200)
p3 = Producto("Mouse", 50)

print()
print(p1)                      # Producto: Laptop, Precio: $1200
print(p2)                      # Producto: Laptop, Precio: $1200
print(p3)                      # Producto: Mouse, Precio: $50
print('\nComporación de productos:')
print(p1 == p2)                # True
print(p1 == p3)                # False
print(p1 + p3)                 # 1250