# Creacion de una clase en Python
class Persona:
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad

    def presentarse(self):
        return (f"Información:\n{self.nombre} {self.apellido}\n{self.edad} años\n{self.ciudad}\n")

# Creacion de un objeto de la clase Persona
user1 = Persona("Juan", "Pérez", 30, "Madrid")
user2 = Persona("Ana", "Gómez", 25, "Barcelona")
user3 = Persona("Luis", "Martínez", 40, "Valencia")

# Presentación de los objetos
print(user1.presentarse())
print(user2.presentarse())
print(user3.presentarse())