class Rectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

base= int(input("Proporciona la base: "))
altura= int(input("proporciona la altura: "))

rectangulo1 = Rectangulo(base,altura)
print(f"Area del rectangulo: {rectangulo1.calcular_area()}")

base= int(input("Proporciona la base: "))
altura= int(input("proporciona la altura: "))

rectangulo2 = Rectangulo(base,altura)
print(f"Area del rectangulo: {rectangulo2.calcular_area()}")

