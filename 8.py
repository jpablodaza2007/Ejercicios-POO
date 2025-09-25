class tienda:
    def __init__(self, factura):
        self.productos = []
        self.factura = factura

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")
    def stock_total(self):
        total = sum(producto['precio'] for producto in self.productos)
        print(f"Stock total: {total}")
    def descuento(self, porcentaje):
        for producto in self.productos:
            producto['precio'] *= (1 - porcentaje / 100)

mi_tienda = tienda(factura=12)
mi_tienda.agregar_producto({'nombre': 'Manzana', 'precio': 1000})
mi_tienda.agregar_producto({'nombre': 'Banana', 'precio': 200})
mi_tienda.mostrar_productos()
mi_tienda.stock_total()
mi_tienda.descuento(10)
mi_tienda.mostrar_productos()