from datetime import datetime, timedelta

class Empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def __str__(self):
        return f"{self.nombre} ({self.puesto})"


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregar_empleado(self, empleado):
        self.miembros.append(empleado)

    def mostrar_equipo(self):
        print(f"\n👥 Equipo {self.nombre}:")
        for e in self.miembros:
            print(f"- {e}")

    def __str__(self):
        return f"Equipo {self.nombre} ({len(self.miembros)} miembros)"


class Tarea:
    def __init__(self, nombre, duracion_dias):
        self.nombre = nombre
        self.duracion = timedelta(days=duracion_dias)
        self.fecha_inicio = None
        self.fecha_fin = None
        self.dependencias = []
        self.responsable = None

    def agregar_dependencia(self, tarea):
        self.dependencias.append(tarea)

    def asignar_responsable(self, empleado):
        self.responsable = empleado

    def programar(self, fecha_inicio):
        if self.dependencias:
            max_fecha = max([t.fecha_fin for t in self.dependencias if t.fecha_fin])
            fecha_inicio = max(fecha_inicio, max_fecha)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_inicio + self.duracion

    def __str__(self):
        responsable = self.responsable.nombre if self.responsable else "Sin asignar"
        inicio = self.fecha_inicio.strftime("%Y-%m-%d") if self.fecha_inicio else "N/A"
        fin = self.fecha_fin.strftime("%Y-%m-%d") if self.fecha_fin else "N/A"
        return f"Tarea: {self.nombre} | Resp: {responsable} | {inicio} → {fin}"


class Proyecto:
    def __init__(self, nombre, fecha_inicio):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def programar_tareas(self):
        for tarea in self.tareas:
            if not tarea.fecha_inicio:  # solo programar si no tiene fecha
                tarea.programar(self.fecha_inicio)

    def mostrar_cronograma(self):
        print(f"\n📅 Cronograma del proyecto: {self.nombre}")
        for t in sorted(self.tareas, key=lambda x: x.fecha_inicio or self.fecha_inicio):
            print(t)

    def __str__(self):
        return f"Proyecto: {self.nombre} ({len(self.tareas)} tareas)"


# --- Ejemplo de uso ---
# Empleados y equipo
e1 = Empleado("Ana", "Desarrolladora")
e2 = Empleado("Luis", "Diseñador")
equipo = Equipo("Alpha")
equipo.agregar_empleado(e1)
equipo.agregar_empleado(e2)
equipo.mostrar_equipo()

# Proyecto y tareas
inicio_proyecto = datetime(2025, 10, 1)
proyecto = Proyecto("Sistema Web", inicio_proyecto)

t1 = Tarea("Diseño UI", 5)
t2 = Tarea("Base de Datos", 4)
t3 = Tarea("Backend", 7)
t4 = Tarea("Frontend", 6)

# Dependencias
t3.agregar_dependencia(t2)   # Backend depende de BD
t4.agregar_dependencia(t1)   # Frontend depende de Diseño UI
t4.agregar_dependencia(t3)   # y de Backend

# Responsables
t1.asignar_responsable(e2)
t2.asignar_responsable(e1)
t3.asignar_responsable(e1)
t4.asignar_responsable(e2)

# Agregar tareas al proyecto
for tarea in [t1, t2, t3, t4]:
    proyecto.agregar_tarea(tarea)

# Programar y mostrar cronograma
proyecto.programar_tareas()
proyecto.mostrar_cronograma()
