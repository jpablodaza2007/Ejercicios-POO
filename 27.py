class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.seguidos = []
        self.publicaciones = []

    def seguir(self, otro_usuario):
        if otro_usuario not in self.seguidos and otro_usuario != self:
            self.seguidos.append(otro_usuario)
            print(f"{self.nombre} ahora sigue a {otro_usuario.nombre}")

    def crear_publicacion(self, contenido):
        pub = Publicacion(contenido, self)
        self.publicaciones.append(pub)
        return pub

    def __str__(self):
        return self.nombre


class Publicacion:
    def __init__(self, contenido, autor):
        self.contenido = contenido
        self.autor = autor
        self.likes = []
        self.comentarios = []

    def dar_like(self, usuario):
        if usuario not in self.likes:
            self.likes.append(usuario)

    def agregar_comentario(self, usuario, texto):
        comentario = Comentario(usuario, texto)
        self.comentarios.append(comentario)

    def mostrar(self):
        print(f"\n{self.autor} publicó: {self.contenido}")
        print(f"👍 Likes: {len(self.likes)} | 💬 Comentarios: {len(self.comentarios)}")
        for c in self.comentarios:
            print(f"   - {c}")


class Comentario:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto

    def __str__(self):
        return f"{self.autor}: {self.texto}"


# Ejemplo de uso
u1 = Usuario("Ana")
u2 = Usuario("Luis")
u3 = Usuario("Carla")

u1.seguir(u2)
u2.seguir(u3)

pub1 = u1.crear_publicacion("Hola, esta es mi primera publicación 🚀")
pub2 = u2.crear_publicacion("Hoy aprendí Python 🐍")

pub1.dar_like(u2)
pub1.dar_like(u3)

pub2.dar_like(u1)
pub2.agregar_comentario(u3, "¡Genial! Yo también estoy aprendiendo.")
pub2.agregar_comentario(u1, "¿En qué nivel vas?")

pub1.mostrar()
pub2.mostrar()
