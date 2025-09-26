class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado

    def calcular_salario(self):
        raise NotImplementedError("Este método debe ser implementado en las subclases")

    def __str__(self):
        return f"Empleado: {self.nombre} (ID: {self.id_empleado})"
    

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, id_empleado, salario_mensual):
        super().__init__(nombre, id_empleado)
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

    def __str__(self):
        return f"{super().__str__()} - Tiempo Completo, Salario mensual: {self.salario_mensual}"
    

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, id_empleado, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, id_empleado)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora

    def __str__(self):
        return f"{super().__str__()} - Medio Tiempo, {self.horas_trabajadas}h x {self.pago_por_hora}/h"

empleado1 = EmpleadoTiempoCompleto("Ana Pérez", 101, 3000)
empleado2 = EmpleadoMedioTiempo("Luis Gómez", 102, 80, 15)

print(empleado1)
print("Salario:", empleado1.calcular_salario())

print(empleado2)
print("Salario:", empleado2.calcular_salario())
