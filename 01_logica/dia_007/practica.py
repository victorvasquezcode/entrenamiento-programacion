#Registro de códigos de productos
codigos = []
contador = 0
for numero_producto in range(1,6):
    while True:
        codigo = input("Ingrese el codigo: ").strip().upper()
        if len(codigo) == 5 and codigo[:2].isalpha()  and codigo[2:].isdigit():
            print("Codigo valido")
            break
        print("Codigo invalido")
    codigos.append(codigo)

for codigo in codigos:
    if codigo[:2] == "AB":
        contador += 1

print(f"Lista de codigos: {codigos}\nContador de AB: {contador}")
