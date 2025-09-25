class relog:
    def __init__(self, horas, minutos, segundos):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
    def ajustar_horas(self, horas):
        if 0 <= horas < 24:
            self.horas = horas
        else:
            print("Hora inválida. Debe estar entre 0 y 23.")

h1 = relog(12,30,20)
