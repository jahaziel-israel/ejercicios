class Orden:
    contador_ordenes= 0
    def __init__(self, computadora):
        Orden.contador_ordenes += 1
        self._id_orden= Orden.contador_ordenes
        self._computadora= computadora

    @property
    def id_orde(self):
        return self._id_orden

    @id_orde.setter
    def id_orden(self, id_orden):
        self._id_orden= id_orden

    @property
    def computadora(self):
        return self._computadora

    @computadora.setter
    def computadora(self, computadora):
        self._computadora= computadora

    def agregar_computadora(self, computadora):
        self._computadora.append(computadora)

    def __str__(self):
        computadora_str= ""
        for computadora in self._computadora:
            computadora_str += computadora.__str__()

        return f"""
            Orden: {self._id_orden}
            Computadoras: {computadora_str}
        """
