from Cuadrado01 import Cuadrado
from Rectangulo01 import Rectangulo

#No se puede instanciar un clase abstracta
# figura= FiguraGeometrica2()

print("Creacion de Objeto Cuadrado".center(50, "-"))

cuadrado1= Cuadrado(lado= 5, color ="VERDE")
cuadrado1.alto = 9
cuadrado1.ancho= 9
print(f"Calculo del area de un cuadrado: {cuadrado1.calcular_area()}")
print(cuadrado1)

print("Creacion de Obejeto Rectangulo".center(50, "-"))

rectangulo1= Rectangulo(9, 8, "ROJO")
rectangulo1.ancho= 15

print(f"Calculo del area del rectangulo: {rectangulo1.calcular_area()}")
print(rectangulo1)



# MRO - Method Resolution Order
print(Cuadrado.mro())
print(Rectangulo.mro())

