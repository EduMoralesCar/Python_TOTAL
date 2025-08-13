'''
Definición:
La herencia es un mecanismo de la programación orientada a objetos que permite crear una nueva clase basada en una clase existente.
La nueva clase, llamada subclase o clase derivada, hereda atributos y métodos de la clase base o superclase.
Esto promueve la reutilización del código y la creación de jerarquías de clases.
'''

from abc import abstractmethod


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Vehículo: {self.marca} {self.modelo}")

    @abstractmethod
    def tipo_vehiculo(self):
        pass

    def encender(self):
        print(f"{self.marca} {self.modelo} está encendido.")


# Clase Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self):
        return f"Auto {self.marca} {self.modelo} con {self.puertas} puertas."


# Clase Camion
class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga

    def descripcion(self):
        return f"Camión {self.marca} {self.modelo} con capacidad de {self.capacidad_carga} kg."



# Uso
vehiculos = [
    Auto("Toyota", "Corolla", 4),
    Camion("Volvo", "FH", 18000),
]


for v in vehiculos:
    print(v.descripcion())
    v.encender()
