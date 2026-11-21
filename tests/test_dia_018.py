from copy import deepcopy
from dia_018.practica import validar_registro

class RegistroDict(dict):
    pass

casos = [
    ({"codigo": "A1", "cantidad": "5"},
     {"codigo": "A1", "cantidad": 5}),

    ({"codigo": " ab12 ", "cantidad": " 003 "},
     {"codigo": "AB12", "cantidad": 3}),

    ({"codigo": "9", "cantidad": "0"},
     {"codigo": "9", "cantidad": 0}),

    ([("codigo", "A1"), ("cantidad", "5")], None),

    (RegistroDict(codigo="A1", cantidad="5"), None),

    ({"codigo": "A1"}, None),

    ({"codigo": "A1", "cantidad": "5", "extra": 1}, None),

    ({"codigo": 123, "cantidad": "5"}, None),

    ({"codigo": " ", "cantidad": "5"}, None),

    ({"codigo": "AÑ1", "cantidad": "5"}, None),

    ({"codigo": "A-1", "cantidad": "5"}, None),

    ({"codigo": "A1", "cantidad": "-1"}, None),
]

aprobados = 0

for numero, (entrada, esperado) in enumerate(casos, start = 1):
    try:
        obtenido = validar_registro(entrada)
        correcto = obtenido == esperado
    except Exception as error:
        obtenido = f"EXCEPCION: {error!r}"
        correcto = False
    if correcto:
        aprobados += 1
    print(
        f"Caso {numero:02}: "
        f"{'PASS' if correcto else 'FAIL'}"
    )
    if not correcto:
        print(f" Esperado: {esperado!r}")
        print(f" Obtenido: {obtenido!r}")
print(f"\nResultado funcional: {aprobados}/12")

original = {"codigo": " ab12 ","cantidad":" 003 "}
copia = deepcopy(original)
resultado = validar_registro(original)
inmutable_valido = (
    original == copia
    and resultado is not original
    and resultado == {"codigo": "AB12", "cantidad": 3}
)
print(
    "Inmutabilidad valida:",
    "PASS" if inmutable_valido else "FAIL"
)

invalido = {"codigo": " ab12 ", "cantidad": "-1"}
copia_invalida = deepcopy(invalido)
resultado_invalido = validar_registro(invalido)

inmutable_invalido = (
    invalido == copia_invalida
    and resultado_invalido is None
)

print(
    "Inmutabilidad inválida:",
    "PASS" if inmutable_invalido else "FAIL"
)