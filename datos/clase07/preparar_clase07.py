"""Descarga los datos de la clase 07 (regularizacion: Ridge y Lasso).

- hitters_islr.csv: jugadores de béisbol y su salario, del libro An Introduction
  to Statistical Learning (James, Witten, Hastie y Tibshirani). Viene en el zip de
  datos de la segunda edicion, en https://www.statlearning.com/resources-second-edition

Uso, desde la raiz del repositorio:
    uv run python datos/clase07/preparar_clase07.py
"""

import io
import urllib.request
import zipfile
from pathlib import Path

carpeta = Path(__file__).parent

ZIP_ISLR = "https://www.statlearning.com/s/ALL-CSV-FILES-2nd-Edition-corrected.zip"
with urllib.request.urlopen(ZIP_ISLR) as r:
    zf = zipfile.ZipFile(io.BytesIO(r.read()))
nombre = next(n for n in zf.namelist() if n.endswith("Hitters.csv"))
(carpeta / "hitters_islr.csv").write_bytes(zf.read(nombre))
print("Escrito: hitters_islr.csv")
