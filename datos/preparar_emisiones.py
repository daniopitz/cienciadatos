"""Prepara el dataset de emisiones al aire que usamos en la clase 02.

Descarga el Registro Único de Emisiones Atmosféricas (RUEA) de fuentes puntuales,
año 2020, publicado por el Ministerio del Medio Ambiente, y guarda un subconjunto
manejable en emisiones_aire_2020.csv.

Fuente: Registro de Emisiones y Transferencias de Contaminantes (RETC),
Ministerio del Medio Ambiente. https://datosretc.mma.gob.cl

Uso:
    uv run python datos/preparar_emisiones.py
"""

import ssl
import urllib.request
from pathlib import Path

import certifi
import pandas as pd

# En macOS es habitual que Python no encuentre los certificados del sistema y la
# descarga falle con un error de SSL. Usamos el paquete certifi, que trae su propia
# lista de autoridades certificadoras.
contexto = ssl.create_default_context(cafile=certifi.where())
urllib.request.install_opener(
    urllib.request.build_opener(urllib.request.HTTPSHandler(context=contexto))
)

URL = (
    "https://datosretc.mma.gob.cl/dataset/2733b0f0-428a-4594-afeb-17780c8d47c1/"
    "resource/9101859d-555f-48ad-becc-caf3aacd03f2/download/ruea-efp-2020-ckan.csv"
)

# Nos quedamos con los contaminantes de los planes de descontaminación atmosférica.
CONTAMINANTES = ["MP2,5", "MP10", "Dióxido de azufre (SO2)"]

COLUMNAS = [
    "año",
    "razon_social",
    "nombre_establecimiento",
    "rubro_vu",
    "region",
    "provincia",
    "comuna",
    "latitud",
    "longitud",
    "tipo_fuente",
    "combustible_primario",
    "contaminante",
    "cantidad_toneladas",
]

NOMBRES = {
    "razon_social": "empresa",
    "nombre_establecimiento": "establecimiento",
    "rubro_vu": "rubro",
}

salida = Path(__file__).parent / "emisiones_aire_2020.csv"

print("Descargando el archivo original (unos 118 MB), esto puede demorar...")
datos = pd.read_csv(
    URL,
    sep=";",
    encoding="utf-8-sig",
    decimal=",",
    low_memory=False,
    usecols=COLUMNAS,
)
print(f"El archivo original tiene {len(datos):,} filas.")

# Varias columnas de texto traen espacios al inicio o al final, por ejemplo "NOx ".
# Si no se limpian, los filtros y los groupby fallan sin avisar.
for columna in datos.select_dtypes(include="str").columns:
    datos[columna] = datos[columna].str.strip()

# La columna de toneladas viene como texto por dos razones: usa coma decimal y marca
# los datos faltantes con un guion. La dejamos numerica, con los faltantes como NaN.
datos["cantidad_toneladas"] = pd.to_numeric(
    datos["cantidad_toneladas"].astype("string").str.replace(",", ".", regex=False),
    errors="coerce",
)

emisiones = datos[datos["contaminante"].isin(CONTAMINANTES)].copy()
emisiones = emisiones.rename(columns=NOMBRES)
emisiones = emisiones[
    [
        "año",
        "empresa",
        "establecimiento",
        "rubro",
        "region",
        "provincia",
        "comuna",
        "latitud",
        "longitud",
        "tipo_fuente",
        "combustible_primario",
        "contaminante",
        "cantidad_toneladas",
    ]
]

emisiones.to_csv(salida, index=False, encoding="utf-8")
print(f"Guardadas {len(emisiones):,} filas en {salida.name}")
print(emisiones["contaminante"].value_counts().to_string())
