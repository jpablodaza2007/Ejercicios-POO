from datetime import datetime, timedelta

class Cuenta:
    def __init__(self, numero, titular, saldo_inicial=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial
        self.transacciones = []
        self.tarjetas = []
        self.prestamos = []

    def depositar(self, monto):
        self.saldo += monto
        self.transacciones.append(Transaccion("Deposito", monto, self))
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            self.transacciones.append(Transaccion("Retiro", monto, self))
        else:
            print("Fondos insuficientes.")
    
    def emitir_tarjeta(self, tipo="debito"):
        tarjeta = Tarjeta(self, tipo)
        self.tarjetas.append(tarjeta)
        return tarjeta

    def solicitar_prestamo(self, monto, tasa_interes, plazo_meses):
        prestamo = Prestamo(self, monto, tasa_interes, plazo_meses)
        self.prestamos.append(prestamo)
        self.depositar(monto)  # se abona a la cuenta
        return prestamo

    def mostrar_estado(self):
        print(f"\n🏦 Cuenta {self.numero} de {self.titular}")
        print(f"Saldo: ${self.saldo:.2f}")
        print("Transacciones:")
        for t in self.transacciones:
            print(" -", t)
        print("Tarjetas:")
        for tar in self.tarjetas:
            print(" -", tar)
        print("Préstamos:")
        for p in self.prestamos:
            print(" -", p)

    def __str__(self):
        return f"Cuenta {self.numero} ({self.titular})"


class Transaccion:
    def __init__(self, tipo, monto, cuenta):
        self.tipo = tipo
        self.monto = monto
        self.cuenta = cuenta
        self.fecha = datetime.now()

    def __str__(self):
        return f"{self.fecha.strftime('%Y-%m-%d %H:%M')} - {self.tipo}: ${self.monto:.2f}"


class Tarjeta:
    def __init__(self, cuenta, tipo="debito"):
        self.numero = f"****{str(hash(datetime.now()))[-4:]}"  # número ficticio
        self.tipo = tipo
        self.cuenta = cuenta
        self.estado = "activa"

    def bloquear(self):
        self.estado = "bloqueada"

    def __str__(self):
        return f"Tarjeta {self.tipo.upper()} {self.numero} ({self.estado})"


class Prestamo:
    def __init__(self, cuenta, monto, tasa_interes, plazo_meses):
        self.cuenta = cuenta
        self.monto = monto
        self.tasa_interes = tasa_interes
        self.plazo_meses = plazo_meses
        self.fecha_inicio = datetime.now()
        self.estado = "activo"
        self.saldo_pendiente = monto * (1 + tasa_interes * plazo_meses / 12)

    def pagar_cuota(self, monto):
        if self.estado != "activo":
            print("El préstamo no está activo.")
            return
        self.saldo_pendiente -= monto
        if self.saldo_pendiente <= 0:
            self.saldo_pendiente = 0
            self.estado = "pagado"

    def __str__(self):
        return f"Préstamo ${self.monto:.2f}, interés {self.tasa_interes*100:.1f}%, saldo pendiente ${self.saldo_pendiente:.2f}, estado: {self.estado}"


# --- Ejemplo de uso ---
cuenta1 = Cuenta("001", "Ana", 1000)

# Operaciones
cuenta1.depositar(500)
cuenta1.retirar(200)

# Tarjeta
tarjeta = cuenta1.emitir_tarjeta("credito")

# Préstamo
prestamo = cuenta1.solicitar_prestamo(5000, 0.12, 12)
prestamo.pagar_cuota(1000)
prestamo.pagar_cuota(4500)

# Estado general
cuenta1.mostrar_estado()
