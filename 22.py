class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_permisos(self):
        raise NotImplementedError("Este método debe ser implementado en las subclases.")


class Administrador(Usuario):
    def mostrar_permisos(self):
        return f"{self.nombre} (Administrador): puede crear, modificar y eliminar usuarios."


class Cliente(Usuario):
    def mostrar_permisos(self):
        return f"{self.nombre} (Cliente): puede comprar productos y ver su historial."


class Moderador(Usuario):
    def mostrar_permisos(self):
        return f"{self.nombre} (Moderador): puede supervisar comentarios y bloquear usuarios."


# Ejemplo de uso
usuarios = [
    Administrador("Ana"),
    Cliente("Luis"),
    Moderador("Carlos")
]

for u in usuarios:
    print(u.mostrar_permisos())
