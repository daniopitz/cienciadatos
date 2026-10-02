"""Descarga los dos datasets de la clase 6 (regresion logistica).

- default_islr.csv: 10.000 clientes de tarjeta de credito (default, student,
  balance, income), del libro An Introduction to Statistical Learning
  (James, Witten, Hastie y Tibshirani). Viene en el zip de datos de la
  segunda edicion, en https://www.statlearning.com/resources-second-edition
- titanic.csv: 891 pasajeros del Titanic, del repositorio de datos de
  ejemplo de seaborn, https://github.com/mwaskom/seaborn-data

Uso, desde la raiz del repositorio:
    uv run python datos/clase06/preparar_clase06.py
"""

import io
import urllib.request
import zipfile
from pathlib import Path

carpeta = Path(__file__).parent

ZIP_ISLR = "https://www.statlearning.com/s/ALL-CSV-FILES-2nd-Edition-corrected.zip"
with urllib.request.urlopen(ZIP_ISLR) as r:
    zf = zipfile.ZipFile(io.BytesIO(r.read()))
nombre = next(n for n in zf.namelist() if n.endswith("Default.csv"))
(carpeta / "default_islr.csv").write_bytes(zf.read(nombre))
print("Escrito: default_islr.csv")

URL_TITANIC = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
with urllib.request.urlopen(URL_TITANIC) as r:
    (carpeta / "titanic.csv").write_bytes(r.read())
print("Escrito: titanic.csv")
