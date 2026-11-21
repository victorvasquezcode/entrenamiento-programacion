import os
from pathlib import Path
from tempfile import NamedTemporaryFile


def guardar_seguro(ruta, lineas):
    if type(lineas) is not list or any(type(linea) is not str for linea in lineas):
        return False

    destino = Path(ruta).absolute()
    temporal = None
    try:
        with NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=destino.parent, delete=False
        ) as archivo:
            temporal = archivo.name
            for linea in lineas:
                archivo.write(linea if linea.endswith("\n") else linea + "\n")
        os.replace(temporal, destino)
        temporal = None
        return True
    except (OSError, UnicodeError):
        return False
    finally:
        if temporal is not None:
            try:
                os.unlink(temporal)
            except OSError:
                pass
