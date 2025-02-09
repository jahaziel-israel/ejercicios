materias= int(input("introduce el numero de materias:"))
suma= 0
for materia in range(1, materias+1):
    calificaciones= int(input(f"ingresa tu calificacion {materia}: "))
    suma= calificaciones + suma
promedio= suma / materias

if promedio < 5:
    print("reprobaste")

print(f"tu promedio es: {promedio}")