class mascota:
    def __init__(self, nombre, tipo, edad, metodo_presentarse):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.metodo_presentarse = metodo_presentarse

perro = mascota("Firulais", "perro", "5 años", "La pata")
gato = mascota("Michi", "gato", "3 años", "El salto")
pajaro = mascota("Piolin", "pájaro", "2 años", "El vuelo")

print(perro.nombre, perro.tipo, perro.edad, perro.metodo_presentarse)
print(gato.nombre, gato.tipo, gato.edad, gato.metodo_presentarse)
print(pajaro.nombre, pajaro.tipo, pajaro.edad, pajaro.metodo_presentarse)