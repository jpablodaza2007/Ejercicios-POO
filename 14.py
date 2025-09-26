import random

class Dado:
    def __init__(self, caras=6):
        if caras < 2:
            raise ValueError("Un dado debe tener al menos 2 caras.")
        self.caras = caras
        self.historial = []  # Guardar resultados de los lanzamientos

    def lanzar(self):
        resultado = random.randint(1, self.caras)
        self.historial.append(resultado)
        return resultado

    def estadisticas(self):
        total = len(self.historial)
        if total == 0:
            return "Aún no se ha lanzado el dado."
        
        conteo = {i: self.historial.count(i) for i in range(1, self.caras + 1)}
        porcentajes = {k: (v / total) * 100 for k, v in conteo.items()}
        
        return {
            "total_lanzamientos": total,
            "conteo": conteo,
            "porcentajes": porcentajes
        }

    def __str__(self):
        return f"Dado de {self.caras} caras"
dado = Dado(6)

print(dado)

# Lanzar el dado varias veces
for _ in range(10):
    print("Lanzamiento:", dado.lanzar())

# Ver estadísticas
stats = dado.estadisticas()
print("Total lanzamientos:", stats["total_lanzamientos"])
print("Conteo por cara:", stats["conteo"])
print("Porcentajes:", stats["porcentajes"])
