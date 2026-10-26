"""Prepara los datos de la Tarea 2 (regularizacion y clasificacion con costos).

- viviendas_california.csv: 20.640 zonas censales de California (censo de 1990), con
  8 variables y el precio mediano de las viviendas en cientos de miles de dolares.
  Viene en scikit-learn (fetch_california_housing), que lo descarga desde StatLib.
- tumores_wisconsin.csv: 569 tumores de mama con 30 medidas tomadas de una imagen
  digitalizada y el diagnostico (maligno o benigno). Viene en scikit-learn
  (load_breast_cancer); el original es del repositorio UCI (Breast Cancer Wisconsin,
  Diagnostic).

Uso, desde la raiz del repositorio:
    uv run python datos/tarea2/preparar_tarea2.py
"""

from pathlib import Path

import pandas as pd
from sklearn.datasets import fetch_california_housing, load_breast_cancer

carpeta = Path(__file__).parent

# 1. Viviendas de California. Los nombres de las columnas en espanol.
casas = fetch_california_housing(as_frame=True)
viviendas = casas.frame.rename(columns={
    "MedInc": "ingreso_mediano",        # ingreso mediano del hogar, en decenas de miles de dolares
    "HouseAge": "antiguedad_mediana",   # antiguedad mediana de las viviendas, en anios
    "AveRooms": "piezas_promedio",      # piezas por vivienda
    "AveBedrms": "dormitorios_promedio",
    "Population": "poblacion",          # personas en la zona
    "AveOccup": "ocupantes_promedio",   # personas por vivienda
    "Latitude": "latitud",
    "Longitude": "longitud",
    "MedHouseVal": "precio_mediano",    # precio mediano de las viviendas, en cientos de miles de dolares
})
viviendas.to_csv(carpeta / "viviendas_california.csv", index=False)
print("Escrito: viviendas_california.csv", viviendas.shape)

# 2. Tumores de Wisconsin. scikit-learn codifica maligno como 0 y benigno como 1;
#    aqui el diagnostico va en palabras y la respuesta de la tarea es maligno = 1.
cancer = load_breast_cancer(as_frame=True)
tumores = cancer.frame.copy()
tumores["diagnostico"] = tumores["target"].map({0: "maligno", 1: "benigno"})
tumores = tumores.drop(columns="target")
tumores.columns = [c.replace(" ", "_") for c in tumores.columns]
tumores.to_csv(carpeta / "tumores_wisconsin.csv", index=False)
print("Escrito: tumores_wisconsin.csv", tumores.shape, tumores["diagnostico"].value_counts().to_dict())
