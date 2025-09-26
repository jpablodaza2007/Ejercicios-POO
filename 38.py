from datetime import datetime

class Leccion:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def __str__(self):
        return f"Lección: {self.titulo}"


class Modulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lecciones = []

    def agregar_leccion(self, leccion):
        self.lecciones.append(leccion)

    def __str__(self):
        return f"Módulo: {self.nombre} ({len(self.lecciones)} lecciones)"


class Curso:
    def __init__(self, titulo, certificado_min=0.7):
        self.titulo = titulo
        self.modulos = []
        self.estudiantes = []
        self.certificado_min = certificado_min  # % requerido para certificar

    def agregar_modulo(self, modulo):
        self.modulos.append(modulo)

    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.inscribir(self)

    def total_lecciones(self):
        return sum(len(m.lecciones) for m in self.modulos)

    def __str__(self):
        return f"Curso: {self.titulo} ({len(self.modulos)} módulos, {self.total_lecciones()} lecciones)"


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = {}
        self.certificados = []

    def inscribir(self, curso):
        self.cursos[curso] = {"completadas": 0, "fecha_inicio": datetime.now()}

    def completar_leccion(self, curso):
        if curso in self.cursos:
            self.cursos[curso]["completadas"] += 1
            print(f"✅ {self.nombre} completó una lección en {curso.titulo}.")
        else:
            print(f"⚠️ {self.nombre} no está inscrito en {curso.titulo}.")

    def progreso(self, curso):
        if curso not in self.cursos:
            return 0
        total = curso.total_lecciones()
        completadas = self.cursos[curso]["completadas"]
        return completadas / total if total > 0 else 0

    def verificar_certificacion(self, curso):
        progreso = self.progreso(curso)
        if progreso >= curso.certificado_min and curso not in self.certificados:
            self.certificados.append(curso)
            print(f"🏆 {self.nombre} obtuvo certificación en {curso.titulo} ({progreso*100:.1f}%).")
        elif curso in self.certificados:
            print(f"📜 {self.nombre} ya está certificado en {curso.titulo}.")
        else:
            print(f"📌 {self.nombre} tiene {progreso*100:.1f}% de progreso en {curso.titulo}.")

    def __str__(self):
        return f"{self.nombre} ({len(self.certificados)} certificados)"


# --- Ejemplo de uso ---
curso_python = Curso("Python Básico")

# Módulos y lecciones
mod1 = Modulo("Introducción")
mod1.agregar_leccion(Leccion("Historia de Python", "Contenido..."))
mod1.agregar_leccion(Leccion("Instalación", "Contenido..."))

mod2 = Modulo("Fundamentos")
mod2.agregar_leccion(Leccion("Variables", "Contenido..."))
mod2.agregar_leccion(Leccion("Condicionales", "Contenido..."))
mod2.agregar_leccion(Leccion("Bucles", "Contenido..."))

curso_python.agregar_modulo(mod1)
curso_python.agregar_modulo(mod2)

print(curso_python)

# Estudiante
est1 = Estudiante("Laura")
curso_python.inscribir_estudiante(est1)

# Progreso
est1.completar_leccion(curso_python)
est1.completar_leccion(curso_python)
est1.completar_leccion(curso_python)

print(f"\nProgreso de {est1.nombre}: {est1.progreso(curso_python)*100:.1f}%")

# Verificar certificación
est1.verificar_certificacion(curso_python)
