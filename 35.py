class Candidato:
    def __init__(self, nombre, partido):
        self.nombre = nombre
        self.partido = partido
        self.votos = 0

    def recibir_voto(self):
        self.votos += 1

    def __str__(self):
        return f"{self.nombre} ({self.partido}) - Votos: {self.votos}"


class Votante:
    def __init__(self, nombre, id_votante):
        self.nombre = nombre
        self.id_votante = id_votante
        self.ha_votado = False

    def votar(self, eleccion, candidato):
        if self.ha_votado:
            print(f"⚠️ {self.nombre} ya ha votado y no puede votar de nuevo.")
        elif candidato not in eleccion.candidatos:
            print(f"⚠️ {candidato.nombre} no es un candidato válido en esta elección.")
        else:
            candidato.recibir_voto()
            self.ha_votado = True
            eleccion.votos_registrados.append((self, candidato))
            print(f"✅ {self.nombre} votó por {candidato.nombre}.")

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_votante})"


class Eleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.candidatos = []
        self.votantes = []
        self.votos_registrados = []

    def agregar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def registrar_votante(self, votante):
        self.votantes.append(votante)

    def resultados(self):
        print(f"\n📊 Resultados de la elección: {self.nombre}")
        for c in self.candidatos:
            print(c)
        ganador = max(self.candidatos, key=lambda c: c.votos, default=None)
        if ganador:
            print(f"\n🏆 Ganador: {ganador.nombre} ({ganador.partido}) con {ganador.votos} votos.")

    def __str__(self):
        return f"Elección: {self.nombre} | Candidatos: {len(self.candidatos)} | Votantes: {len(self.votantes)}"


# --- Ejemplo de uso ---
eleccion = Eleccion("Elección Presidencial 2025")

# Candidatos
cand1 = Candidato("Ana Gómez", "Partido Azul")
cand2 = Candidato("Luis Pérez", "Partido Verde")
eleccion.agregar_candidato(cand1)
eleccion.agregar_candidato(cand2)

# Votantes
v1 = Votante("Carlos", "V001")
v2 = Votante("María", "V002")
v3 = Votante("José", "V003")
eleccion.registrar_votante(v1)
eleccion.registrar_votante(v2)
eleccion.registrar_votante(v3)

# Votación
v1.votar(eleccion, cand1)
v2.votar(eleccion, cand2)
v3.votar(eleccion, cand1)
v1.votar(eleccion, cand2)  # intento de voto duplicado

# Resultados
eleccion.resultados()
