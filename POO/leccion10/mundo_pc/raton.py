from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones= 0

    def __init__(self,marca, dispositivo_entrada,):
        Raton.contador_ratones += 1
        self._id_raton= Raton.contador_ratones
        super().__init__(marca, dispositivo_entrada)

    @property
    def id_raton(self):
        return self._id_raton

    @id_raton.setter
    def id_raton(self, id_raton):
        self._id_raton= id_raton



    def __str__(self):
        return f"id: {self.id_raton}, Marca: {self.marca}, Tipo_entrada: {self.tipo_entrada}"


if __name__ == "__main__":
    raton1= Raton("HP", "USB")
    print(raton1)

    raton2= Raton("Acer", "Bluetooth")
    print(raton2)