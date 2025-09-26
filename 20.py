from abc import ABC, abstractmethod

class Instrumento(ABC):
    """Clase base abstracta para instrumentos musicales."""
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def tocar(self):
        """Cada instrumento debe implementar su forma de tocar."""
        pass

    def __str__(self):
        return f"Instrumento: {self.nombre}"


class Guitarra(Instrumento):
    def __init__(self, nombre="Guitarra"):
        super().__init__(nombre)

    def tocar(self):
        return "Rasgueando las cuerdas de la guitarra 🎸"


class Piano(Instrumento):
    def __init__(self, nombre="Piano"):
        super().__init__(nombre)

    def tocar(self):
        return "Tocando las teclas del piano 🎹"


class Bateria(Instrumento):
    def __init__(self, nombre="Batería"):
        super().__init__(nombre)

    def tocar(self):
        return "Golpeando los tambores y platillos de la batería 🥁"
instrumentos = [Guitarra(), Piano(), Bateria()]

for inst in instrumentos:
    print(inst, "->", inst.tocar())
