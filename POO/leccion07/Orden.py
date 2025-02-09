from Producto import Producto


class Ordenes:
    contador_ordenes= 0


    def __init__(self, productos):
        Ordenes.contador_ordenes+= 1
        self._id_orden = Ordenes.contador_ordenes
        self._productos = list(productos)


    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total= 0
        for producto in self._productos:
            total+= producto.precio
        return total

    def __str__(self):
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__() + "--"

        return f"orden: {self._id_orden}, \nproductos: {productos_str}"

if __name__ == "__main__":
    producto01 = Producto("Camisa", 120.00)
    producto02 = Producto("Pantalon", 300.00)
    productos1 = [producto01,producto02]
    orden1 = Ordenes(productos1)
    print(orden1)
    orden2 = Ordenes(producto02)
