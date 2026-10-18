# Descuento condicionado

precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

if cantidad > 0 and precio >= 0:
    subtotal = precio * cantidad
    if subtotal < 50:
        total = subtotal
        print(f"El total sin descuento es {total}")
    else:
        total = subtotal - 10
        print(f"El total con descuento es {total}")
else:
    print("Error")


