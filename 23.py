import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"


class Baraja:
    valores = ["A", "2", "3", "4", "5", "6", "7",
               "8", "9", "10", "J", "Q", "K"]
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]

    def __init__(self):
        self.cartas = [Carta(valor, palo) for palo in self.palos for valor in self.valores]

    def mezclar(self):
        random.shuffle(self.cartas)

    def repartir(self, cantidad):
        mano = []
        for _ in range(cantidad):
            if self.cartas:
                mano.append(self.cartas.pop())
        return mano


class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_cartas(self, cartas):
        self.cartas.extend(cartas)

    def mostrar(self):
        return ", ".join(str(carta) for carta in self.cartas)


# Ejemplo de uso
baraja = Baraja()
baraja.mezclar()

mano_jugador = Mano()
mano_maquina = Mano()

mano_jugador.agregar_cartas(baraja.repartir(5))
mano_maquina.agregar_cartas(baraja.repartir(5))

print("Mano del jugador:", mano_jugador.mostrar())
print("Mano de la máquina:", mano_maquina.mostrar())
print("Cartas restantes en la baraja:", len(baraja.cartas))
