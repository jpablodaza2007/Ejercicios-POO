from abc import ABC, abstractmethod
import math
from typing import Optional, Tuple


class Forma(ABC):
    """Clase base abstracta para cualquier forma geométrica."""
    @abstractmethod
    def area(self) -> float:
        """Devuelve el área de la forma."""
        pass

    @abstractmethod
    def perimetro(self) -> float:
        """Devuelve el perímetro de la forma."""
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


class Poligono(Forma, ABC):
    """Clase base para polígonos. Aquí podemos añadir comportamientos comunes."""
    def __init__(self, lados: int):
        if lados < 3:
            raise ValueError("Un polígono debe tener al menos 3 lados.")
        self.lados = lados


class Triangulo(Poligono):
    """
    Triangulo puede construirse de dos formas:
    - con tres lados (a, b, c) -> area por Herón
    - con base y altura -> area = 0.5 * base * altura
    """
    def __init__(self,
                 lados: Optional[Tuple[float, float, float]] = None,
                 base_altura: Optional[Tuple[float, float]] = None):
        super().__init__(3)
        if lados is None and base_altura is None:
            raise ValueError("Proporcione 'lados' o 'base_altura' para el triángulo.")
        self._lados = None
        self._base = None
        self._altura = None

        if lados:
            a, b, c = lados
            if any(x <= 0 for x in (a, b, c)):
                raise ValueError("Los lados deben ser positivos.")
            # Validar desigualdad triangular
            if not (a + b > c and a + c > b and b + c > a):
                raise ValueError("Los lados no cumplen la desigualdad triangular.")
            self._lados = (float(a), float(b), float(c))

        if base_altura:
            base, altura = base_altura
            if base <= 0 or altura <= 0:
                raise ValueError("Base y altura deben ser positivas.")
            self._base = float(base)
            self._altura = float(altura)

    def area(self) -> float:
        if self._lados:
            a, b, c = self._lados
            s = (a + b + c) / 2.0
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return area
        else:
            return 0.5 * self._base * self._altura

    def perimetro(self) -> float:
        if self._lados:
            return sum(self._lados)
        else:
            # Si sólo tenemos base+altura no conocemos los otros lados;
            # asumimos triángulo isósceles con lados iguales derivados (opcional).
            # Aquí lanzamos excepción porque el perímetro no puede calcularse con sólo base+altura.
            raise ValueError("Perímetro no disponible si sólo se proporcionó base y altura.")

    def __str__(self):
        if self._lados:
            return f"Triángulo(lados={self._lados})"
        else:
            return f"Triángulo(base={self._base}, altura={self._altura})"


class Cuadrado(Poligono):
    """Cuadrado regular definido por la longitud del lado."""
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que 0.")
        super().__init__(4)
        self.lado = float(lado)

    def area(self) -> float:
        return self.lado * self.lado

    def perimetro(self) -> float:
        return 4 * self.lado

    def __str__(self):
        return f"Cuadrado(lado={self.lado})"


class Pentagono(Poligono):
    """
    Pentágono regular (todos los lados y ángulos iguales).
    Fórmula del área para pentágono regular de lado a:
      area = (1/4) * sqrt(5(5+2*sqrt(5))) * a^2
    Perímetro = 5 * a
    """
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que 0.")
        super().__init__(5)
        self.lado = float(lado)

    def area(self) -> float:
        a = self.lado
        factor = math.sqrt(5 * (5 + 2 * math.sqrt(5)))
        return 0.25 * factor * a * a

    def perimetro(self) -> float:
        return 5 * self.lado

    def __str__(self):
        return f"Pentágono regular(lado={self.lado})"
    
# Triángulo por lados (Herón)
t1 = Triangulo(lados=(3, 4, 5))
print(t1)                    # Triángulo(lados=(3.0, 4.0, 5.0))
print("Área:", t1.area())    # 6.0
print("Perímetro:", t1.perimetro())  # 12.0

# Triángulo por base y altura
t2 = Triangulo(base_altura=(10, 4))
print(t2)                    # Triángulo(base=10.0, altura=4.0)
print("Área:", t2.area())    # 20.0
# t2.perimetro() -> ValueError

# Cuadrado
c = Cuadrado(5)
print(c)                     # Cuadrado(lado=5.0)
print("Área:", c.area())     # 25.0
print("Perímetro:", c.perimetro())  # 20.0

# Pentágono regular
p = Pentagono(3)
print(p)                     # Pentágono regular(lado=3.0)
print("Área:", p.area())     # ~15.484
print("Perímetro:", p.perimetro())  # 15.0
