print("proporcioine informacion del libro:")
nombre= input("Proporcione el nombre del libro: ")
id= int(input("proporcione el id del libro: "))
precio= float(input("proporcione el precio del libro: "))
envioGrstuito= input("indica si es envio gratuito true/false: ")

if envioGrstuito == "true":
    envioGrstuito= True
elif envioGrstuito == "false":
    envioGrstuito= False
else:
    envioGrstuito= ("valor incorrecto debe escribir true/false: ")
print(f'''
    nombre: {nombre}
    id: {id}
    precio: {precio}
    envio gratuito? {envioGrstuito}

''')
