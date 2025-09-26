from datetime import datetime

class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.pedidos = []

    def realizar_pedido(self, detalles):
        pedido = Pedido(self, detalles)
        self.pedidos.append(pedido)
        print(f"Pedido {pedido.id_pedido} creado para {self.nombre}.")
        return pedido

    def __str__(self):
        return f"{self.nombre} ({self.correo})"


class Pedido:
    contador_id = 1
    ESTADOS = ["Pendiente", "Procesando", "Enviado", "Entregado", "Cancelado"]

    def __init__(self, cliente, detalles):
        self.id_pedido = Pedido.contador_id
        Pedido.contador_id += 1
        self.cliente = cliente
        self.detalles = detalles
        self.estado = "Pendiente"
        self.fecha_creacion = datetime.now()
        self.fecha_entrega = None

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in Pedido.ESTADOS:
            self.estado = nuevo_estado
            if nuevo_estado == "Entregado":
                self.fecha_entrega = datetime.now()
            print(f"Pedido {self.id_pedido} actualizado a estado '{self.estado}'.")
        else:
            print("Estado inválido.")

    def calcular_total(self):
        return sum(detalle.subtotal() for detalle in self.detalles)

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.estado} - Total: ${self.calcular_total():.2f}"


class DetallePedido:
    def __init__(self, producto, cantidad, precio_unitario):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.producto} x{self.cantidad} = ${self.subtotal():.2f}"


# --- Ejemplo de uso ---
cliente1 = Cliente("Laura Gómez", "laura@example.com")

# Crear pedido con detalles
detalles = [
    DetallePedido("Laptop", 1, 3500),
    DetallePedido("Mouse", 2, 80),
]
pedido1 = cliente1.realizar_pedido(detalles)

print("\n--- Resumen Pedido ---")
print(pedido1)
for d in pedido1.detalles:
    print(d)

# Cambiar estados
pedido1.cambiar_estado("Procesando")
pedido1.cambiar_estado("Enviado")
pedido1.cambiar_estado("Entregado")

print("\n--- Seguimiento Final ---")
print(pedido1)
