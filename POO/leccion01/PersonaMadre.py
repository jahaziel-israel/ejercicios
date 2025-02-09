# class Persona:
#     def __init__(self, nombre, apellido, edad, nacionalidad, *valores, **terminos):
#         self.nombre= nombre
#         self.apellido= apellido
#         self.edad=edad
#         self.nacionalidad= nacionalidad
#         self.valores= valores
#         self.terminos= terminos
#
#     def mostrar_detalle(self):
#         print(f"{self.nombre}, {self.apellido}, {self.edad}, {self.nacionalidad}, {self.valores}, {self.terminos}")
#
#
#
# persona_1= Persona("israel", "Perez", "28 años", "Mexicano", "32432424242",23, m="manzana", s="sandia")
# persona_1.mostrar_detalle()
# persona_1.telefono= "0987979978"
# print(persona_1.telefono)
# Persona.mostrar_detalle(persona_1)

# persona_2= Persona("Juan","Lopez", "38 años", "Mexicano")
# persona_2.mostrar_detalle()
# persona_2.telefono= "2345467676"
# print(persona_2.telefono)


class Persona:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.__nombre= nombre
        self.__apellido= apellido
        self.__edad=edad
        self.__nacionalidad= nacionalidad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre= nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def nombre(self, edad):
        self.__edad = edad

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    def mostrar_detalle(self):
        print(f"{self.__nombre}, {self.__apellido}, {self.__edad}, {self.__nacionalidad}")

    def __del__(self):
        print(f"persona: {self.__edad}, {self.__apellido}")

if __name__ == "__main__":

    persona_1= Persona("israel", "Perez", "28 años", "Mexicano")

    persona_1.apellido= "Mejia Perez"
    persona_1.nombre= "Jahaziel israel"

    persona_1.mostrar_detalle()
    print(__name__)