class lista_tareas:
    def __init__(self):
        self.items = ["barrer", "limpiar", "cocinar"]

    def agregar(self, item):
        self.items.append(item)

    def eliminar(self, item):
        if item in self.items:
            self.items.remove(item)

    def mostrar(self):
        return self.items
tareas = lista_tareas()
tareas.agregar("lavar ropa")
tareas.eliminar("limpiar")
print("Tareas actuales:", tareas.mostrar())