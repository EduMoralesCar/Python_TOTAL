'''
Ejemplo 1:
Crea una clase Perro. Dicho perro debe poder ladrar.
Crea el metodo ladrar() y ejecútalo en una instancia de Perro.
Cada vez que ladre, debe mostrarse en pantalla "Guau!".
'''

# Version 1
class Perro:
    def __init__(self, aullido):
        self.aullido = aullido

    def ladrar(self):
        return f"{self.aullido}"

perro1 = Perro("Guau!")
print(perro1.ladrar())


# Version 2
class Perro:
    def ladrar(self):
        print("Guau!")

pluto = Perro()
pluto.ladrar()




'''
Ejemplo 2:
Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").
Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.
'''

class Mago:
    def lanzar_hechizo(self):
        print('¡Abracadabra!')

merlin = Mago()
merlin.lanzar_hechizo()




'''
Ejemplo 3:
Crea una instancia de la clase Alarma, que tenga un método llamado
postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje
"La alarma ha sido pospuesta {cantidad_minutos} minutos"
'''

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

alarma = Alarma()
alarma.postergar(10)