palabra= input("Proporciona una Palabra: ")
vocales= " a e i o u "
contador= 0
for letra in palabra:
        if letra in vocales:
                contador= contador+1
print(f"la palabra tiene {contador} vocales")

