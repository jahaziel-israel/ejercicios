from dominio.Pelicula import Pelicula
from servicio.catalago_peliculas import CatalogoPelículas as cp

opcion= None
while opcion != 4:
    try:
        print("Opciones".center(50,"*"))
        print("1. Agregar Pelicula")
        print("2. Listar Pelicula")
        print("3. Eliminar Pelicula")
        print("4. Salir")
        opcion= int(input("Escribe tu Opcion (1-4): "))

        if opcion == 1:
            nombre_pelicula=input("Proporciona el nombre de la Pelicula: ")
            pelicula= Pelicula(nombre_pelicula)
            cp.agregar_película(pelicula)

        elif opcion == 2:
            cp.listar_películas()

        elif opcion == 3:
            cp.eliminar_películas()

    except Exception as e :
        print(f"Ocurrio un error: {e}")
        opcion= None
else:
    print("Salimos del Programa".center(50,"-"))
