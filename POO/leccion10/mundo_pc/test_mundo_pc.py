from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado
from orden import Orden

teclado1= Teclado("HP", "Bluetooth")
raton1= Raton("HP", "USB")
monitor1= Monitor("LG", "55 PULGADAS")
computadora=Computadora("APPLE", monitor1,teclado1,raton1)

teclado2= Teclado("acer", "Bluetooth")
raton2= Raton("HP", "USB")
monitor2= Monitor("Samsung", "55 PULGADAS")
computadora2=Computadora("Hp PRO", monitor2,teclado2,raton2)

teclado3= Teclado("Gamer", "Bluetooth")
raton3= Raton("HP", "Bluetooth")
monitor3= Monitor("Samsung", "80 PULGADAS")
computadora3=Computadora("Gamer Pro Max", monitor3,teclado3,raton3)

computadoras01= [computadora, computadora2]
orden1= Orden(computadoras01)
print(orden1)
orden1.agregar_computadora(computadora3)
print(orden1)