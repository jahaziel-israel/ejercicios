import os
class CatalogoPelículas:

    ruta_archivo= "películas.txt"

    @classmethod
    def agregar_película(cls, película):
        with open(cls.ruta_archivo, "a", encoding="utf8") as archivo:
            archivo.write(f"{película.nombre}\n")


    @classmethod
    def listar_películas(cls):
        with open(cls.ruta_archivo, "r", encoding="utf8") as archivo:
            print("Catalogo de Películas".center(60, "-"))
            print(archivo.read())


    @classmethod
    def eliminar_películas(cls):
        os.remove(cls.ruta_archivo)
        print(f"Archivo eliminado: {cls.ruta_archivo}")







