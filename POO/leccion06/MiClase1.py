class MiClase:

    variable_clase= "Valor variable de clase "

    def __init__(self, variable_instancia):
        self.variable_instancia=  variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_instancia)
        print(self.variable_clase)


MiClase.metodo_estatico()
MiClase.metodo_clase()
miObjeto1= MiClase("variable_instancia")
miObjeto1.metodo_clase()
miObjeto1.metodo_estatico()
miObjeto1.metodo_instancia()

# miclase= MiClase("VALOR VARIABLE INSTANCIA")
#
# print(MiClase.variable_clase)
# print(miclase.variable_instancia)
# print(miclase.variable_clase)
#
# MiClase.variable_clase2= "Valor variable de clase 2"
#
# miclase2= MiClase("Otro valor variable de instancia")
# print(miclase2.variable_instancia)
# print(miclase2.variable_clase)
# print(miclase.variable_clase2)
# print(miclase.variable_clase2)
# print(miclase2.variable_clase2)