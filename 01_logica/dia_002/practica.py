# Control de acceso

edad = int(input("Edad: "))
estado = input("Estado: ")

if edad >= 18 and estado == "si":
    print("Acceso permitido")
else:
    print("Acceso denegado")
