from  dia_017.practica import convertir_stock
def validar_registro(registro):
    if type(registro) is not dict:
        return None
    claves_validas = {"codigo","cantidad"}
    if set(registro.keys()) != claves_validas:
        return None
    codigo = registro['codigo']
    if type(codigo) is not str:
        return None
    valor_normalizado = codigo.strip().upper()
    if not valor_normalizado:
        return None
    for caracter in valor_normalizado:
        es_letra = 'A' <= caracter <= 'Z'
        es_numero = '0' <= caracter <= '9'
        if not (es_letra or es_numero):
            return None
    cantidad = registro['cantidad']
    conversion = convertir_stock(cantidad)
    if conversion is None:
        return None
    nuevo_registro={
        "codigo": valor_normalizado,
        "cantidad": conversion
    }
    return nuevo_registro