import os
from pathlib import Path
from tempfile import NamedTemporaryFile


def escribir_texto_seguro(ruta, lineas):
    """Escribe todas las líneas antes de reemplazar el destino."""
    destino = Path(ruta).absolute()
    temporal = None
    try:
        with NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=destino.parent, delete=False
        ) as archivo:
            temporal = archivo.name
            archivo.writelines(lineas)
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
