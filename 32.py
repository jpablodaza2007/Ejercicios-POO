from datetime import datetime

class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial = []
        self.citas = []

    def agregar_historial(self, descripcion):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.historial.append(f"{fecha}: {descripcion}")

    def mostrar_historial(self):
        print(f"\nHistorial médico de {self.nombre}:")
        for registro in self.historial:
            print(f" - {registro}")

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"


class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.citas = []

    def programar_cita(self, paciente, fecha_hora):
        cita = Cita(paciente, self, fecha_hora)
        paciente.citas.append(cita)
        self.citas.append(cita)
        print(f"Cita programada: {paciente.nombre} con Dr. {self.nombre} el {fecha_hora.strftime('%Y-%m-%d %H:%M')}")
        return cita

    def __str__(self):
        return f"Dr. {self.nombre} ({self.especialidad})"


class Cita:
    def __init__(self, paciente, doctor, fecha_hora):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha_hora = fecha_hora
        self.atendida = False
        self.notas = ""

    def atender(self, notas):
        self.atendida = True
        self.notas = notas
        self.paciente.agregar_historial(f"Atendido por {self.doctor.nombre}: {notas}")

    def __str__(self):
        estado = "✅ Atendida" if self.atendida else "⏳ Pendiente"
        return f"{self.fecha_hora.strftime('%Y-%m-%d %H:%M')} - {self.paciente.nombre} con {self.doctor.nombre} [{estado}]"


# --- Ejemplo de uso ---
pac1 = Paciente("Ana", 30)
doc1 = Doctor("Martínez", "Cardiología")

# Programar citas
fecha1 = datetime(2025, 9, 27, 10, 30)
cita1 = doc1.programar_cita(pac1, fecha1)

fecha2 = datetime(2025, 9, 28, 9, 0)
cita2 = doc1.programar_cita(pac1, fecha2)

print("\n--- Citas programadas ---")
for c in pac1.citas:
    print(c)

# Atender una cita
cita1.atender("Chequeo general, presión arterial normal.")

# Mostrar historial médico actualizado
pac1.mostrar_historial()
