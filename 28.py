from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

    def tomar_prestado(self, libro, dias=7):
        if libro.disponible:
            prestamo = Prestamo(self, libro, dias)
            self.prestamos.append(prestamo)
            libro.disponible = False
            print(f"{self.nombre} tomó prestado '{libro.titulo}' por {dias} días.")
            return prestamo
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")

    def devolver_libro(self, prestamo):
        multa = prestamo.calcular_multa()
        prestamo.libro.disponible = True
        self.prestamos.remove(prestamo)
        print(f"{self.nombre} devolvió '{prestamo.libro.titulo}'. Multa: ${multa:.2f}")

    def __str__(self):
        return self.nombre


class Prestamo:
    def __init__(self, usuario, libro, dias):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_vencimiento = self.fecha_prestamo + timedelta(days=dias)
        self.devuelto = False

    def calcular_multa(self):
        if self.devuelto:
            return 0
        hoy = datetime.now()
        if hoy > self.fecha_vencimiento:
            dias_retraso = (hoy - self.fecha_vencimiento).days
            return dias_retraso * 1.5  # multa de 1.5 por día de retraso
        return 0

    def __str__(self):
        return f"{self.libro.titulo} prestado a {self.usuario} hasta {self.fecha_vencimiento.date()}"
    

# Ejemplo de uso
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("El Quijote", "Miguel de Cervantes")

usuario1 = Usuario("Juan")

prestamo1 = usuario1.tomar_prestado(libro1, dias=5)
prestamo2 = usuario1.tomar_prestado(libro2, dias=3)

print("\n--- Estado de préstamos ---")
for p in usuario1.prestamos:
    print(p)

# Simular devolución (puedes modificar la fecha de vencimiento para probar multas)
usuario1.devolver_libro(prestamo1)
