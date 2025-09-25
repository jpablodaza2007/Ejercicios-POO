class libro:
    def __init__(self, titulo, autor, ISBN, estado):
        self.titulo=titulo
        self.autor=autor
        self.ISBN=ISBN
        self.estado=estado
        self.libros:[]
    def agregar_libro(self, titulo):
        self.libros.append(titulo)

    def Buscar_libro(self, titulo):
        if titulo in self.libros:
            return True
        else:
            return False
        
l1 = libro("monica y los reyes","Jose",1234567891023,"disponible")
print(l1.autor,l1.estado)

        