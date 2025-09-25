# Clase padre
class universidad:
    def __init__(self,nombre, ano_lanzamiento):
        self.nombre = nombre
        self.ano_lanzamiento = ano_lanzamiento

    def mostrar_info(self):
        print(f"Universidad: {self.nombre}, fundada en {self.ano_lanzamiento}")

# Aplicamos herencia
class sedeLima(universidad):
    def __init__(self,nombre, ano_lanzamiento, direccion):
        super().__init__(nombre, ano_lanzamiento)
        self.direccion = direccion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Sede Lima ubicada en: {self.direccion}")


class sedeArequipa(universidad):
    def __init__(self, nombre, ano_lanzamiento, direccion):
        super().__init__(nombre, ano_lanzamiento)
        self.direccion = direccion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Sede Arequipa ubicada en: {self.direccion}")


class sedeTrujillo(universidad):
    def __init__(self, nombre, ano_lanzamiento, direccion):
        super().__init__(nombre, ano_lanzamiento)
        self.direccion = direccion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Sede Trujillo ubicada en: {self.direccion}")

# Ejemplo de uso

lima = sedeLima("Lima Centro", 2002, "Av. Arequipa 1234, Lima")
arequipa = sedeArequipa("UTP", 2002, "Av. Ejército 567, Arequipa")
trujillo = sedeTrujillo("UTP Trujillo", 2022 , "Avenida Nicolas de Pierola 1221, Trujillo 13001")

# Mostramos
lima.mostrar_info()
print()
arequipa.mostrar_info()
print()
trujillo.mostrar_info()