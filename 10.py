class contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"
class agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto)
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None
mi_agenda = agenda()
mi_agenda.agregar_contacto(contacto("Juan Perez", "123456789", "juan.perez@example.com"))
mi_agenda.agregar_contacto(contacto("Ana Gomez", "987654321", "lsadguas@gmail.com"))
mi_agenda.mostrar_contactos()
resultado_busqueda = mi_agenda.buscar_contacto("Ana Gomez")
if resultado_busqueda:
    print("Contacto encontrado:")
    print(resultado_busqueda) 