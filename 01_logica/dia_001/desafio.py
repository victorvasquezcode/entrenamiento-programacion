# Descuento fijo

precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

subtotal = precio_unitario * cantidad
total = subtotal - 10

if total < 0:
    total = 0

print(f"Subtotal: S/ {subtotal:.2f}")
print(f"Total a pagar: S/ {total:.2f}")