nombres = [
    " ana ",
    "LUIS",
    "",
    "  ",
    "maria",
    25,
    "pedro"
]
def guardar_nombre(ruta, nombres):
    if type(nombres) is not list:
        return None
    rechazados = 0
    guardados = 0
    lista_nombres = []
    for nombre in nombres:
        if type(nombre) is str:
            normalizar_nombre = nombre.strip().title()
            if not normalizar_nombre:
                rechazados += 1
            else:
                lista_nombres.append(normalizar_nombre)
                guardados += 1
        else:
            rechazados += 1
    try:
         with open(ruta,"w",encoding="utf-8") as archivo:
            for lista in lista_nombres:
                archivo.write(f"{lista}\n")
    except OSError:
        return None
    return guardados, rechazados
guardados, rechazados = guardar_nombre("nombres.txt",nombres)
print(guardados, rechazados)