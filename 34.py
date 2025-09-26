from datetime import datetime

class Estudiante:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento
        self.clases = []
        self.progreso = {}

    def inscribirse(self, clase):
        self.clases.append(clase)
        clase.estudiantes.append(self)
        self.progreso[clase] = []
        print(f"{self.nombre} se inscribió en {clase.instrumento} con {clase.profesor.nombre}.")

    def registrar_progreso(self, clase, nota, comentario=""):
        if clase in self.progreso:
            registro = {
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "nota": nota,
                "comentario": comentario
            }
            self.progreso[clase].append(registro)

    def mostrar_progreso(self):
        print(f"\n📘 Progreso académico de {self.nombre}:")
        for clase, registros in self.progreso.items():
            print(f" - Clase de {clase.instrumento} con {clase.profesor.nombre}:")
            for r in registros:
                print(f"   [{r['fecha']}] Nota: {r['nota']} | {r['comentario']}")

    def __str__(self):
        return f"{self.nombre} ({self.instrumento})"


class Profesor:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento
        self.clases = []

    def crear_clase(self, horario):
        clase = Clase(self, self.instrumento, horario)
        self.clases.append(clase)
        return clase

    def __str__(self):
        return f"Profesor {self.nombre} ({self.instrumento})"


class Clase:
    def __init__(self, profesor, instrumento, horario):
        self.profesor = profesor
        self.instrumento = instrumento
        self.horario = horario
        self.estudiantes = []

    def mostrar_estudiantes(self):
        print(f"\n👩‍🎓 Estudiantes en clase de {self.instrumento}:")
        for est in self.estudiantes:
            print(f" - {est.nombre}")

    def __str__(self):
        return f"Clase de {self.instrumento} con {self.profesor.nombre} ({self.horario})"


# --- Ejemplo de uso ---
prof1 = Profesor("Carlos Pérez", "Guitarra")
clase_guitarra = prof1.crear_clase("Lunes 10:00 - 11:00")

est1 = Estudiante("María López", "Guitarra")
est2 = Estudiante("Juan Torres", "Guitarra")

# Inscripción
est1.inscribirse(clase_guitarra)
est2.inscribirse(clase_guitarra)

# Registrar progreso
est1.registrar_progreso(clase_guitarra, 9.0, "Buen dominio de acordes básicos")
est1.registrar_progreso(clase_guitarra, 9.5, "Mejora en arpegios")

# Mostrar información
clase_guitarra.mostrar_estudiantes()
est1.mostrar_progreso()
