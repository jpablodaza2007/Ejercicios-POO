import time

class Semaforo:
    def __init__(self, tiempo_rojo=5, tiempo_amarillo=2, tiempo_verde=5):
        self.estados = ["Rojo", "Verde", "Amarillo"]
        self.tiempos = {
            "Rojo": tiempo_rojo,
            "Verde": tiempo_verde,
            "Amarillo": tiempo_amarillo
        }
        self.estado_actual = "Rojo"

    def cambiar(self):
        if self.estado_actual == "Rojo":
            self.estado_actual = "Verde"
        elif self.estado_actual == "Verde":
            self.estado_actual = "Amarillo"
        elif self.estado_actual == "Amarillo":
            self.estado_actual = "Rojo"

    def iniciar(self, ciclos=1):
        for _ in range(ciclos):
            for estado in self.estados:
                self.estado_actual = estado
                print(f"Semáforo en {estado} ({self.tiempos[estado]}s)")
                time.sleep(self.tiempos[estado])  

    def __str__(self):
        return f"Semáforo en estado: {self.estado_actual}"

semaforo = Semaforo(tiempo_rojo=3, tiempo_amarillo=1, tiempo_verde=4)

print(semaforo)        # Estado inicial
semaforo.iniciar(ciclos=2)  # Corre dos ciclos completos
