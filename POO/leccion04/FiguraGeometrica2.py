#ABC = Abstract Base Class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self.__validar_valor(ancho):
         self.__ancho= ancho
        else:
            self.__ancho = 0
            print(f"Valor erroneo de ancho: {ancho}")
        if self.__validar_valor(alto):
         self.__alto= alto
        else:
            self.__alto= 0
            print(f"Valor erroneo de alto: {alto}")

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        if self.__validar_valor(ancho):
           self.__ancho = ancho
        else:
            print(f"Valor erroneo de ancho: {ancho}")

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        if self.__validar_valor(alto):
            self.__alto= alto
        else:
            print(f"Valor erroneo de alto: {alto}")

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f"FiguraGeometrica: [ancho: {self.__ancho}, alto: {self.__alto}]"

    def __validar_valor(self, valor):
        return True if 0 < valor < 10 else False

