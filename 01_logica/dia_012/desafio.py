import math

from escritura_segura import escribir_texto_seguro


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
            if type(importe) in (int, float) and 0 < importe < math.inf:
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
    separador = "-" * 30 + "\n"
    lineas = ["REPORTE DE VENTAS\n", separador]
    total = 0
    for producto in sorted(resumen):
        datos = resumen[producto]
        lineas.append(
            f"{producto} | Cantidad: {datos['cantidad']} | "
            f"Total: S/ {datos['total']:.2f} | Promedio: S/ {datos['promedio']:.2f}\n"
        )
        total += datos["total"]
    lineas.extend([separador, f"TOTAL GENERAL: S/ {total:.2f}"])
    return escribir_texto_seguro(ruta, lineas)


if __name__ == "__main__":
    print(guardar_reporte("reporte_ventas.txt", calcular_resumen(validar_ventas(ventas))))
