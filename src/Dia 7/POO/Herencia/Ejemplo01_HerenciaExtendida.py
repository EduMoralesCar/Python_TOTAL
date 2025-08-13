class Padre:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def presentarse(self):
        return f'Nombre: {self.nombre} {self.apellido} \nEdad: {self.edad} años \nInfo: Padre'


class Hijo(Padre):
    def __init__(self, nombre, apellido, edad, oficio):
        super().__init__(nombre, apellido, edad)
        self.oficio = oficio

    def presentarse(self):
        return f'Nombre: {self.nombre} {self.apellido} \nEdad: {self.edad} años \nTrabajo: {self.oficio} \nInfo: Hijo'


class Nieto(Hijo):
    def __init__(self, nombre, apellido, edad, oficio, hobby):
        super().__init__(nombre, apellido, edad, oficio)
        self.hobby = hobby

    def presentarse(self):
        return f'Nombre: {self.nombre} {self.apellido} \nEdad: {self.edad} años \nHobby: {self.hobby} \nInfo: Nieto'


padre = Padre('Aldomar', 'Morales', 56)
hijo = Hijo('Edumoca', 'Morales', 30, 'Desarrollador')
nieto = Nieto('Edomocar', 'Morales', 10, 'Estudiante', 'PlayStation 5')

print(padre.presentarse())
print()
print(hijo.presentarse())
print()
print(nieto.presentarse())
