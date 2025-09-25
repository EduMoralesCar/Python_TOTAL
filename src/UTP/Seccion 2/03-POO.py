class Persona:
    def __init__(self, nombre, apellido, edad, telefono, direccion, sexo, anoNacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.sexo = sexo
        self.anoNacimiento = anoNacimiento

    def identificacion(self):
        return (f"Indentificación emitida por la Reniec\n"
                f"Nombre: {self.nombre}\n"
                f"Apellido: {self.apellido}\n"
                f"Edad: {self.edad}\n"
                f"año de nacimiento: {self.anoNacimiento}\n"
                f"Sexo: {self.sexo}\n")

    def contacto(self):
        return (f"Contactos de la persona\n"
                f"Nombre y Apellido: {self.nombre} {self.apellido}\n"
                f"Contacto: {self.telefono}\n"
                f"Direccion: {self.direccion}\n")

user1 = Persona(
    "Edu",
    "Morales",
    20,
    930273073,
    "Urbanizacion 666 - Manzana 45",
    "M",
    "2004-08-12"
)

print(user1.identificacion())
print(user1.contacto())