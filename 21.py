class ProductoCarrito:
    def __init__(self, nombre, precio, cantidad=1, descuento=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descuento = descuento  # porcentaje (ejemplo: 10 = 10%)

    def subtotal(self):
        total = self.precio * self.cantidad
        if self.descuento > 0:
            total -= total * (self.descuento / 100)
        return total

    def __str__(self):
        return f"{self.nombre} x{self.cantidad} - ${self.subtotal():.2f}"


class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(p.subtotal() for p in self.productos)

    def mostrar_carrito(self):
        print("=== Carrito de Compras ===")
        for p in self.productos:
            print(p)
        print(f"Total: ${self.calcular_total():.2f}")


# Ejemplo de uso
p1 = ProductoCarrito("Laptop", 3000, cantidad=1, descuento=10)
p2 = ProductoCarrito("Mouse", 50, cantidad=2)
p3 = ProductoCarrito("Teclado", 120, cantidad=1, descuento=5)

carrito = CarritoCompras()
carrito.agregar_producto(p1)
carrito.agregar_producto(p2)
carrito.agregar_producto(p3)

carrito.mostrar_carrito()
