class Pajaro:
    alas = True

    def __init__(self, nombre, color, especie):
        self.nombre = nombre
        self.color = color
        self.especie = especie

    # Metodo de instancia para piar
    def piar(self):
        print(f"{self.nombre} está piando.")

    # Metodo para volar
    def volar(self):
        if self.alas:
            print(f"{self.nombre} está volando.")
        else:
            print(f"{self.nombre} no puede volar porque no tiene alas.")

    # Metodo para pintar el pajaro de otro color
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    # Metodo de Clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    # Metodos Estaticos
    @staticmethod
    def mirar():
        print('El pajaro esta mirando')


# Imprimir en la Consola
piando = Pajaro("Aveztruz","Amarrillo","Vertebrados")
piando.piar()

otro_color = Pajaro("Aveztruz","Amarrillo","Vertebrados")
otro_color.pintar_negro()

Pajaro.poner_huevos(10)

Pajaro.mirar()

