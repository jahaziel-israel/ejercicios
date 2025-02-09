# from super_mercado import total
#
#
# class Usuario:
#     def __init__(self,articulos, precio1,precio2,precio3):
#         self.articulos = articulos
#         self.precio1 = precio1
#         self.precio2 = precio2
#         self.precio3 = precio3
#
#     def __str__(self):
#         return f"precio1: {self.precio1},precio2: {self.precio2}, precio3: {self.precio3}"
#
#     def total(self):
#         return total

articulos= int(input("Cuantos articulos vas a comprar? "))
total= 0
for articulo in range(1, articulos+1):
    precio1 = int(input(f"Introduce el precio del articulo {articulo} : "))

    total= precio1 + total

if  total > 500:
    print("exediste limite")

print(f"total de compras : {total}")
