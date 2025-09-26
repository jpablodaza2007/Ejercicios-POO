import random, math
from collections import defaultdict

class Objeto:
    def __init__(self, nombre, valor_base=10):
        self.nombre = nombre
        self.valor_base = valor_base
        self.en_mundo = True

class Avatar:
    def __init__(self, nombre, dinero=100):
        self.nombre = nombre
        self.dinero = dinero
        self.inventario = []
    def pickup(self, obj, mundo):
        if obj in mundo.objetos:
            mundo.objetos.remove(obj)
            self.inventario.append(obj)
    def comprar(self, nombre, mundo):
        if mundo.mercado.get(nombre,0)>0 and self.dinero>=10:
            self.inventario.append(Objeto(nombre))
            mundo.mercado[nombre]-=1
            self.dinero-=10

class Mundo:
    def __init__(self):
        self.objetos = []
        self.mercado = defaultdict(int)
    def agregar_objeto(self, obj):
        self.objetos.append(obj)
        self.mercado[obj.nombre]+=1

# Ejemplo
m = Mundo()
a1 = Avatar("Ana")
a2 = Avatar("Pedro")
manzana = Objeto("Manzana",5)
m.agregar_objeto(manzana)
a1.pickup(manzana,m)
a2.comprar("Manzana",m)
