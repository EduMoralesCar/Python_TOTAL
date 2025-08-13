class Universidad:
    def __init__(self, nombre, sede, facultades):
        self.nombre = nombre
        self.sede = sede
        self.facultades = facultades

    def SedeUniversitaria(self):
        return f"La sede de la {self.nombre} es {self.sede}."

    def FacultadesUniversitarias(self):
        return f"La {self.nombre} cuenta con las siguientes facultades:\n{'\n'.join(self.facultades)}."


# Creación de un objeto de la clase Universidad
universidad1 = Universidad(
    "Universidad Tecnologica del Perú",
    "Lima Norte",
    ["Facultad de Ingeniería", "Facultad de Ciencias", "Facultad de Derecho"]
)
universidad2 = Universidad(
    "Universidad Nacional de Ingeniería",
    "Lima Centro",
    ["Facultad de Ingeniería Civil", "Facultad de Ingeniería Electrónica", "Facultad de Arquitectura"]
)
universidad3 = Universidad(
    "Universidad de Lima",
    "Lima Sur",
    ["Facultad de Ciencias Empresariales", "Facultad de Ingeniería Industrial", "Facultad de Comunicaciones"]
)

# Presentación de la información de la universidad
print()
print(universidad1.SedeUniversitaria())
print(universidad2.SedeUniversitaria())
print(universidad3.SedeUniversitaria())
print()
print(universidad1.FacultadesUniversitarias(),'\n')
print(universidad2.FacultadesUniversitarias(),'\n')
print(universidad3.FacultadesUniversitarias(),'\n')

