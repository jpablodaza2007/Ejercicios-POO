class Temperatura:
    def __init__(self, valor, escala="C"):
        self.valor = valor
        self.escala = escala.upper()
    
    def a_celsius(self):
        if self.escala == "C":
            return self.valor
        elif self.escala == "F":
            return (self.valor - 32) * 5/9
        elif self.escala == "K":
            return self.valor - 273.15
        else:
            raise ValueError("Escala no válida. Usa 'C', 'F' o 'K'.")

    def a_fahrenheit(self):
        celsius = self.a_celsius()
        return (celsius * 9/5) + 32

    def a_kelvin(self):
        celsius = self.a_celsius()
        return celsius + 273.15

    def __str__(self):
        return f"{self.valor}°{self.escala}"

# Ejemplo de uso:
t1 = Temperatura(100, "C")
print(f"{t1} en Fahrenheit: {t1.a_fahrenheit():.2f}°F")
print(f"{t1} en Kelvin: {t1.a_kelvin():.2f}K")

t2 = Temperatura(32, "F")