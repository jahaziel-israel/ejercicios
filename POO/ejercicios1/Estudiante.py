class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre= nombre
        self.edad= edad
        self.grado= grado

    def estudiar(self):
        print("Estudiando....")



nombre= input("Proporcione su nombre: ")
edad=int(input("Proporcione su edad: "))
grado= input("Proporcione su grado: ")



estudiante1= Estudiante(nombre,edad,grado)
print(f"""
    Datos del estudiante: \n\n
    Nombre:{estudiante1.nombre} \n
    Edad: {estudiante1.edad} \n
    Grado: {estudiante1.grado} \n

""")
estudiar= input()
if (estudiar.lower() == "estudiando...."):
    print(estudiante1.estudiar())




