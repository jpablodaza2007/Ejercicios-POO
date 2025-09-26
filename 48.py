import random

class Planta:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia

    def crecer(self):
        ganancia = random.randint(5, 15)
        self.energia += ganancia
        print(f"🌱 {self.nombre} creció y ganó {ganancia} de energía (Total: {self.energia}).")

    def ser_consumida(self, cantidad):
        energia_tomada = min(self.energia, cantidad)
        self.energia -= energia_tomada
        return energia_tomada

    def __str__(self):
        return f"Planta {self.nombre} | Energía: {self.energia}"


class Animal:
    def __init__(self, nombre, especie, dieta, energia=50):
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta  # "herbívoro", "carnívoro", "omnívoro"
        self.energia = energia
        self.vivo = True

    def comer(self, recurso):
        if not self.vivo:
            return
        if isinstance(recurso, Planta) and self.dieta in ["herbívoro", "omnívoro"]:
            energia_ganada = recurso.ser_consumida(20)
            self.energia += energia_ganada
            print(f"🐰 {self.nombre} comió {recurso.nombre} y ganó {energia_ganada} energía.")
        elif isinstance(recurso, Animal) and self.dieta in ["carnívoro", "omnívoro"]:
            if recurso.vivo:
                recurso.vivo = False
                self.energia += recurso.energia
                print(f"🦁 {self.nombre} cazó a {recurso.nombre} y ganó {recurso.energia} energía.")
        else:
            print(f"⚠️ {self.nombre} no puede comer eso.")

    def gastar_energia(self):
        if not self.vivo:
            return
        gasto = random.randint(5, 15)
        self.energia -= gasto
        if self.energia <= 0:
            self.vivo = False
            print(f"💀 {self.nombre} ha muerto por falta de energía.")
        else:
            print(f"⚡ {self.nombre} gastó {gasto} energía (Restante: {self.energia}).")

    def __str__(self):
        estado = "Vivo" if self.vivo else "Muerto"
        return f"Animal {self.nombre} ({self.especie}, {self.dieta}) | Energía: {self.energia} [{estado}]"


class Ambiente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []
        self.plantas = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def agregar_planta(self, planta):
        self.plantas.append(planta)

    def ciclo(self):
        print(f"\n🌍 Ciclo en el ambiente {self.nombre}:")
        # Plantas crecen
        for p in self.plantas:
            p.crecer()

        # Animales gastan energía y buscan alimento
        for a in self.animales:
            if a.vivo:
                a.gastar_energia()
                if a.dieta in ["herbívoro", "omnívoro"] and self.plantas:
                    a.comer(random.choice(self.plantas))
                elif a.dieta in ["carnívoro", "omnívoro"] and self.animales:
                    posible_presa = random.choice(self.animales)
                    if posible_presa != a and posible_presa.vivo:
                        a.comer(posible_presa)

    def __str__(self):
        texto = f"\n=== Ambiente: {self.nombre} ===\n"
        texto += "\nAnimales:\n"
        for a in self.animales:
            texto += f" - {a}\n"
        texto += "\nPlantas:\n"
        for p in self.plantas:
            texto += f" - {p}\n"
        return texto


class CadenaAlimenticia:
    def __init__(self, ambiente):
        self.ambiente = ambiente

    def simular(self, ciclos):
        for i in range(ciclos):
            print(f"\n🔄 --- Ciclo {i+1} ---")
            self.ambiente.ciclo()
        print("\n📊 Estado final del ecosistema:")
        print(self.ambiente)


# --- Ejemplo de uso ---
ambiente = Ambiente("Sabana Africana")

# Plantas
pasto = Planta("Pasto", 50)
arbol = Planta("Árbol", 100)
ambiente.agregar_planta(pasto)
ambiente.agregar_planta(arbol)

# Animales
conejo = Animal("Conejo", "Mamífero", "herbívoro")
leon = Animal("León", "Felino", "carnívoro")
oso = Animal("Oso", "Mamífero", "omnívoro")
ambiente.agregar_animal(conejo)
ambiente.agregar_animal(leon)
ambiente.agregar_animal(oso)

# Simulación
ecosistema = CadenaAlimenticia(ambiente)
ecosistema.simular(5)
