from abc import ABC, abstractmethod


class ElementoSistema(ABC):
    """Clase base abstracta para archivos y carpetas."""
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def mostrar(self, nivel=0):
        """Mostrar el contenido de forma jerárquica."""
        pass


class Archivo(ElementoSistema):
    """Representa un archivo simple con un tamaño en KB."""
    def __init__(self, nombre: str, tamanio: int):
        super().__init__(nombre)
        self.tamanio = tamanio

    def mostrar(self, nivel=0):
        print("    " * nivel + f"- Archivo: {self.nombre} ({self.tamanio} KB)")

    def __str__(self):
        return f"Archivo: {self.nombre}, {self.tamanio} KB"


class Carpeta(ElementoSistema):
    """Carpeta que puede contener archivos u otras carpetas."""
    def __init__(self, nombre: str):
        super().__init__(nombre)
        self.elementos = []

    def agregar(self, elemento: ElementoSistema):
        self.elementos.append(elemento)

    def mostrar(self, nivel=0):
        print("    " * nivel + f"+ Carpeta: {self.nombre}")
        for elem in self.elementos:
            elem.mostrar(nivel + 1)

    def __str__(self):
        return f"Carpeta: {self.nombre} ({len(self.elementos)} elementos)"
# Crear archivos
archivo1 = Archivo("documento.txt", 120)
archivo2 = Archivo("foto.jpg", 2048)
archivo3 = Archivo("video.mp4", 102400)

# Crear carpetas
carpeta1 = Carpeta("Mis Documentos")
carpeta2 = Carpeta("Multimedia")
carpeta3 = Carpeta("Fotos Vacaciones")

# Construir estructura
carpeta1.agregar(archivo1)
carpeta2.agregar(archivo2)
carpeta2.agregar(carpeta3)
carpeta3.agregar(archivo3)

# Carpeta raíz
raiz = Carpeta("Disco C")
raiz.agregar(carpeta1)
raiz.agregar(carpeta2)

# Mostrar estructura
raiz.mostrar()
