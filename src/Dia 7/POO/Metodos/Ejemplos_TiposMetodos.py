'''
    Ejemplo 1:
    Crea un metodo estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
'''

class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()


print()


'''
    Ejemplo 2:
    Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, 
    estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.
'''
class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(f'El jugador ha revivido: {cls.vivo}')

print(Jugador.vivo)  # False
Jugador.revivir()
print(Jugador.vivo)  # True


print()


'''
    Ejemplo 3:
    Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje,
    que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
'''
class Personaje:
    def __init__(self, nombre, cantidad_flechas):
        self.nombre = nombre
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print(f"{self.nombre} ha lanzado una flecha. Flechas restantes: {self.cantidad_flechas}")
        else:
            print(f"{self.nombre} no tiene flechas para lanzar.")

# Ejemplo de uso
personaje = Personaje("Edomocar", 5)
personaje.lanzar_flecha()  # Edomocar ha lanzado una flecha.
personaje.lanzar_flecha()
personaje.lanzar_flecha()
personaje.lanzar_flecha()
personaje.lanzar_flecha()
personaje.lanzar_flecha()


# Versión Simple
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

legolas = Personaje(5)
legolas.lanzar_flecha()
print(legolas.cantidad_flechas)