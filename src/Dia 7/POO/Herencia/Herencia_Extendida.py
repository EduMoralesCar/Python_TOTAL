
class Animal:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal", self.nombre, "ya nacio")

    def hablar(self):
        print("El animal", self.nombre, "emite un sonido")


class Pajaro(Animal):
    def __init__(self, nombre, edad, color, distancia):
        super().__init__(nombre, edad, color)
        self.distancia = distancia

    def hablar(self):
        print("El", self.nombre, "emite un sonido de Craac-crac ")

    def volar(self, distancia):
        print(f"El Pajaro vuela {distancia} metros")



animal1 = Animal('Loro', 1, 'negro')
animal1.nacer()

animal2 = Pajaro('Avestruz', 2, 'branco', '')
animal2.volar(100)
