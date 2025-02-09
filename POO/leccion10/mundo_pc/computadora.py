from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Computadora:
    contador_computadoras= 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora= Computadora.contador_computadoras
        self._nombre= nombre
        self._monitor= monitor
        self._teclado= teclado
        self._raton= raton

    @property
    def id_computadora(self):
        return self.id_computadora

    @id_computadora.setter
    def id_computadora(self, id_computadora):
        self._id_computadora= id_computadora

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre= nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor= monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado= teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self,raton):
        self._raton= raton


    def __str__(self):
        return f"""
    {self._nombre} : {self._id_computadora}
    Monitor: {self._monitor}
    Teclado: {self._teclado}
    Raton: {self._raton}    
    """
if __name__ == "__main__":
    teclado1= Teclado("HP", "Bluetooth")
    raton1= Raton("HP", "USB")
    monitor1= Monitor("LG", "55 PULGADAS")
    computadora=Computadora("APPLE", monitor1,teclado1,raton1)
    print(computadora)

    teclado2= Teclado("acer", "Bluetooth")
    raton2= Raton("HP", "USB")
    monitor2= Monitor("Samsung", "55 PULGADAS")
    computadora2=Computadora("Hp PRO", monitor2,teclado2,raton2)
    print(computadora2)