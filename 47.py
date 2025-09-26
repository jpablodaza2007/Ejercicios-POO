from datetime import datetime

class Paquete:
    def __init__(self, id_paquete, destino, peso):
        self.id_paquete = id_paquete
        self.destino = destino
        self.peso = peso
        self.entregado = False

    def __str__(self):
        estado = "Entregado" if self.entregado else "Pendiente"
        return f"📦 Paquete {self.id_paquete} -> {self.destino} ({self.peso}kg) [{estado}]"


class Vehiculo:
    def __init__(self, placa, capacidad, velocidad_promedio):
        self.placa = placa
        self.capacidad = capacidad  # kg máximos
        self.velocidad_promedio = velocidad_promedio  # km/h
        self.carga_actual = []
        self.ruta = None

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def cargar_paquete(self, paquete):
        if self.peso_total() + paquete.peso <= self.capacidad:
            self.carga_actual.append(paquete)
            return True
        return False

    def peso_total(self):
        return sum(p.peso for p in self.carga_actual)

    def tiempo_entrega_estimado(self):
        if not self.ruta:
            return None
        return self.ruta.distancia / self.velocidad_promedio

    def __str__(self):
        return f"🚚 Vehículo {self.placa} | Capacidad: {self.capacidad}kg | Carga: {self.peso_total()}kg"


class Ruta:
    def __init__(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia  # km

    def __str__(self):
        return f"Ruta {self.origen} -> {self.destino} ({self.distancia}km)"


class Almacen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.paquetes = []
        self.vehiculos = []
        self.rutas = []

    def agregar_paquete(self, paquete):
        self.paquetes.append(paquete)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)

    def optimizar_entregas(self):
        print(f"\n🚀 Optimizando entregas en {self.nombre}...")
        for paquete in self.paquetes:
            if paquete.entregado:
                continue
            # Buscar vehículo con capacidad suficiente y menor carga actual
            vehiculo_elegido = None
            for v in self.vehiculos:
                if v.cargar_paquete(paquete):
                    vehiculo_elegido = v
                    break
            if vehiculo_elegido:
                print(f"✅ Paquete {paquete.id_paquete} asignado a {vehiculo_elegido.placa}.")
            else:
                print(f"❌ No hay vehículo disponible para {paquete.id_paquete} (exceso de peso).")

    def reporte_entregas(self):
        print(f"\n📊 Reporte de entregas - {self.nombre}")
        for v in self.vehiculos:
            print(f"\n{v}")
            if v.ruta:
                print(f"  {v.ruta} | Tiempo estimado: {v.tiempo_entrega_estimado():.1f}h")
            for p in v.carga_actual:
                print(f"  - {p}")

    def __str__(self):
        return f"🏢 Almacén {self.nombre} | Paquetes: {len(self.paquetes)} | Vehículos: {len(self.vehiculos)}"


# --- Ejemplo de uso ---
almacen = Almacen("Central Bogotá")

# Rutas
ruta1 = Ruta("Bogotá", "Medellín", 420)
ruta2 = Ruta("Bogotá", "Cali", 460)

# Vehículos
v1 = Vehiculo("ABC123", 200, 80)
v2 = Vehiculo("XYZ789", 500, 70)

v1.asignar_ruta(ruta1)
v2.asignar_ruta(ruta2)

# Paquetes
p1 = Paquete("P001", "Medellín", 50)
p2 = Paquete("P002", "Cali", 100)
p3 = Paquete("P003", "Medellín", 180)
p4 = Paquete("P004", "Cali", 300)

# Cargar datos al almacén
almacen.agregar_paquete(p1)
almacen.agregar_paquete(p2)
almacen.agregar_paquete(p3)
almacen.agregar_paquete(p4)

almacen.agregar_vehiculo(v1)
almacen.agregar_vehiculo(v2)

almacen.agregar_ruta(ruta1)
almacen.agregar_ruta(ruta2)

# Optimización y reporte
almacen.optimizar_entregas()
almacen.reporte_entregas()
