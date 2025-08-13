# Creamos una clase con sus Atributos y métodos
class Pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

peli1 = Pelicula("'El Escuadron Suicida'", "(Jame Gunn, 2021)")
peli2 = Pelicula("'El Padrino'", "(Francis Ford Coppola, 1972)")

# Imprimimos los atributos de los objetos
print(peli1.titulo, peli1.director)
print(peli2.titulo, peli2.director)

# EJemplo01
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa('blanco', 4)
print('\nColor de la casa:', casa_blanca.color,
      '\nCantidad de pisos:', casa_blanca.cantidad_pisos)

# EJemplo02
class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje('Humano', True, 17)
print('\nEspecie:', harry_potter.especie,
      '\nMagico:', harry_potter.magico,
      '\nEdad:', harry_potter.edad)