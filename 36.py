from datetime import datetime

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = Carrito(self)
        self.ordenes = []

    def __str__(self):
        return f"{self.nombre} ({self.correo})"


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"


class Carrito:
    def __init__(self, usuario):
        self.usuario = usuario
        self.items = []

    def agregar_producto(self, producto, cantidad=1):
        self.items.append({"producto": producto, "cantidad": cantidad})
        print(f"🛒 {cantidad} x {producto.nombre} agregado al carrito.")

    def calcular_total(self):
        return sum(item["producto"].precio * item["cantidad"] for item in self.items)

    def vaciar(self):
        self.items = []

    def mostrar(self):
        print(f"\nCarrito de {self.usuario.nombre}:")
        for item in self.items:
            print(f"- {item['producto'].nombre} x{item['cantidad']} = ${item['producto'].precio * item['cantidad']:.2f}")
        print(f"Total: ${self.calcular_total():.2f}")


class Orden:
    contador_id = 1

    def __init__(self, usuario, carrito):
        self.id_orden = Orden.contador_id
        Orden.contador_id += 1
        self.usuario = usuario
        self.items = carrito.items.copy()
        self.total = carrito.calcular_total()
        self.fecha = datetime.now()
        self.estado = "Pendiente"
        self.pago = None

    def registrar_pago(self, metodo, monto):
        if monto < self.total:
            print("❌ Pago insuficiente.")
            return None
        self.pago = Pago(self, metodo, monto)
        self.estado = "Pagada"
        print(f"✅ Orden {self.id_orden} pagada con {metodo}.")
        return self.pago

    def __str__(self):
        return f"Orden {self.id_orden} - {self.usuario.nombre} - Estado: {self.estado} - Total: ${self.total:.2f}"


class Pago:
    def __init__(self, orden, metodo, monto):
        self.orden = orden
        self.metodo = metodo
        self.monto = monto
        self.fecha = datetime.now()

    def __str__(self):
        return f"Pago de ${self.monto:.2f} vía {self.metodo} el {self.fecha.strftime('%Y-%m-%d %H:%M')}"


# --- Ejemplo de uso ---
u1 = Usuario("Laura", "laura@example.com")

# Crear productos
p1 = Producto("Laptop", 3500)
p2 = Producto("Mouse", 80)

# Carrito
u1.carrito.agregar_producto(p1, 1)
u1.carrito.agregar_producto(p2, 2)
u1.carrito.mostrar()

# Crear orden
orden1 = Orden(u1, u1.carrito)
u1.ordenes.append(orden1)
u1.carrito.vaciar()

print("\n--- Orden generada ---")
print(orden1)

# Registrar pago
orden1.registrar_pago("Tarjeta de Crédito", 3660)
print(orden1.pago)
