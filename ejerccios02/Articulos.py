class Articulo:

    def __init__(self, nombre, precio):
        self.nombre= nombre
        self.precio= precio

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}"

class Calculo:
    def __init__(self, lista):
        self.lista= lista

    def calculo_total(self):
        total= 0
        for articulo in self.lista:
            total=articulo.precio + total
            len(self.lista)
        return total

    def promedio_total(self):
        promedio= 0
        total= self.calculo_total()
        promedio=total / len(self.lista)
        return promedio


articulos=[]
mi_articulo=Articulo("Papel",23.00)
mi_articulo2=Articulo("JABON",23.50)
mi_articulo3=Articulo("sal", 12.89)

articulos.append(mi_articulo3)
articulos.append(mi_articulo)
articulos.append(mi_articulo2)
articulos.append(mi_articulo3)
articulos.remove(mi_articulo3)

total1= Calculo(articulos)
print(total1.calculo_total())
total1= Calculo.promedio_total()
print(total1)
# for articulo in articulos:
#     print(articulo)



