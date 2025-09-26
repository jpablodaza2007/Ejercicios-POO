import random

class Habilidad:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder  # daño base

    def usar(self, atacante, objetivo):
        dano = self.poder + atacante.nivel
        objetivo.recibir_dano(dano)
        print(f"{atacante.nombre} usa {self.nombre} contra {objetivo.nombre} causando {dano} de daño.")


class Item:
    def __init__(self, nombre, efecto):
        self.nombre = nombre
        self.efecto = efecto  # función que aplica el efecto

    def usar(self, personaje):
        self.efecto(personaje)
        print(f"{personaje.nombre} usó {self.nombre}.")


class Personaje:
    def __init__(self, nombre, vida=100):
        self.nombre = nombre
        self.vida = vida
        self.nivel = 1
        self.exp = 0
        self.habilidades = []
        self.items = []

    def aprender_habilidad(self, habilidad):
        self.habilidades.append(habilidad)

    def agregar_item(self, item):
        self.items.append(item)

    def atacar(self, objetivo):
        dano = random.randint(5, 15)
        objetivo.recibir_dano(dano)
        print(f"{self.nombre} ataca a {objetivo.nombre} causando {dano} de daño.")

    def recibir_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha sido derrotado.")

    def ganar_exp(self, cantidad):
        self.exp += cantidad
        print(f"{self.nombre} gana {cantidad} EXP. (Total: {self.exp})")
        if self.exp >= self.nivel * 50:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 20
        self.exp = 0
        print(f"⚡ {self.nombre} subió al nivel {self.nivel}! Vida: {self.vida}")

    def __str__(self):
        return f"{self.nombre} | Vida: {self.vida} | Nivel: {self.nivel} | EXP: {self.exp}"


# --- Ejemplo de uso ---
# Crear personajes
p1 = Personaje("Guerrero")
p2 = Personaje("Mago", vida=80)

# Crear habilidades
espada = Habilidad("Golpe de espada", 12)
fuego = Habilidad("Bola de fuego", 15)

# Asignar habilidades
p1.aprender_habilidad(espada)
p2.aprender_habilidad(fuego)

# Crear ítem
pocion = Item("Poción de curación", lambda p: setattr(p, "vida", p.vida + 30))
p1.agregar_item(pocion)

# Combate
print("\n--- Combate ---")
p1.atacar(p2)
p2.habilidades[0].usar(p2, p1)
p1.items[0].usar(p1)  # usa la poción
p1.ganar_exp(60)      # gana experiencia y sube nivel

print("\n--- Estado final ---")
print(p1)
print(p2)
