class Animal:
    def comer(self):
        print("el animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("el animal esta VOLANDO")

class Mamifero(Animal):
    def amamantar(self):
        print("el animal esta amamantando")

class Murcielago(Mamifero,Ave):
    pass

murcielago= Murcielago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()
print(Murcielago.mro())