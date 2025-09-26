import random

class Planta:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia
    def crecer(self):
        self.energia += random.randint(5, 15)
    def ser_consumida(self, cantidad):
        energia_tomada = min(self.energia, cantidad)
        self.energia -= energia_tomada
        return energia_tomada

class Animal:
    def __init__(self, nombre, dieta, energia=50):
        self.nombre = nombre
        self.dieta = dieta
        self.energia = energia
        self.vivo = True
    def comer(self, recurso):
        if not self.vivo: return
        if isinstance(recurso, Planta) and self.dieta in ["herbívoro","omnívoro"]:
            self.energia += recurso.ser_consumida(20)
        elif isinstance(recurso, Animal) and recurso.vivo and self.dieta in ["carnívoro","omnívoro"]:
            recurso.vivo = False
            self.energia += recurso.energia
    def gastar_energia(self):
        if not self.vivo: return
        self.energia -= random.randint(5, 15)
        if self.energia <= 0: self.vivo = False

class Ambiente:
    def __init__(self):
        self.animales, self.plantas = [], []
    def ciclo(self):
        for p in self.plantas: p.crecer()
        for a in self.animales:
            a.gastar_energia()
            if a.dieta in ["herbívoro","omnívoro"] and self.plantas:
                a.comer(random.choice(self.plantas))
            elif a.dieta in ["carnívoro","omnívoro"] and self.animales:
                presa = random.choice(self.animales)
                if presa != a: a.comer(presa)

class CadenaAlimenticia:
    def __init__(self, ambiente): self.ambiente = ambiente
    def simular(self, ciclos):
        for _ in range(ciclos): self.ambiente.ciclo()

# Ejemplo
a = Ambiente()
a.plantas = [Planta("Pasto", 50)]
a.animales = [Animal("Conejo","herbívoro"), Animal("León","carnívoro")]
CadenaAlimenticia(a).simular(5)
