from NumerosIdenticosExcepcion import NumerosIdenticos

resultado= None
try:
    a = int(input("introduce un mumero: "))
    b = int(input("introduce otro numero: "))

    if a == b:
        raise NumerosIdenticos("NUMEROS IDENTICOS")

    resultado = a/b
except ZeroDivisionError as z:
    print(f"Ocurrio un error: {z}")
except TypeError as t:
    print(f"Ocurrio un error: {t}")
except Exception as e:
    print(f"Ocurrio un error: {e}")

else:
    print("no se arrojo ninguna excepcion..")

finally:
    print("ejecucion del bloque finally...")

print(f"resultado: {resultado}")
print("continuamos....!!!")