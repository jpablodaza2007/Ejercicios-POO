class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def __str__(self):
        return f"{self.nombre} ({self.creditos} créditos)"


class Calificacion:
    def __init__(self, materia, nota):
        self.materia = materia
        self.nota = nota  # valor numérico de 0 a 5, por ejemplo

    def __str__(self):
        return f"{self.materia.nombre}: {self.nota}"


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, materia, nota):
        self.calificaciones.append(Calificacion(materia, nota))

    def promedio_ponderado(self):
        total_creditos = sum(c.materia.creditos for c in self.calificaciones)
        if total_creditos == 0:
            return 0
        suma_ponderada = sum(c.nota * c.materia.creditos for c in self.calificaciones)
        return suma_ponderada / total_creditos

    def mostrar_calificaciones(self):
        print(f"Calificaciones de {self.nombre}:")
        for c in self.calificaciones:
            print(f" - {c}")
        print(f"Promedio ponderado: {self.promedio_ponderado():.2f}")


# Ejemplo de uso
mat1 = Materia("Matemáticas", 4)
mat2 = Materia("Historia", 2)
mat3 = Materia("Programación", 3)

est = Estudiante("Juan")
est.agregar_calificacion(mat1, 4.5)
est.agregar_calificacion(mat2, 3.8)
est.agregar_calificacion(mat3, 5.0)

est.mostrar_calificaciones()
