class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se depositaron ${monto}. Saldo actual: ${self.saldo}")
        else:
            print("El depósito debe ser positivo.")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Se retiraron ${monto}. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes.")

    def consultar_saldo(self):
        return f"Saldo de {self.titular}: ${self.saldo}"


class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo=0, interes=0.02):
        super().__init__(titular, saldo)
        self.interes = interes  # 2% por defecto

    def aplicar_interes(self):
        ganancia = self.saldo * self.interes
        self.saldo += ganancia
        print(f"Se aplicó interés de {self.interes*100}%. Ganancia: ${ganancia:.2f}. Saldo actual: ${self.saldo:.2f}")


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo=0, sobregiro=500):
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro  # límite de sobregiro

    def retirar(self, monto):
        if monto <= self.saldo + self.sobregiro:
            self.saldo -= monto
            print(f"Se retiraron ${monto}. Saldo actual: ${self.saldo}")
        else:
            print("Límite de sobregiro excedido.")


# Ejemplo de uso
ahorros = CuentaAhorros("Ana", 1000, interes=0.05)
corriente = CuentaCorriente("Luis", 300, sobregiro=200)

print("\n--- Cuenta de Ahorros ---")
print(ahorros.consultar_saldo())
ahorros.aplicar_interes()

print("\n--- Cuenta Corriente ---")
print(corriente.consultar_saldo())
corriente.retirar(400)  # dentro del saldo
corriente.retirar(200)  # usa sobregiro
corriente.retirar(500)  # excede límite
