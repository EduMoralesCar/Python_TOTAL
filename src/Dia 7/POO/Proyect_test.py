class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_cliente(self):
        return f"Cliente: {self.nombre} {self.apellido}\nCuenta: {self.numero_cuenta}\nBalance: ${self.balance}"

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            return f"Depósito exitoso de ${monto}.\nNuevo balance: ${self.balance}"
        else:
            return "El monto a depositar debe ser positivo."

    def retirar(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
            return f"Retiro exitoso de ${monto}.\nNuevo balance: ${self.balance}"
        elif monto > self.balance:
            return "Fondos insuficientes para el retiro."
        else:
            return "El monto a retirar debe ser positivo."

'''
    Elegir depositar, retirar o salir
'''

cliente1 = Cliente("Juan", "Perez", "123456789", 1000)

# Imprimir en la Consola
print(cliente1.imprimir_cliente())
print()
print(cliente1.depositar(500))
print()
print(cliente1.retirar(300))
