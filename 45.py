from datetime import datetime

class Tratamiento:
    def __init__(self, descripcion, duracion_dias, medicamentos):
        self.descripcion = descripcion
        self.duracion_dias = duracion_dias
        self.medicamentos = medicamentos
        self.fecha_inicio = datetime.now()
        self.fecha_fin = self.fecha_inicio.replace(day=self.fecha_inicio.day + duracion_dias)

    def __str__(self):
        return (f"Tratamiento: {self.descripcion}, Duración: {self.duracion_dias} días, "
                f"Medicamentos: {', '.join(self.medicamentos)} "
                f"(Inicio: {self.fecha_inicio.strftime('%Y-%m-%d')}, Fin: {self.fecha_fin.strftime('%Y-%m-%d')})")


class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial = []

    def agregar_tratamiento(self, tratamiento, doctor):
        registro = {
            "fecha": datetime.now(),
            "doctor": doctor.nombre,
            "departamento": doctor.departamento.nombre,
            "tratamiento": tratamiento
        }
        self.historial.append(registro)

    def mostrar_historial(self):
        print(f"\n📋 Historial médico de {self.nombre} ({self.edad} años):")
        for h in self.historial:
            print(f"- Fecha: {h['fecha'].strftime('%Y-%m-%d %H:%M')}")
            print(f"  Doctor: {h['doctor']} ({h['departamento']})")
            print(f"  {h['tratamiento']}\n")


class Doctor:
    def __init__(self, nombre, especialidad, departamento):
        self.nombre = nombre
        self.especialidad = especialidad
        self.departamento = departamento
        self.pacientes_atendidos = []

    def atender_paciente(self, paciente, tratamiento):
        paciente.agregar_tratamiento(tratamiento, self)
        self.pacientes_atendidos.append(paciente.nombre)
        print(f"✅ El Dr. {self.nombre} ha registrado un tratamiento para {paciente.nombre}.")

    def __str__(self):
        return f"Dr. {self.nombre} - {self.especialidad} ({self.departamento.nombre})"


class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def __str__(self):
        return f"Departamento de {self.nombre}"


# --- Ejemplo de uso ---
dep_cardiologia = Departamento("Cardiología")
dep_pediatria = Departamento("Pediatría")

dr_juan = Doctor("Juan Pérez", "Cardiólogo", dep_cardiologia)
dr_maria = Doctor("María Gómez", "Pediatra", dep_pediatria)

dep_cardiologia.agregar_doctor(dr_juan)
dep_pediatria.agregar_doctor(dr_maria)

p1 = Paciente("Ana López", 45)
p2 = Paciente("Carlos Ruiz", 12)

t1 = Tratamiento("Tratamiento para hipertensión", 30, ["Enalapril", "Aspirina"])
t2 = Tratamiento("Tratamiento para asma infantil", 15, ["Salbutamol"])

dr_juan.atender_paciente(p1, t1)
dr_maria.atender_paciente(p2, t2)

p1.mostrar_historial()
p2.mostrar_historial()
