# Datos de la clase 08: aprendizaje supervisado y no supervisado

| Archivo | Filas | Contenido | Origen |
|---|---|---|---|
| `pinguinos_palmer.csv` | 344 (342 con las cuatro medidas) | Pingüinos adultos de tres especies (Adelia, barbijo y papúa) medidos en tres islas del archipiélago Palmer, Antártida, entre 2007 y 2009: largo y alto del pico, largo de la aleta, masa corporal, sexo, isla y año. | Gorman, K. B., Williams, T. D. y Fraser, W. R. (2014). *Ecological sexual dimorphism and environmental variability within a community of Antarctic penguins (genus Pygoscelis)*. PLoS ONE, 9(3), e90081. Datos del paquete [palmerpenguins](https://github.com/allisonhorst/palmerpenguins) (Horst, Hill y Gorman, 2020), licencia CC0. |

La clase 08 también usa `datos/clase07/hitters_islr.csv`, los jugadores de béisbol de la clase 07, para el análisis de componentes principales.

## Columnas

| Columna | Qué mide |
|---|---|
| `especie` | Adelia, Barbijo o Papúa (en inglés, Adelie, Chinstrap y Gentoo) |
| `isla` | Biscoe, Dream o Torgersen |
| `largo_pico_mm` | largo del pico, en milímetros |
| `alto_pico_mm` | alto del pico (*bill depth*), en milímetros |
| `largo_aleta_mm` | largo de la aleta, en milímetros |
| `masa_g` | masa corporal, en gramos |
| `sexo` | hembra o macho; sin dato para 11 pingüinos |
| `anio` | año de la medición |

Dos pingüinos no tienen ninguna de las cuatro medidas; en la clase se dejan fuera.

El script `preparar_clase08.py` vuelve a descargar el archivo desde su origen y traduce las columnas y las categorías:

```bash
uv run python datos/clase08/preparar_clase08.py
```
