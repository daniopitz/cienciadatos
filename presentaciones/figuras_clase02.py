"""Genera las figuras de la clase 02 a partir de los datos de emisiones.

Todas las figuras de las slides salen de este script, para que sean reproducibles:
si los datos cambian, se vuelve a correr y las imágenes se actualizan solas.

Uso:
    uv run python presentaciones/figuras_clase02.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

AZUL = "#4C72B0"
NARANJO = "#DD8452"

raiz = Path(__file__).parent.parent
carpeta = Path(__file__).parent / "figuras"
carpeta.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 150

emisiones = pd.read_csv(raiz / "datos" / "emisiones_aire_2020.csv")
mp25 = emisiones[emisiones["contaminante"] == "MP2,5"]
valores = mp25["cantidad_toneladas"].dropna()


def guardar(fig, nombre):
    ruta = carpeta / nombre
    fig.savefig(ruta, bbox_inches="tight")
    plt.close(fig)
    print(f"  {nombre}")


# Figura 1: el histograma sin transformar, que casi no se puede leer.
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.hist(valores, bins=50, color=AZUL)
ax.set_xlabel("Emisiones de MP2,5 (toneladas al año)")
ax.set_ylabel("Establecimientos")
ax.set_title("Casi todas las observaciones se apilan cerca de cero")
guardar(fig, "01_histograma_crudo.png")

# Figura 2: el mismo histograma en escala logarítmica. Los intervalos también tienen
# que ser logarítmicos, si no todas las observaciones caen en una sola barra.
positivos = valores[valores > 0]
intervalos = np.logspace(np.log10(positivos.min()), np.log10(positivos.max()), 40)
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.hist(positivos, bins=intervalos, color=AZUL)
ax.set_xscale("log")
ax.set_xlabel("Emisiones de MP2,5 (toneladas al año, escala logarítmica)")
ax.set_ylabel("Establecimientos")
ax.set_title("Con escala logarítmica aparece la forma real")
guardar(fig, "02_histograma_log.png")

# Figura 3: media contra mediana sobre el histograma, para mostrar por qué el
# promedio describe mal el caso típico.
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.hist(positivos, bins=intervalos, color=AZUL)
ax.set_xscale("log")
ax.axvline(valores.median(), color="#55A868", linewidth=2, label=f"Mediana: {valores.median():.3f} t")
ax.axvline(valores.mean(), color=NARANJO, linewidth=2, label=f"Media: {valores.mean():.3f} t")
ax.set_xlabel("Emisiones de MP2,5 (toneladas al año, escala logarítmica)")
ax.set_ylabel("Establecimientos")
ax.set_title("La media queda lejos de donde está la mayoría")
ax.legend()
guardar(fig, "03_media_vs_mediana.png")

# Figura 4: ranking de regiones.
por_region = (
    mp25.groupby("region")["cantidad_toneladas"].sum().sort_values(ascending=False)
)
top = por_region.head(8)
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.barh(top.index, top.values, color=AZUL)
ax.invert_yaxis()
ax.set_xlabel("Toneladas de MP2,5 emitidas en 2020")
ax.set_title("Ocho regiones con mayores emisiones de MP2,5")
guardar(fig, "04_regiones.png")

# Figura 5: distribución por macrozona.
macrozonas = pd.DataFrame(
    {
        "region": [
            "Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama", "Coquimbo",
            "Valparaíso", "Metropolitana", "Libertador Gral. Bernardo O'Higgins",
            "Maule", "Ñuble", "Biobío", "Araucanía", "Los Ríos", "Los Lagos",
            "Aysén del Gral. Carlos Ibáñez del Campo",
            "Magallanes y de la Antártica Chilena",
        ],
        "macrozona": [
            "Norte", "Norte", "Norte", "Norte", "Norte",
            "Centro", "Centro", "Centro", "Centro",
            "Sur", "Sur", "Sur", "Sur", "Sur",
            "Austral", "Austral",
        ],
    }
)
con_zona = mp25.merge(macrozonas, on="region", how="left")
con_zona = con_zona[con_zona["cantidad_toneladas"] > 0]

fig, ax = plt.subplots(figsize=(7, 3.6))
sns.boxplot(
    data=con_zona, x="macrozona", y="cantidad_toneladas",
    order=["Norte", "Centro", "Sur", "Austral"], ax=ax, color=AZUL,
)
ax.set_yscale("log")
ax.set_xlabel("Macrozona")
ax.set_ylabel("Toneladas al año (escala logarítmica)")
ax.set_title("Distribución de emisiones de MP2,5 por macrozona")
guardar(fig, "05_boxplot_macrozona.png")

print(f"\nFiguras guardadas en {carpeta}")
