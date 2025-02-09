from EmpleadoS import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamneto):
        super().__init__(nombre, sueldo)
        self.departamento = departamneto

    def __str__(self):
        return (f"Gerente: {self.departamento} [{super().__str__()}]")

