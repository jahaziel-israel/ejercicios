mes= int(input("proporciona mes del año (1 - 12): "))
estacion= None
if mes == 1 or mes == 2 or mes == 12:
    estacion= "invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion= "primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion= "verano"
elif mes == 9 or  mes == 10 or mes == 11:
    estacion= "otoño"
else:
    estacion= "mes incorrecto"

print(f"para el mes {mes} la estacion es: {estacion}")

edad= int(input("PROPORCIONA TU EDAD: "))
mensaje= None
if 0 <= edad < 10:
    mensaje= "la infancia es increibre..."
elif 10<= edad < 20:
    mensaje= "muchos cambios mucho estudio..."
elif 20<= edad < 30:
    mensaje= "amor y comienza el trabajo..."
else:
    mensaje= ("etapa de vida no reconocida...")
print(f"tu edad es : {edad} - {mensaje}")

my_stringn_variable= "My String variable"
print(my_stringn_variable)

amiGos= ("Mi Nombres es:")
print(amiGos)
nombre= "Jahaziel israel"
print(nombre)

mensaje= "Quiero qe me apoyen , estoy iniciando en este mundo de Python"
print(mensaje)

