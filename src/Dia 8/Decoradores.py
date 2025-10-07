def decorar_saludo(funcion):
    def nueva_funcion(nombre):
        return "Hola, " + funcion(nombre)
    return nueva_funcion

@decorar_saludo
def obtener_nombre(nombre):
    return nombre.upper()

print(obtener_nombre("Morales"))