from Gerentes import Gerente
from EmpleadoS import Empleado


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado("CARLOS", 3000)
imprimir_detalles(empleado)

gerente= Gerente("JUAN",4500, "BODEGA ")
imprimir_detalles(gerente)