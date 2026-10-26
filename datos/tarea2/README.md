# Datos de la Tarea 2

| Archivo | Filas | Contenido | Origen |
|---|---|---|---|
| `viviendas_california.csv` | 20.640 | Zonas censales de California según el censo de 1990. Ocho variables por zona y el precio mediano de sus viviendas. | Pace, R. K. y Barry, R. (1997), *Sparse Spatial Autoregressions*, Statistics and Probability Letters, 33, 291 a 297. Distribuido por scikit-learn (`fetch_california_housing`). |
| `tumores_wisconsin.csv` | 569 | Tumores de mama con 30 medidas del núcleo celular, tomadas de una imagen digitalizada de una punción, y el diagnóstico: 212 malignos y 357 benignos. | Street, W. N., Wolberg, W. H. y Mangasarian, O. L. (1993), *Nuclear feature extraction for breast tumor diagnosis*, IS&T/SPIE. Repositorio UCI, Breast Cancer Wisconsin (Diagnostic). Distribuido por scikit-learn (`load_breast_cancer`). |

## Viviendas de California

Una fila es una zona censal (un *block group*, la unidad más chica del censo de Estados
Unidos, de 600 a 3.000 personas). Las columnas:

| Columna | Qué mide |
|---|---|
| `ingreso_mediano` | ingreso mediano de los hogares de la zona, en decenas de miles de dólares |
| `antiguedad_mediana` | antigüedad mediana de las viviendas, en años |
| `piezas_promedio` | piezas por vivienda, en promedio |
| `dormitorios_promedio` | dormitorios por vivienda, en promedio |
| `poblacion` | personas que viven en la zona |
| `ocupantes_promedio` | personas por vivienda, en promedio |
| `latitud`, `longitud` | ubicación de la zona |
| `precio_mediano` | precio mediano de las viviendas, en cientos de miles de dólares; es la respuesta |

Dos detalles del dato original: el precio está truncado en 5,0 (500 mil dólares), así
que las zonas más caras aparecen todas con ese valor, y algunas zonas tienen promedios
de piezas u ocupantes muy altos porque corresponden a lugares con pocas viviendas.

## Tumores de Wisconsin

Una fila es un tumor. Para cada uno se midieron diez características de los núcleos
celulares (radio, textura, perímetro, área, suavidad, compacidad, concavidad, puntos
cóncavos, simetría y dimensión fractal) y de cada una se guardó la media (`mean_`), el
error estándar (`_error`) y el valor más alto (`worst_`), lo que da 30 columnas. La
columna `diagnostico` vale `maligno` o `benigno`.

El script `preparar_tarea2.py` vuelve a generar los dos archivos desde scikit-learn:

```bash
uv run python datos/tarea2/preparar_tarea2.py
```
