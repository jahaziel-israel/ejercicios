class Cubo:
    def __init__(self, alto, ancho, profundo):
        self.alto = alto
        self.ancho= ancho
        self.profundo= profundo

    def cacular_volumen(self):
        return self.alto * self.ancho * self.profundo

alto= int(input("Proporciona la altura: "))
ancho = int(input("Proporciona el ancho: "))
profundo= int(input("Proporciona el profundo: "))

cubo_1= Cubo(alto, ancho, profundo)

print(f"el volumen del cubo es : {cubo_1.cacular_volumen()}")

alto= int(input("Proporciona la altura: "))
ancho = int(input("Proporciona el ancho: "))
profundo= int(input("Proporciona el profundo: "))

cubo_2 = Cubo(alto, ancho, profundo)

print(f"el volumen del Cubo es : {cubo_2.cacular_volumen()}")