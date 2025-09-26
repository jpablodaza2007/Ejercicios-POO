from datetime import datetime, timedelta
from statistics import mean

class Producto:
    def __init__(self, codigo, nombre, stock_inicial, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock_inicial
        self.precio = precio
        self.historial_ventas = []  # (fecha, cantidad)

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            self.historial_ventas.append((datetime.now(), cantidad))
        else:
            print(f"No hay suficiente stock de {self.nombre}.")

    def reabastecer(self, cantidad):
        self.stock += cantidad

    def prediccion_stock(self, dias=7):
        if not self.historial_ventas:
            return f"Sin datos suficientes para predecir ventas de {self.nombre}."
        # Promedio de ventas por día
        ventas_diarias = {}
        for fecha, cant in self.historial_ventas:
            dia = fecha.date()
            ventas_diarias[dia] = ventas_diarias.get(dia, 0) + cant
        promedio = mean(ventas_diarias.values())
        stock_estimado = self.stock - promedio * dias
        return f"Stock estimado de {self.nombre} en {dias} días: {stock_estimado:.1f}"

    def __str__(self):
        return f"{self.nombre} (Stock: {self.stock}, Precio: ${self.precio})"


class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __str__(self):
        return f"Proveedor: {self.nombre} ({len(self.productos)} productos)"


class Orden:
    def __init__(self, proveedor, producto, cantidad):
        self.proveedor = proveedor
        self.producto = producto
        self.cantidad = cantidad
        self.fecha = datetime.now()
        self.estado = "pendiente"

    def completar(self):
        self.producto.reabastecer(self.cantidad)
        self.estado = "completada"

    def __str__(self):
        return f"Orden {self.estado}: {self.cantidad} x {self.producto.nombre} a {self.proveedor.nombre} ({self.fecha.date()})"


class Almacen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.ordenes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def realizar_orden(self, proveedor, producto, cantidad):
        orden = Orden(proveedor, producto, cantidad)
        self.ordenes.append(orden)
        return orden

    def reporte_stock(self):
        print(f"\n📦 Reporte de stock en {self.nombre}:")
        for p in self.productos:
            print("-", p)

    def __str__(self):
        return f"Almacén: {self.nombre} ({len(self.productos)} productos)"
    

# --- Ejemplo de uso ---
# Proveedor y productos
prov = Proveedor("TechSupply")
p1 = Producto("P001", "Laptop", 20, 1200)
p2 = Producto("P002", "Mouse", 100, 25)

prov.agregar_producto(p1)
prov.agregar_producto(p2)

# Almacén
alm = Almacen("Central")
alm.agregar_producto(p1)
alm.agregar_producto(p2)

# Ventas
p1.vender(3)
p1.vender(2)
p2.vender(10)
p2.vender(5)

# Orden de reabastecimiento
orden1 = alm.realizar_orden(prov, p1, 10)
orden1.completar()

# Reportes
alm.reporte_stock()
print("\n🔮 Predicciones:")
print(p1.prediccion_stock(7))
print(p2.prediccion_stock(7))
