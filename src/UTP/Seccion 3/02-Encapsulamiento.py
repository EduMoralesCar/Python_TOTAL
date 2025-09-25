'''
Ejemplo: Sistema de cuentas bancarias
'''

class CuentaBancaria:
    def __init__(self,titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial # Atributo Privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return monto # Retorna el monto despositado
        else:
            raise ValueError("El monto debe ser positivo")

    def retirar(self,monto):
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes")
        self.__saldo -= monto
        return monto # Retorna el monto retirado

    def obtener_saldo(self):
        return self.__saldo

    def __auditoria_interna(self):
        print(f"Auditoria: {self.titular} tiene s/.{self.__saldo}")

# Uso
cuenta = CuentaBancaria("Edu Morales", 500)

print("Cuenta Bancaria inicial:", cuenta.obtener_saldo())
print("Depositamos:", cuenta.depositar(300))
print("Actualizamos la cuenta bancaria:", cuenta.obtener_saldo())
print("Retiramos:", cuenta.retirar(450))
print("Saldo Disponible, despues del retiro:", cuenta.obtener_saldo())
