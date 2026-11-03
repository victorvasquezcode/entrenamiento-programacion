
import os
import tempfile
from unittest.mock import patch
from desafio import guardar_inventario_seguro
inventario_valido = {
    "P001": {
        "nombre": "Teclado",
        "stock": 10,
        "precio": 45.50
    }
}
# PRUEBA 1: Fallo de os.replace()
with tempfile.TemporaryDirectory() as carpeta:
    ruta = os.path.join(carpeta, "inventario.txt")
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("INVENTARIO ORIGINAL\n")
    with patch("os.replace", side_effect=OSError("Fallo simulado")):
        resultado = guardar_inventario_seguro(ruta, inventario_valido)
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    assert resultado is False
    assert contenido == "INVENTARIO ORIGINAL\n"
    assert os.listdir(carpeta) == ["inventario.txt"]
    print("PRUEBA 1 SUPERADA")
# PRUEBA 2: Stock negativo
inventario_invalido = {
    "P001": {
        "nombre": "Teclado",
        "stock": -10,
        "precio": 45.50
    }
}
with tempfile.TemporaryDirectory() as carpeta:
    ruta = os.path.join(carpeta, "inventario.txt")
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("INVENTARIO ORIGINAL\n")
    with patch("tempfile.NamedTemporaryFile") as mock_temporal:
        with patch("os.replace") as mock_replace:
            resultado = guardar_inventario_seguro(ruta, inventario_invalido)
            mock_temporal.assert_not_called()
            mock_replace.assert_not_called()
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    assert resultado is None
    assert contenido == "INVENTARIO ORIGINAL\n"
    assert os.listdir(carpeta) == ["inventario.txt"]
    print("PRUEBA 2 SUPERADA")
# PRUEBA 3: Precio infinito
inventario_invalido = {
    "P001": {
        "nombre": "Teclado",
        "stock": 10,
        "precio": float("inf")
    }
}
with tempfile.TemporaryDirectory() as carpeta:
    ruta = os.path.join(carpeta, "inventario.txt")
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("INVENTARIO ORIGINAL\n")
    with patch("tempfile.NamedTemporaryFile") as mock_temporal:
        with patch("os.replace") as mock_replace:
            resultado = guardar_inventario_seguro(ruta, inventario_invalido)
            mock_temporal.assert_not_called()
            mock_replace.assert_not_called()
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    assert resultado is None
    assert contenido == "INVENTARIO ORIGINAL\n"
    assert os.listdir(carpeta) == ["inventario.txt"]
    print("PRUEBA 3 SUPERADA")
# PRUEBA 4: Códigos duplicados después de strip()
inventario_invalido = {
    "P001": {
        "nombre": "Teclado",
        "stock": 10,
        "precio": 45.50
    },
    " P001 ": {
        "nombre": "Mouse",
        "stock": 5,
        "precio": 25.00
    }
}
with tempfile.TemporaryDirectory() as carpeta:
    ruta = os.path.join(carpeta, "inventario.txt")
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("INVENTARIO ORIGINAL\n")
    with patch("tempfile.NamedTemporaryFile") as mock_temporal:
        with patch("os.replace") as mock_replace:
            resultado = guardar_inventario_seguro(ruta, inventario_invalido)
            mock_temporal.assert_not_called()
            mock_replace.assert_not_called()
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    assert resultado is None
    assert contenido == "INVENTARIO ORIGINAL\n"
    assert os.listdir(carpeta) == ["inventario.txt"]
    print("PRUEBA 4 SUPERADA")
# PRUEBA 5: Nombre con separador prohibido
inventario_invalido = {
    "P001": {
        "nombre": "Teclado;Mecanico",
        "stock": 10,
        "precio": 45.50
    }
}
with tempfile.TemporaryDirectory() as carpeta:
    ruta = os.path.join(carpeta, "inventario.txt")
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("INVENTARIO ORIGINAL\n")
    with patch("tempfile.NamedTemporaryFile") as mock_temporal:
        with patch("os.replace") as mock_replace:
            resultado = guardar_inventario_seguro(ruta, inventario_invalido)

            mock_temporal.assert_not_called()
            mock_replace.assert_not_called()
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    assert resultado is None
    assert contenido == "INVENTARIO ORIGINAL\n"
    assert os.listdir(carpeta) == ["inventario.txt"]
    print("PRUEBA 5 SUPERADA")
# PRUEBA 6: Fallo durante la escritura temporal
with tempfile.TemporaryDirectory() as carpeta:
    ruta = os.path.join(carpeta, "inventario.txt")
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("INVENTARIO ORIGINAL\n")
    # Simular un error al crear el temporal
    with patch(
        "tempfile.NamedTemporaryFile",
        side_effect=OSError("Fallo al crear temporal")
    ):
        with patch("os.replace") as mock_replace:
            resultado = guardar_inventario_seguro(
                ruta,
                inventario_valido
            )
            mock_replace.assert_not_called()
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    assert resultado is False
    assert contenido == "INVENTARIO ORIGINAL\n"
    assert os.listdir(carpeta) == ["inventario.txt"]
    print("PRUEBA 6 SUPERADA")