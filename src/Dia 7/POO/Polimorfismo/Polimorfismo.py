'''
Definición:
El polimorfismo es un concepto de programación orientada a objetos que permite que diferentes
clases puedan ser tratadas como instancias de la misma clase a través de una interfaz común.
El polimorfismo se manifiesta principalmente en dos formas:
el polimorfismo de tiempo de compilación (sobrecarga de métodos) y
el polimorfismo de tiempo de ejecución (sobreescritura de métodos).
'''
# Importa clases y decoradores para definir clases abstractas y métodos abstractos
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Muuu")

def hacer_sonido_varios(animales):
    for animal in animales:
        animal.hacer_sonido()

animales = [Perro(), Gato(), Vaca()]
hacer_sonido_varios(animales)