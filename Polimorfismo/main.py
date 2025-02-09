class Gato:
    def sonido(self):
        return ("miauu")

class Perro:
    def sonido(self):
        return ("guuaa")

def hacer_sonido(animal):
    print(animal.sonido())

gato= Gato()
perro= Perro()
hacer_sonido(gato)

