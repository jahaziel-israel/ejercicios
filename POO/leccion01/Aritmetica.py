class Aritmatica:
    """
    Clase Aritmetica para realizar Operaciones semar, restra, ect

    """
    def __init__(self,operando_a, operando_b):
        self.operando_a = operando_a
        self.operando_b= operando_b

    def sumar(self):
        return  self.operando_a + self.operando_b

    def multiplicar(self):
        return self.operando_a * self.operando_b

    def dividir(self):
        return self.operando_a / self.operando_b

    def restar(self):
        return self.operando_a - self.operando_b

aritmetica1 = Aritmatica(32,20)
print(f"suma: {aritmetica1.sumar()}")
print(f"multiplicar: {aritmetica1.multiplicar()}")
print(f"dividir: {aritmetica1.dividir():.3f}")
print(f"restar: {aritmetica1.restar()}")

