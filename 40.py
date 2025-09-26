from datetime import datetime

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
        self.grupos = []
        self.eventos = []
        self.notificaciones = []
        self.privacidad = "publico"  # publico, amigos, privado

    def agregar_amigo(self, usuario):
        if usuario not in self.amigos:
            self.amigos.append(usuario)
            usuario.amigos.append(self)

    def enviar_mensaje(self, receptor, contenido):
        if self.puede_interactuar_con(receptor):
            mensaje = Mensaje(self, receptor, contenido)
            receptor.recibir_mensaje(mensaje)
            return mensaje
        else:
            print(f"{self.nombre} no puede enviar mensaje a {receptor.nombre} por privacidad.")

    def recibir_mensaje(self, mensaje):
        noti = Notificacion(f"Nuevo mensaje de {mensaje.emisor.nombre}: {mensaje.contenido}")
        self.notificaciones.append(noti)

    def crear_grupo(self, nombre, privacidad="publico"):
        grupo = Grupo(nombre, self, privacidad)
        self.grupos.append(grupo)
        return grupo

    def unirse_a_grupo(self, grupo):
        if grupo.puede_unirse(self):
            grupo.miembros.append(self)
            self.grupos.append(grupo)
        else:
            print(f"{self.nombre} no puede unirse al grupo {grupo.nombre} por privacidad.")

    def crear_evento(self, nombre, fecha, privacidad="publico"):
        evento = Evento(nombre, fecha, self, privacidad)
        self.eventos.append(evento)
        return evento

    def unirse_a_evento(self, evento):
        if evento.puede_unirse(self):
            evento.participantes.append(self)
            self.eventos.append(evento)
        else:
            print(f"{self.nombre} no puede unirse al evento {evento.nombre} por privacidad.")

    def puede_interactuar_con(self, usuario):
        if usuario.privacidad == "publico":
            return True
        elif usuario.privacidad == "amigos":
            return self in usuario.amigos
        elif usuario.privacidad == "privado":
            return self == usuario
        return False

    def ver_notificaciones(self):
        print(f"\n🔔 Notificaciones de {self.nombre}:")
        for n in self.notificaciones:
            print("-", n)

    def __str__(self):
        return f"Usuario: {self.nombre} ({self.privacidad})"


class Grupo:
    def __init__(self, nombre, creador, privacidad="publico"):
        self.nombre = nombre
        self.creador = creador
        self.privacidad = privacidad
        self.miembros = [creador]

    def puede_unirse(self, usuario):
        if self.privacidad == "publico":
            return True
        elif self.privacidad == "amigos":
            return usuario in self.creador.amigos
        elif self.privacidad == "privado":
            return usuario == self.creador
        return False

    def __str__(self):
        return f"Grupo: {self.nombre} ({self.privacidad}, {len(self.miembros)} miembros)"


class Evento:
    def __init__(self, nombre, fecha, creador, privacidad="publico"):
        self.nombre = nombre
        self.fecha = fecha
        self.creador = creador
        self.privacidad = privacidad
        self.participantes = [creador]

    def puede_unirse(self, usuario):
        if self.privacidad == "publico":
            return True
        elif self.privacidad == "amigos":
            return usuario in self.creador.amigos
        elif self.privacidad == "privado":
            return usuario == self.creador
        return False

    def __str__(self):
        return f"Evento: {self.nombre} en {self.fecha} ({self.privacidad})"


class Mensaje:
    def __init__(self, emisor, receptor, contenido):
        self.emisor = emisor
        self.receptor = receptor
        self.contenido = contenido
        self.fecha = datetime.now()

    def __str__(self):
        return f"[{self.fecha.strftime('%Y-%m-%d %H:%M')}] {self.emisor.nombre} → {self.receptor.nombre}: {self.contenido}"


class Notificacion:
    def __init__(self, contenido):
        self.contenido = contenido
        self.fecha = datetime.now()

    def __str__(self):
        return f"{self.fecha.strftime('%Y-%m-%d %H:%M')} - {self.contenido}"


# --- Ejemplo de uso ---
u1 = Usuario("Ana")
u2 = Usuario("Luis")
u3 = Usuario("Marta")

# Privacidad
u2.privacidad = "amigos"
u3.privacidad = "privado"

# Amistades
u1.agregar_amigo(u2)

# Mensajes con restricciones de privacidad
u1.enviar_mensaje(u2, "Hola Luis!")
u1.enviar_mensaje(u3, "Hola Marta!")  # No debería poder

# Crear grupos y eventos
g1 = u1.crear_grupo("Programadores", "publico")
g2 = u2.crear_grupo("Diseñadores", "amigos")

u2.unirse_a_grupo(g1)
u3.unirse_a_grupo(g2)  # No debería poder

e1 = u1.crear_evento("Hackathon", "2025-11-01", "publico")
u2.unirse_a_evento(e1)

# Notificaciones
u2.ver_notificaciones()
u3.ver_notificaciones()

# Mostrar info
print("\n", g1)
print(g2)
print(e1)
