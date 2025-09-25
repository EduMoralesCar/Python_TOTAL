# Crear una clase que administre la información de un
# dispositivo de almacenamiento, considerando los atributos:
# número de serie, una etiqueta, capacidad total, espacio ocupado.
# Incluir métodos para ocupar y desocupar espacio
# y un método que muestre el espacio disponible.

class DispositivoAlmacenamiento:
    etiqueta = ''
    numero_serie = ''
    capacidad_total = 0
    espacio_ocupado = 0

    def __init__(self, etiqueta, numero_serie, capacidad_total):
        self.etiqueta = etiqueta
        self.numero_serie = numero_serie
        self.capacidad_total = capacidad_total

    def asignar_espacio(self, total_bytes):
        if self.espacio_ocupado + total_bytes <= self.capacidad_total:
            self.espacio_ocupado += total_bytes
            return True
        
        return False
    
    def liberar_espacio(self, total_bytes):
        if self.espacio_ocupado > 0:
            if total_bytes >= self.espacio_ocupado:
                self.espacio_ocupado = 0
            else:
                self.espacio_ocupado -= total_bytes
            
            return True
        else:
            return False


disco1 = DispositivoAlmacenamiento("C:\\", "HD00987", 30000)
disco1.asignar_espacio(2000)
disco1.asignar_espacio(1500)
disco1.liberar_espacio(500)
disco1.liberar_espacio(250)

print(f'Dispositivo "{disco1.etiqueta}", ' \
      f'capacidad: {disco1.capacidad_total} bytes')
print('Espacio disponible: ' + \
      str(disco1.capacidad_total - disco1.espacio_ocupado) + " bytes")
