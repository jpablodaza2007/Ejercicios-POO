class circulo:
    def __init__(self, radio, metodo_area,circunferencia,comparacion):
        self.radio = radio
        self.metodo_area = metodo_area
        self.circunferencia = circunferencia
        self.comparacion = comparacion
    def area(self):
        return self.metodo_area(self.radio)
    def perimetro(self):
        return self.circunferencia(self.radio)
    def comparar(self, otro_circulo):
        return self.comparacion(self.radio, otro_circulo.radio)
print("Circulo 1")
circulo1 = circulo(5, lambda r: 3.14 * r *  r, lambda r: 2 * 3.14 * r, lambda r1, r2: r1 > r2)
print(f"Area: {circulo1.area()}")    
print(f"Perimetro: {circulo1.perimetro()}")
print("Circulo 2")
circulo2 = circulo(3, lambda r: 3.14 * r *  r, lambda r: 2 * 3.14 * r, lambda r1, r2: r1 > r2)
print(f"Area: {circulo2.area()}")
print(f"Perimetro: {circulo2.perimetro()}")
print("Comparacion de circulos")
if circulo1.comparar(circulo2):
    print("El circulo 1 es mayor que el circulo 2")