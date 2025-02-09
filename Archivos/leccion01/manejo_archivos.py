try:
    archivo= open("prueba.txt", "w", encoding= "utf8")
    archivo.write("Agregando información al Archivo:\n")
    archivo.write("Adios!!\n Fin de la prueba..")
except Exception as e:
    print(e)

finally:
    archivo.close()
    print("Fin del Archivo..")
