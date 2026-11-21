from escritura_segura import escribir_texto_seguro


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
            if not normalizar_nombre or "\n" in normalizar_nombre or "\r" in normalizar_nombre:
                rechazados += 1
            else:
                lista_nombres.append(normalizar_nombre)
                guardados += 1
        else:
            rechazados += 1
    lineas = (f"{nombre}\n" for nombre in lista_nombres)
    if not escribir_texto_seguro(ruta, lineas):
        return None
    return guardados, rechazados


if __name__ == "__main__":
    print(guardar_nombre("nombres.txt", nombres))
