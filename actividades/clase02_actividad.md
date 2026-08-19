# Actividad de la clase 02

**INF-396 Introducción a la Ciencia de Datos**
Manipulación de datos con Pandas y análisis exploratorio

**Modalidad**: en parejas · **Duración**: segundo bloque, 16:05 a 17:15
**Entrega**: no se califica. Es una actividad para practicar y para revisar juntos al cierre.

## Antes de empezar

Trabajen sobre el archivo `datos/emisiones_aire_2020.csv`, el mismo del notebook de la
clase. Pueden partir de una copia del notebook `02_pandas_eda.ipynb` o abrir uno nuevo.

```python
import pandas as pd

emisiones = pd.read_csv("datos/emisiones_aire_2020.csv")
```

Escriban las respuestas en celdas de markdown, junto al código. No basta con el número:
lo que interesa es qué concluyen a partir de él.

## Parte 1. Conocer los datos

1. ¿Cuántas comunas distintas aparecen en el conjunto de datos? ¿Y cuántos
   establecimientos distintos?
2. ¿Cuántas filas hay por cada contaminante? ¿Están balanceados?
3. Revisen los valores faltantes. ¿En qué columnas están y cuántos son? Propongan una
   decisión sobre qué hacer con ellos, y justifíquenla en una frase.

## Parte 2. Filtrar y agrupar

4. Calculen el total de MP10 emitido por región. Comparen ese ranking con el de MP2,5
   que vimos en clase. ¿Cambian las primeras posiciones? ¿Se les ocurre por qué?
5. Obtengan los cinco establecimientos con mayores emisiones de SO2. ¿A qué rubro
   pertenecen? ¿Están concentrados en alguna región?
6. Para el rubro con más emisiones de MP2,5, calculen cuántos establecimientos lo
   componen y cuánto emite cada uno en promedio y en mediana.

## Parte 3. Elegir cómo resumir

7. Para las emisiones de MP10, calculen la media, la mediana y la media truncada al 10%.
8. Supongan que tienen que informar en una noticia "cuánto emite un establecimiento
   típico en Chile". ¿Qué número reportarían y por qué? Escriban dos o tres líneas
   defendiendo su elección.
9. Construyan un histograma de MP10 en escala logarítmica. Recuerden que los intervalos
   también deben ser logarítmicos.

## Parte 4. Para discutir al cierre

10. En la clase 01 hablamos de sesgo y de decisiones automatizadas. Si alguien usara
    estos datos para decidir dónde fiscalizar, ¿qué podría salir mal? Piensen en qué
    establecimientos quedan fuera del registro y en qué significa un dato faltante en
    este contexto.

## Si terminan antes

Exploren la relación entre `tipo_fuente` y las emisiones: ¿hay tipos de fuente que
concentren las emisiones más altas? ¿Y algún combustible en particular?
