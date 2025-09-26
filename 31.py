from datetime import datetime, timedelta

class Ruta:
    def __init__(self, nombre, paradas, hora_inicio, intervalo_minutos):
        self.nombre = nombre
        self.paradas = paradas  # lista de paradas
        self.hora_inicio = hora_inicio
        self.intervalo = intervalo_minutos

    def horarios(self, cantidad=5):
        horarios = []
        hora = self.hora_inicio
        for _ in range(cantidad):
            horarios.append(hora)
            hora += timedelta(minutes=self.intervalo)
        return horarios

    def __str__(self):
        return f"Ruta {self.nombre} con paradas: {', '.join(self.paradas)}"


class Vehiculo:
    def __init__(self, id_vehiculo, capacidad, ruta):
        self.id_vehiculo = id_vehiculo
        self.capacidad = capacidad
        self.ruta = ruta
        self.pasajeros = []

    def abordar(self, pasajero):
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajero)
            print(f"{pasajero.nombre} abordó el vehículo {self.id_vehiculo}.")
        else:
            print(f"❌ El vehículo {self.id_vehiculo} está lleno.")

    def bajar(self, pasajero):
        if pasajero in self.pasajeros:
            self.pasajeros.remove(pasajero)
            print(f"{pasajero.nombre} bajó del vehículo {self.id_vehiculo}.")

    def __str__(self):
        return f"Vehículo {self.id_vehiculo} en {self.ruta.nombre} | Pasajeros: {len(self.pasajeros)}/{self.capacidad}"


class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino

    def __str__(self):
        return f"{self.nombre} → {self.destino}"


# --- Ejemplo de uso ---
hora_inicio = datetime(2025, 9, 26, 6, 0)
ruta1 = Ruta("A", ["Centro", "Estación", "Universidad", "Barrio Norte"], hora_inicio, 20)

vehiculo1 = Vehiculo("Bus-101", capacidad=3, ruta=ruta1)

p1 = Pasajero("Ana", "Universidad")
p2 = Pasajero("Luis", "Centro")
p3 = Pasajero("Carla", "Barrio Norte")
p4 = Pasajero("Pedro", "Estación")

# Pasajeros abordan
vehiculo1.abordar(p1)
vehiculo1.abordar(p2)
vehiculo1.abordar(p3)
vehiculo1.abordar(p4)  # Este no cabe

print("\n--- Estado del vehículo ---")
print(vehiculo1)

print("\n--- Horarios de salida de la ruta ---")
for h in ruta1.horarios(4):
    print(h.strftime("%H:%M"))
