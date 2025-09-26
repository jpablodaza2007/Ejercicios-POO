from datetime import datetime

class Propuesta:
    def __init__(self, freelancer, proyecto, monto, plazo_dias):
        self.freelancer = freelancer
        self.proyecto = proyecto
        self.monto = monto
        self.plazo_dias = plazo_dias
        self.fecha = datetime.now()
        self.aceptada = False

    def aceptar(self):
        self.aceptada = True
        self.proyecto.asignar_freelancer(self.freelancer, self)
        print(f"✅ Propuesta de {self.freelancer.nombre} aceptada para el proyecto '{self.proyecto.titulo}'.")

    def __str__(self):
        estado = "Aceptada" if self.aceptada else "Pendiente"
        return f"Propuesta de {self.freelancer.nombre}: ${self.monto}, {self.plazo_dias} días [{estado}]"


class Proyecto:
    def __init__(self, titulo, descripcion, cliente):
        self.titulo = titulo
        self.descripcion = descripcion
        self.cliente = cliente
        self.freelancer_asignado = None
        self.propuestas = []
        self.finalizado = False
        self.calificacion = None

    def recibir_propuesta(self, propuesta):
        self.propuestas.append(propuesta)

    def asignar_freelancer(self, freelancer, propuesta):
        if not self.freelancer_asignado:
            self.freelancer_asignado = freelancer
            freelancer.proyectos.append(self)
            self.cliente.proyectos.append(self)
            propuesta.aceptada = True
        else:
            print("❌ Ya hay un freelancer asignado.")

    def finalizar(self, calificacion):
        if self.freelancer_asignado:
            self.finalizado = True
            self.calificacion = calificacion
            self.freelancer_asignado.recibir_calificacion(calificacion)
            print(f"📌 Proyecto '{self.titulo}' finalizado con calificación {calificacion}/5.")
        else:
            print("❌ No se puede finalizar, no hay freelancer asignado.")

    def __str__(self):
        estado = "Finalizado" if self.finalizado else "En curso"
        return f"Proyecto: {self.titulo} ({estado}) - Cliente: {self.cliente.nombre}"


class Freelancer:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.proyectos = []
        self.calificaciones = []

    def enviar_propuesta(self, proyecto, monto, plazo_dias):
        propuesta = Propuesta(self, proyecto, monto, plazo_dias)
        proyecto.recibir_propuesta(propuesta)
        print(f"📨 {self.nombre} envió una propuesta para '{proyecto.titulo}'.")
        return propuesta

    def recibir_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def rating_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad} | Rating: {self.rating_promedio():.1f}/5"


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.proyectos = []

    def crear_proyecto(self, titulo, descripcion):
        proyecto = Proyecto(titulo, descripcion, self)
        print(f"📝 Proyecto '{titulo}' creado por {self.nombre}.")
        return proyecto

    def __str__(self):
        return f"Cliente: {self.nombre}, Proyectos: {len(self.proyectos)}"
    

# --- Ejemplo de uso ---
cliente1 = Cliente("Empresa Tech")
freelancer1 = Freelancer("Ana Torres", "Desarrollo Web")
freelancer2 = Freelancer("Luis Gómez", "Diseño Gráfico")

# Cliente crea proyecto
p1 = cliente1.crear_proyecto("Página Web", "Desarrollo de un e-commerce")

# Freelancers envían propuestas
pr1 = freelancer1.enviar_propuesta(p1, 1200, 20)
pr2 = freelancer2.enviar_propuesta(p1, 900, 25)

# Cliente acepta una propuesta
pr1.aceptar()

# Finalizar proyecto con calificación
p1.finalizar(5)

print("\n--- Estado final ---")
print(freelancer1)
print(freelancer2)
print(p1)
