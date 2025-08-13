# Ejemplo de métodos especiales en Python
class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        print(f'El libro "{self.titulo}" ha sido eliminado.')

l1 = Libro('Quijote de la Mancha', 'Miguel de Cervantes', 1200)

print(l1)  # Imprime: "Quijote de la Mancha", de Miguel de Cervantes
print(len(l1))  # Imprime: 1200 (cantidad de páginas del libro)
del l1  # Elimina el objeto l1 y llama al metodo __del__
