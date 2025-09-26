from datetime import datetime
from collections import Counter

class Contenido:
    def __init__(self, titulo, categoria, duracion):
        self.titulo = titulo
        self.categoria = categoria
        self.duracion = duracion  # minutos
        self.reproducciones = 0

    def reproducir(self):
        self.reproducciones += 1
        return f"▶ Reproduciendo: {self.titulo}"

    def __str__(self):
        return f"{self.titulo} ({self.categoria}, {self.duracion} min, {self.reproducciones} reproducciones)"


class Playlist:
    def __init__(self, nombre, creador):
        self.nombre = nombre
        self.creador = creador
        self.contenidos = []

    def agregar_contenido(self, contenido):
        if contenido not in self.contenidos:
            self.contenidos.append(contenido)

    def mostrar(self):
        print(f"\n🎵 Playlist: {self.nombre} (creada por {self.creador.nombre})")
        for c in self.contenidos:
            print(" -", c)

    def __str__(self):
        return f"Playlist: {self.nombre} ({len(self.contenidos)} contenidos)"


class Suscripcion:
    def __init__(self, tipo, precio):
        self.tipo = tipo  # básico, premium
        self.precio = precio
        self.fecha_inicio = datetime.now()

    def __str__(self):
        return f"Suscripción {self.tipo.capitalize()} (${self.precio}/mes, desde {self.fecha_inicio.date()})"


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.suscripcion = None
        self.historial = []
        self.playlists = []

    def suscribirse(self, tipo, precio):
        self.suscripcion = Suscripcion(tipo, precio)

    def ver_contenido(self, contenido):
        print(contenido.reproducir())
        self.historial.append(contenido)

    def crear_playlist(self, nombre):
        playlist = Playlist(nombre, self)
        self.playlists.append(playlist)
        return playlist

    def estadisticas(self):
        total_vistos = len(self.historial)
        total_minutos = sum(c.duracion for c in self.historial)
        categorias = Counter(c.categoria for c in self.historial)
        top_categoria = categorias.most_common(1)[0][0] if categorias else "N/A"

        print(f"\n📊 Estadísticas de {self.nombre}:")
        print(f" - Contenidos vistos: {total_vistos}")
        print(f" - Tiempo total: {total_minutos} minutos")
        print(f" - Categoría favorita: {top_categoria}")

    def recomendar(self, biblioteca):
        if not self.historial:
            return "Sin historial, no se pueden generar recomendaciones."
        categorias = Counter(c.categoria for c in self.historial)
        favorita = categorias.most_common(1)[0][0]
        recomendados = [c for c in biblioteca if c.categoria == favorita and c not in self.historial]
        return recomendados if recomendados else f"No hay nuevos contenidos en {favorita}"

    def __str__(self):
        return f"Usuario: {self.nombre}, {self.suscripcion}"


# --- Ejemplo de uso ---
# Biblioteca de contenidos
c1 = Contenido("Python desde cero", "Educación", 60)
c2 = Contenido("Historia del Arte", "Cultura", 45)
c3 = Contenido("Machine Learning avanzado", "Educación", 90)
c4 = Contenido("Rock Clásico", "Música", 50)
c5 = Contenido("Jazz Contemporáneo", "Música", 40)

biblioteca = [c1, c2, c3, c4, c5]

# Usuario
u1 = Usuario("Ana")
u1.suscribirse("premium", 29.99)

# Consumo de contenidos
u1.ver_contenido(c1)
u1.ver_contenido(c3)
u1.ver_contenido(c4)

# Playlists
pl = u1.crear_playlist("Favoritos de Ana")
pl.agregar_contenido(c1)
pl.agregar_contenido(c4)
pl.mostrar()

# Estadísticas y recomendaciones
u1.estadisticas()
print("\n🤖 Recomendaciones:", u1.recomendar(biblioteca))
