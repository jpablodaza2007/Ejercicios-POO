class ContadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def contar_palabras(self):
        palabras = self.texto.split()
        return len(palabras)

    def contar_caracteres(self):
        return len(self.texto)

    def contar_lineas(self):
        lineas = self.texto.splitlines()
        return len(lineas)



texto = "Hola mundo\nEsto es un ejemplo\npara la clase ContadorTexto"

contador = ContadorTexto(texto)

print("Palabras:", contador.contar_palabras())
print("Caracteres:", contador.contar_caracteres())
print("Líneas:", contador.contar_lineas())
