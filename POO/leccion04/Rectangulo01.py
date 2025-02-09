from  FiguraGeometrica2 import FiguraGeometrica
from Color import Colores

class Rectangulo(FiguraGeometrica, Colores):
    def __init__(self,ancho, alto,color):
        FiguraGeometrica.__init__(self, ancho,alto)
        Colores.__init__(self,color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)}, {Colores.__str__(self)}"