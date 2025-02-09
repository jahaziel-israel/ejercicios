# def miFuncion(nombre, apellido):
#     print("hola")
#     print(f"{nombre} , {apellido}")
#
#
# miFuncion("israel","mejia")
# miFuncion("maria", "del carmen")

# def sumar (a,b):
#     return a+b
#
# resultado= sumar (20,25)
# print(resultado)
# #print({sumar(20,25)})

# def listar_nombres(*nombres):
#     for nombre in nombres:
#         print(nombre)
#
# listar_nombres("jahaziel", "mary", "nestor","anabel")
# listar_nombres("laura","carlos")

# def listarterminos(**terminos):
#     for llave, valor in terminos.items():
#         print(f"{llave} : {valor}")
#
# listarterminos(ppcds= "Puro Pinche Cartel de Santa", pk= "Primary Key")
# listarterminos(alv= "a la Verga")
#
# def desplegar_nombres(nombres):
#     for nombre in nombres:
#         print(nombre)
#
# nombres= ["david", "edgar", "arturo"]
# desplegar_nombres(nombres)
# desplegar_nombres("carlos")
# desplegar_nombres([10.3, 14.5])
# desplegar_nombres((10, 14))

#funcion recursiva
#5! = 5 * 4 * 3 * 2 * 1
#5! = 5 * 4 * 3 * 2
#5! = 5 * 4 * 6
#5! = 5 * 24
#5! = 120

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
numero = 10
resultado = factorial(numero)
print(f"el factorial de {numero} es: {resultado}")
