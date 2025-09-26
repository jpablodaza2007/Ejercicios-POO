class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn}) - {estado}"

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0")

print(libro1)          
libro1.prestar()       
print(libro1)          
libro1.prestar()       
libro1.devolver()      
print(libro1)          
