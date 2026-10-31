ventas = {
    "Teclado": [45.5, 30.0],
    "Mouse": [25.0, 25.0, 25.0],
    "Monitor": [750.0],
    "Cable": [],
    "Webcam": [120.0, -15.0, "error", 80.0]
}
def validar_ventas(ventas):
    if not type(ventas) is dict:
        return None
    ventas_validas = {}
    for venta in ventas:
        importes_validos = []
        if not type(venta) is str:
            continue
        normalizar_venta = venta.strip()
        if not normalizar_venta:
            continue
        if not type(ventas[venta]) is list:
            continue
        for importe in ventas[venta]:
            if (type(importe) is int or type(importe) is float) and importe > 0:
                importes_validos.append(importe)
        if normalizar_venta in ventas_validas:
            ventas_validas[normalizar_venta] += importes_validos
        else:
            ventas_validas[normalizar_venta] = importes_validos
    return ventas_validas
def calcular_resumen(ventas_validas):
    resumen_ventas = {}
    for ventas in ventas_validas:
        cantidad = len(ventas_validas[ventas])
        total = sum(ventas_validas[ventas])
        if cantidad == 0:
            promedio = 0
        else:
            promedio = total / cantidad
        resumen_ventas[ventas] = {
            "cantidad" : cantidad,
            "total" : total,
            "promedio" : promedio
        }
    return resumen_ventas  
def guardar_reporte(ruta, resumen):
    total = 0
    try:
        with open(ruta,"w",encoding="utf-8") as archivo:
            archivo.write("REPORTE DE VENTAS\n")
            archivo.write("-" * 30)
            archivo.write("\n")
            resumen_ordenado = sorted(resumen)
            for res in resumen_ordenado:
                archivo.write(f"{res} | Cantidad: {resumen[res]["cantidad"]} | Total: S/ {resumen[res]["total"]:.2f} | Promedio: S/ {resumen[res]["promedio"]:.2f}\n")
                total += resumen[res]["total"]
            archivo.write("-" * 30)
            archivo.write("\n")
            archivo.write(f"TOTAL GENERAL: S/ {total:.2f}")
        return True
    except OSError:
        return False
resultado = validar_ventas(ventas)
resumen_ventas = calcular_resumen(resultado)
respuesta = guardar_reporte("reporte_ventas.txt",resumen_ventas)
print(respuesta)