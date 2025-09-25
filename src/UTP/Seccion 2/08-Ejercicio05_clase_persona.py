class Persona:
    nombre = ""
    edad = 0

    # constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def print(self):
        print(f"{self.nombre} ({self.edad})")

    def __str__(self):
        return f"{self.nombre} ({self.edad})"
    

persona1 = Persona("Andrés Rojas", 35)

print(persona1.nombre)
print(persona1.edad)

persona2 = Persona("Marizta Vega", 28)

print(persona2)  # se invoca __str__ implícitamente
persona2.print()


'''
Python Magic methods are the methods starting and ending with double underscores ‘__’. 
They are defined by built-in classes in Python and commonly used for operator overloading. 

They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.
'''
