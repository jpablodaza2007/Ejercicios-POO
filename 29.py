from datetime import datetime

class Recurso:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.reservas = []

    def esta_disponible(self, fecha):
        return all(reserva.fecha != fecha for reserva in self.reservas)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []

    def reservar(self, recurso, fecha):
        if recurso.esta_disponible(fecha):
            reserva = Reserva(self, recurso, fecha)
            self.reservas.append(reserva)
            recurso.reservas.append(reserva)
            print(f"{self.nombre} reservó {recurso.nombre} para {fecha.strftime('%Y-%m-%d %H:%M')}")
            return reserva
        else:
            print(f"❌ El recurso {recurso.nombre} no está disponible en esa fecha.")

    def __str__(self):
        return self.nombre


class Reserva:
    def __init__(self, usuario, recurso, fecha):
        self.usuario = usuario
        self.recurso = recurso
        self.fecha = fecha

    def __str__(self):
        return f"{self.recurso.nombre} reservado por {self.usuario} en {self.fecha.strftime('%Y-%m-%d %H:%M')}"


# Ejemplo de uso
sala1 = Recurso("Sala de reuniones 101", "Sala")
equipo1 = Recurso("Proyector Epson", "Equipo")

usuario1 = Usuario("Ana")
usuario2 = Usuario("Luis")

fecha1 = datetime(2025, 9, 26, 10, 0)
fecha2 = datetime(2025, 9, 26, 15, 0)

# Reservas
usuario1.reservar(sala1, fecha1)
usuario2.reservar(sala1, fecha1)  # No debería dejar, ya está ocupada
usuario2.reservar(sala1, fecha2)  # Diferente hora, sí permite
usuario1.reservar(equipo1, fecha1)

print("\n--- Reservas de Sala ---")
for r in sala1.reservas:
    print(r)

print("\n--- Reservas de Usuario Ana ---")
for r in usuario1.reservas:
    print(r)
