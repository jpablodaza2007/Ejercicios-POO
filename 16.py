class Vehiculo:
    def __init__(self, marca, modelo, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas

    def descripcion(self):
        return f"{self.marca} {self.modelo} con {self.ruedas} ruedas"


class Carro(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo, 4)
        self.puertas = puertas

    def descripcion(self):
        return f"Carro: {super().descripcion()}, {self.puertas} puertas"


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo, 2)
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"Motocicleta: {super().descripcion()}, {self.cilindrada}cc"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, 2)
        self.tipo = tipo  # Ej: montaña, ruta, eléctrica

    def descripcion(self):
        return f"Bicicleta: {super().descripcion()}, tipo {self.tipo}"
carro = Carro("Toyota", "Corolla", 4)
moto = Motocicleta("Yamaha", "MT-07", 689)
bici = Bicicleta("Trek", "Marlin 7", "Montaña")

print(carro.descripcion())
print(moto.descripcion())
print(bici.descripcion())
