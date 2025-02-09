from Orden import Ordenes
from Producto import Producto

producto1 = Producto("Camisa", 120.00)
producto2 = Producto("Pantalon", 300.00)
producto3 = Producto("calsetines", 50.00)
producto4 = Producto("blusa", 100.00)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Ordenes(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)

print(orden1)
print(orden1.calcular_total())
orden2 = Ordenes(productos2)

print(orden2)
print(orden2.calcular_total())
