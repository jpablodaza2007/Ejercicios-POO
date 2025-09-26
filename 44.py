import random
from datetime import datetime

class Accion:
    def __init__(self, simbolo, nombre, precio_inicial):
        self.simbolo = simbolo
        self.nombre = nombre
        self.precio = precio_inicial
        self.historial_precios = [(datetime.now(), precio_inicial)]

    def actualizar_precio(self):
        # Variación aleatoria entre -5% y +5%
        variacion = random.uniform(-0.05, 0.05)
        self.precio *= (1 + variacion)
        self.precio = round(self.precio, 2)
        self.historial_precios.append((datetime.now(), self.precio))

    def __str__(self):
        return f"{self.simbolo} - {self.nombre}: ${self.precio}"


class Transaccion:
    def __init__(self, tipo, accion, cantidad, precio_unitario):
        self.tipo = tipo  # "compra" o "venta"
        self.accion = accion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.fecha = datetime.now()

    def __str__(self):
        return f"{self.fecha.strftime('%Y-%m-%d %H:%M')} - {self.tipo.upper()} {self.cantidad} x {self.accion.simbolo} @ ${self.precio_unitario}"


class Portafolio:
    def __init__(self, propietario, saldo_inicial=0):
        self.propietario = propietario
        self.saldo = saldo_inicial
        self.inversiones = {}  # simbolo -> cantidad
        self.transacciones = []

    def comprar(self, accion, cantidad):
        costo = accion.precio * cantidad
        if self.saldo >= costo:
            self.saldo -= costo
            self.inversiones[accion.simbolo] = self.inversiones.get(accion.simbolo, 0) + cantidad
            trans = Transaccion("compra", accion, cantidad, accion.precio)
            self.transacciones.append(trans)
            print(f"✅ Compra realizada: {cantidad} x {accion.simbolo} a ${accion.precio}")
        else:
            print("Fondos insuficientes para la compra.")

    def vender(self, accion, cantidad):
        if self.inversiones.get(accion.simbolo, 0) >= cantidad:
            self.inversiones[accion.simbolo] -= cantidad
            ingreso = accion.precio * cantidad
            self.saldo += ingreso
            trans = Transaccion("venta", accion, cantidad, accion.precio)
            self.transacciones.append(trans)
            print(f"💰 Venta realizada: {cantidad} x {accion.simbolo} a ${accion.precio}")
        else:
            print("No tienes suficientes acciones para vender.")

    def valor_total(self, mercado):
        valor_acciones = sum(mercado.obtener_precio(sim) * cant for sim, cant in self.inversiones.items())
        return self.saldo + valor_acciones

    def mostrar_portafolio(self, mercado):
        print(f"\n📊 Portafolio de {self.propietario}")
        print(f"Saldo disponible: ${self.saldo:.2f}")
        for sim, cant in self.inversiones.items():
            precio_actual = mercado.obtener_precio(sim)
            print(f"- {sim}: {cant} acciones (precio actual ${precio_actual}, valor total ${precio_actual * cant:.2f})")
        print(f"Valor total del portafolio: ${self.valor_total(mercado):.2f}")

    def historial_transacciones(self):
        print(f"\n📑 Historial de transacciones de {self.propietario}:")
        for t in self.transacciones:
            print("-", t)


class Mercado:
    def __init__(self):
        self.acciones = {}

    def agregar_accion(self, accion):
        self.acciones[accion.simbolo] = accion

    def fluctuar(self):
        for accion in self.acciones.values():
            accion.actualizar_precio()

    def mostrar_mercado(self):
        print("\n💹 Precios actuales del mercado:")
        for a in self.acciones.values():
            print("-", a)

    def obtener_precio(self, simbolo):
        return self.acciones[simbolo].precio if simbolo in self.acciones else 0


# --- Ejemplo de uso ---
mercado = Mercado()
a1 = Accion("AAPL", "Apple Inc.", 150)
a2 = Accion("TSLA", "Tesla Motors", 250)
a3 = Accion("AMZN", "Amazon", 3000)

mercado.agregar_accion(a1)
mercado.agregar_accion(a2)
mercado.agregar_accion(a3)

# Crear portafolio
p1 = Portafolio("Ana", saldo_inicial=10000)

# Comprar acciones
p1.comprar(a1, 20)
p1.comprar(a2, 10)

# Mercado fluctúa
mercado.fluctuar()
mercado.mostrar_mercado()

# Vender acciones
p1.vender(a1, 5)

# Estado del portafolio
p1.mostrar_portafolio(mercado)
p1.historial_transacciones()
