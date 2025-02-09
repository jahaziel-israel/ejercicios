class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca= marca
        self.modelo=modelo
        self.camara= camara

    def llamar(self):
        print(f"Estas haciendo una llamada desde un {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamada desde tu {self.modelo}")

celular1= Celular("Xaomi", "Redmi 13 Pro", "60Mp" )
celular2= Celular("Apple", "Iphone 15 Pro", "90Mp")

celular1.llamar()
celular1.cortar()
print(celular2.modelo)