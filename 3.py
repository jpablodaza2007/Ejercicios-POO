class CuentaBanco:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, monto):
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0:
            self.__saldo += monto
            print(f"Has depositado {monto}. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto a depositar debe ser mayor que 0.")

    def retirar(self, monto):
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= 0:
            print("El monto a retirar debe ser mayor que 0.")
        elif monto > self.__saldo:
            print("Fondos insuficientes.")
        else:
            self.__saldo -= monto
            print(f"Has retirado {monto}. Nuevo saldo: {self.__saldo}")

    def consultar_saldo(self):
        return self.__saldo



cuenta = CuentaBanco(0)
cuenta.depositar(0)
cuenta.retirar(0)
print("Saldo actual:", cuenta.consultar_saldo())
