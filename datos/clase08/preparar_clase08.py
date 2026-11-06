"""Descarga los datos de la clase 08 (aprendizaje supervisado y no supervisado).

- pinguinos_palmer.csv: 344 pinguinos de tres especies medidos en el archipielago
  Palmer, Antartida, entre 2007 y 2009 (Gorman, Williams y Fraser, 2014). Viene del
  paquete palmerpenguins (Horst, Hill y Gorman, 2020), con licencia CC0:
  https://github.com/allisonhorst/palmerpenguins

Las columnas y las categorias se traducen al espanol; los valores no se tocan.

Uso, desde la raiz del repositorio:
    uv run python datos/clase08/preparar_clase08.py
"""

import io
import urllib.request
from pathlib import Path

import pandas as pd

carpeta = Path(__file__).parent

URL = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
with urllib.request.urlopen(URL) as r:
    pinguinos = pd.read_csv(io.BytesIO(r.read()))

pinguinos = pinguinos.rename(columns={
    "species": "especie", "island": "isla", "bill_length_mm": "largo_pico_mm",
    "bill_depth_mm": "alto_pico_mm", "flipper_length_mm": "largo_aleta_mm",
    "body_mass_g": "masa_g", "sex": "sexo", "year": "anio"})
pinguinos["especie"] = pinguinos["especie"].map({"Adelie": "Adelia", "Chinstrap": "Barbijo", "Gentoo": "Papúa"})
pinguinos["sexo"] = pinguinos["sexo"].map({"female": "hembra", "male": "macho"})
for col in ["largo_aleta_mm", "masa_g"]:
    pinguinos[col] = pinguinos[col].astype("Int64")
pinguinos.to_csv(carpeta / "pinguinos_palmer.csv", index=False)
print("Escrito: pinguinos_palmer.csv,", len(pinguinos), "filas")
