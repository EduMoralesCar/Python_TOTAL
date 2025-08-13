'''
Ejemplo 1:
Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación,
y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le
permita a esta clase heredar correctamente de Padre y Madre.
'''


class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")


class Hija(Padre, Madre):
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y vengo de la herencia múltiple.")


# Crear una instancia de Hija
hija = Hija("Ana")
hija.trabajar()  # -> "Trabajando en la Fiscalía"
hija.reir()  # -> "Ja ja ja!"

print()  # Salto de linea

''' Ejemplo 2:'''


class Vertebrado:
    vertebrado = True


class Ave(Vertebrado):
    tiene_pico = True

    def poner_huevos(self):
        print("Poniendo huevos")


class Reptil(Vertebrado):
    venenoso = True


class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")


class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")


'''
Métodos heredados:
poner_huevos() de Ave y Pez
nadar() de Pez
caminar() de Mamifero
amamantar() de Mamifero
'''


class Ornitorrinco(Pez, Reptil, Ave, Mamifero, Vertebrado):
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, un ornitorrinco con pico, venenoso y vertebrado.")


# Crear una instancia de Ornitorrinco
ornitorrinco = Ornitorrinco("Perry")
ornitorrinco.presentarse()
ornitorrinco.nadar()
ornitorrinco.poner_huevos()
ornitorrinco.caminar()
ornitorrinco.amamantar()


''' Ejemplo 3'''
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

