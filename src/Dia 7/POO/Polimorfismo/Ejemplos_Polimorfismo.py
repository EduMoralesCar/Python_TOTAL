''' EJemplo 1'''

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)


class interadores:
    def palabra_numeros(self):
        longitud1 = len(palabra)
        return longitud1

    def lista_numeros(self):
        longitud2 = len(lista)
        return longitud2

    def tupla_numeros(self):
        longitud3 = len(tupla)
        return longitud3


# Ejemplo de uso
iterador = interadores()
print("Longitud de la palabra:", iterador.palabra_numeros())
print("Longitud de la lista:", iterador.lista_numeros())
print("Longitud de la tupla:", iterador.tupla_numeros())


''' EJemplo 2'''
print()
class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


def realizar_atacque(personaje):
    personaje.atacar()


# Instancias
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# Iterable de personajes
personajes = [mago, arquero, samurai]

# Ataque conjugado
for p in personajes:
    realizar_atacque(p)

'''
realizar_atacque(mago)     # Salida: Ataque mágico
realizar_atacque(arquero)  # Salida: Lanzamiento de flecha
realizar_atacque(samurai)  # Salida: Ataque con katana
'''

''' EJemplo 3'''
print()
class Mago():
    def defender(self):
        print("Escudo mágico")


class Arquero():
    def defender(self):
        print("Esconderse")


class Samurai():
    def defender(self):
        print("Bloqueo")


def personaje_defender(personaje):
    personaje.defender()


# Instancias
mago = Mago()
arquero = Arquero()
samurai = Samurai()
# Iterable de personajes
personajes = [mago, arquero, samurai]
# Defensa conjugada
for p in personajes:
    personaje_defender(p)

'''
personaje_defender(mago)     # Salida: Escudo mágico
personaje_defender(arquero)  # Salida: Esconderse
personaje_defender(samurai)  # Salida: Bloqueo
'''

