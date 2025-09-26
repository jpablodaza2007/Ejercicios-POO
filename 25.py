class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Producto:
    def __init__(self, nombre, precio, cantidad, categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - ${self.precio} | Stock: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def buscar_por_categoria(self, categoria):
        return [p for p in self.productos if p.categoria.nombre.lower() == categoria.lower()]

    def reporte_stock(self):
        print("=== Reporte de Stock ===")
        for p in self.productos:
            print(p)
        total = sum(p.cantidad for p in self.productos)
        print(f"Total de unidades en inventario: {total}")


# Ejemplo de uso
cat1 = Categoria("Electrónica")
cat2 = Categoria("Ropa")

p1 = Producto("Laptop", 3000, 5, cat1)
p2 = Producto("Camiseta", 50, 20, cat2)
p3 = Producto("Celular", 1500, 10, cat1)

inv = Inventario()
inv.agregar_producto(p1)
inv.agregar_producto(p2)
inv.agregar_producto(p3)

inv.reporte_stock()

print("\n--- Búsqueda por nombre: 'lap' ---")
for p in inv.buscar_por_nombre("lap"):
    print(p)

print("\n--- Búsqueda por categoría: 'Electrónica' ---")
for p in inv.buscar_por_categoria("Electrónica"):
    print(p)
