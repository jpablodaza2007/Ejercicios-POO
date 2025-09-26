from datetime import datetime, timedelta

class Huesped:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
        self.reservas = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.documento})"


class Habitacion:
    def __init__(self, numero, tipo, precio_noche):
        self.numero = numero
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.reservas = []

    def esta_disponible(self, fecha_inicio, fecha_fin):
        for reserva in self.reservas:
            if not (fecha_fin <= reserva.fecha_inicio or fecha_inicio >= reserva.fecha_fin):
                return False
        return True

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio_noche:.2f}/noche"


class Reserva:
    def __init__(self, huesped, habitacion, fecha_inicio, fecha_fin):
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.total = self.calcular_total()
        self.confirmada = False

    def calcular_total(self):
        noches = (self.fecha_fin - self.fecha_inicio).days
        return noches * self.habitacion.precio_noche

    def confirmar(self):
        if self.habitacion.esta_disponible(self.fecha_inicio, self.fecha_fin):
            self.habitacion.reservas.append(self)
            self.huesped.reservas.append(self)
            self.confirmada = True
            print(f"✅ Reserva confirmada para {self.huesped.nombre} en {self.habitacion}. Total: ${self.total:.2f}")
        else:
            print("❌ La habitación no está disponible en las fechas seleccionadas.")

    def __str__(self):
        estado = "Confirmada" if self.confirmada else "Pendiente"
        return f"Reserva de {self.huesped.nombre} - {self.habitacion} - {estado} - ${self.total:.2f}"


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def buscar_disponibles(self, fecha_inicio, fecha_fin):
        disponibles = [h for h in self.habitaciones if h.esta_disponible(fecha_inicio, fecha_fin)]
        print(f"\n🔎 Habitaciones disponibles en {self.nombre} del {fecha_inicio.date()} al {fecha_fin.date()}:")
        for h in disponibles:
            print(h)
        return disponibles

    def __str__(self):
        return f"Hotel {self.nombre} - {len(self.habitaciones)} habitaciones"


# --- Ejemplo de uso ---
hotel = Hotel("Gran Hotel")

# Habitaciones
h1 = Habitacion(101, "Simple", 120)
h2 = Habitacion(102, "Doble", 200)
hotel.agregar_habitacion(h1)
hotel.agregar_habitacion(h2)

# Huesped
cliente = Huesped("Ana Torres", "CC12345")

# Fechas de reserva
inicio = datetime(2025, 10, 1)
fin = datetime(2025, 10, 5)

# Buscar disponibilidad
hotel.buscar_disponibles(inicio, fin)

# Crear reserva
reserva1 = Reserva(cliente, h1, inicio, fin)
reserva1.confirmar()

print("\n--- Facturación ---")
print(reserva1)
