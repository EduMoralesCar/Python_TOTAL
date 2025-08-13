'''
Ejemplo 1:
Crea una clase llamada Persona, que tenga los siguientes atributos de instancia:
1.- nombre
2.- edad
Crea otra clase, Alumno, que herede de la primera estos atributos.
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

alumno1 = Alumno("Juan", 20, "Matemáticas")
alumno2 = Alumno("Ana", 22, "Física")

print(f"Nombre: {alumno1.nombre}, Edad: {alumno1.edad}, Curso: {alumno1.curso}")
print(f"Nombre: {alumno2.nombre}, Edad: {alumno2.edad}, Curso: {alumno2.curso}")

print()

'''
Ejemplo 2:
Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar()
(puedes dejar el código de los métodos en blanco con pass).
Crea una clase llamada Automovil que herede estos métodos de Vehiculo.
'''
class Vehiculo(Persona):
    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        super().__init__(marca, modelo)

auto1 = Automovil("Toyota", "Corolla")
auto2 = Automovil("Honda", "Civic")

print(f"Marca: {auto1.marca}, Modelo: {auto1.modelo}")
print(f"Marca: {auto2.marca}, Modelo: {auto2.modelo}")

print()

'''
Ejemplo 3:
Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. 
Crea otra clase, Perro, que herede de la primera sus atributos.
'''
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
class Perro(Mascota):
    def __init__(self, edad, nombre, cantidad_patas, raza):
        super().__init__(edad, nombre, cantidad_patas)
        self.raza = raza

perro1 = Perro(3, "Max", 4, "Labrador")
perro2 = Perro(5, "Bella", 4, "Beagle")

print(f"Nombre: {perro1.nombre}, Edad: {perro1.edad}, Cantidad de Patas: {perro1.cantidad_patas}, Raza: {perro1.raza}")
print(f"Nombre: {perro2.nombre}, Edad: {perro2.edad}, Cantidad de Patas: {perro2.cantidad_patas}, Raza: {perro2.raza}")