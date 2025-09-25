class estudiante:
    def __init__(self, nombre, edad,):
        self.nombre = nombre
        self.edad = edad
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def obtener_promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
estudiante1 = estudiante("Ana", 20)
estudiante1.agregar_nota(85)
estudiante1.agregar_nota(90)
estudiante1.agregar_nota(78)
print(f"{estudiante1.nombre}, Edad: {estudiante1.edad}, Promedio de notas: {estudiante1.obtener_promedio()}")
