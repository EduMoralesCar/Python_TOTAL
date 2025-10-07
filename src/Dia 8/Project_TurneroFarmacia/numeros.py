#Decorador
def mensaje_turno(func):
    def envoltura():
        numero = func()
        return f"Su turno es: {numero}\nAguarde y será atendido."
    return envoltura

# Generadores
def generador_turnos(prefijo):
    contador = 1
    while True:
        yield f"{prefijo}-{contador}"
        contador += 1

turno_farmacia = generador_turnos("F")
turno_perfumeria = generador_turnos("P")
turno_cosmetica = generador_turnos("C")

@mensaje_turno
def siguiente_farmacia():
    return next(turno_farmacia)

@mensaje_turno
def siguiente_perfumeria():
    return next(turno_perfumeria)

@mensaje_turno
def siguiente_cosmetica():
    return next(turno_cosmetica)

