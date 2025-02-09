class Persona:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad

    def __str__(self):
        return f"persona: [nombre:{self.nombre} edad:{self.edad}]"

class Empleado(Persona):
    def __init__(self,nombre ,edad , sueldo):
        super().__init__(nombre, edad)
        self.sueldo= sueldo

    def __str__(self):
        return f"{super().__str__()} sueldo: {self.sueldo}"