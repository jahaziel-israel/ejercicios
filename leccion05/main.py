# definir una lista de tipo string
nombres = ["maria","israel","anabel"]
# imprimir la lista de nombres
print(nombres)
# acceder a los elementos de la lista
print(nombres[0])
print(nombres[2])
# acceder a los elementos de manera inversa
print(nombres[-2])
# preguntar el largo de una lista
print(len(nombres))
# agregar un elemento
nombres.append("jahaziel,ela")
print(nombres)
# insertar un elemento en un indice en especifico
nombres.insert(2, "carlos")
print(nombres)
# remover un elemento
nombres.remove("jahaziel,ela")
print(nombres)
# remover el ultimo valor de la lista
nombres.pop()
print(nombres)
# eliminar un indice
del nombres [2]
print(nombres)
# limpiar todos lo elementos
nombres.clear()
print(nombres)
# borrar la lista por completo
del nombres
print(nombres)
# imprimir un rango
print(nombres[0:2]) # sin incluir el indice 2
#ir del inicio de la lista al indice ( sin incluirlo)
print(nombres[ : 3])
# desde el indice indicado asta el final de lista
print(nombres[1: ])
# cambio de un valor
nombres[2]= "gordo"
print(nombres)
# iterar la lista
for nombre in nombres:
    print(nombre)
else: print("no existen mas nombres en la lista")

#definir una tupla:
frutas= ("sandia","manzana","mandarina")
print(frutas)
#saber el largo:
print(len(frutas))
#acceder a un elemento
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#acceder a un rango de valor
print(frutas[0:3])
# recorrer elemento
for fruta in frutas:
    print(fruta, end= " " )

# cambiar el valor tupla
frutaslista = list(frutas)
frutaslista [0]= "melon"
frutas= tuple(frutaslista)
print("\n" ,frutas)
# eliminar la tupla
# del frutas

# set ORDENAR
planetas = {"tierra","saturno","pluton","marte"}
print(planetas)
# largo
print(len(planetas))
# revisar si un elemento esta presente
print("saturno" in planetas)
#agregar un elemento
planetas.add("venus")
print(planetas)
#no se pueden duplicar elementos
planetas.add("tierra")
print(planetas)
# eliminar elementos
planetas.remove("tierra")
print(planetas)
#eliminar elemento sin error
planetas.discard("pluton")
print(planetas)
#limpiar set
planetas.clear()
print(planetas)
#eliminar set
del planetas
print(planetas)

# diccionarios (dict) key , value

diccionario = {
    "IDE":"integrated development environment",
    "OOP":"object oriented programming",
    "DBMS":"database management system"
}
print(diccionario)

#largo
print(len(diccionario))

#acceder a un elemento (key)
print(diccionario["OOP"])

#Otra forma de recuperar un elemento
print(diccionario.get("IDE"))

#Modificar un elemento
diccionario ["DBMS"] = "Database Management System..."
print(diccionario)

#recorrer los elementos
for termino , valor in diccionario.items():
    print(termino,valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#comprobar existencia de un elemento
print("OOP"in diccionario)

#agregar un elemento
diccionario ["PK"]= "Primary Key"
print(diccionario)

#remover un elemento
diccionario.pop("OOP")
print(diccionario)

#limpiar
diccionario.clear()
print(diccionario)

#eliminar diccionario
del diccionario
print(diccionario)
