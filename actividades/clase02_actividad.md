# Actividad de la clase 02: parte el retrato de tu comuna

**INF-396 Introducción a la Ciencia de Datos**
**Modalidad**: en parejas · **Cuándo**: segundo bloque, 16:05 a 17:15
**Ojo**: esta actividad es la primera sesión de la **Tarea 1**. Lo que avancen hoy
queda en el mismo notebook que van a entregar el 10 de septiembre.

## Qué van a hacer

Cada pareja adopta una comuna del Gran Santiago y comienza a construir su **retrato
de movilidad** con la EOD 2012: quiénes viven ahí, cómo se mueven y en qué se
diferencian del resto de la ciudad.

El enunciado completo de la tarea está en
[`evaluaciones/tareas/tarea1_retrato_comuna.md`](../evaluaciones/tareas/tarea1_retrato_comuna.md).
Hoy corresponde la parte 1: el retrato numérico.

## Paso 0. Elegir la comuna

- Anoten su pareja y su comuna en el hilo de Aula de la Tarea 1. **Las comunas no se
  repiten entre parejas**: el que anota primero se la queda.
- Verifiquen que su comuna tenga datos suficientes: al menos 100 hogares encuestados.

```python
import pandas as pd

RUTA = "datos/eod_stgo/"
hogares = pd.read_csv(RUTA + "Hogares.csv", sep=";", decimal=",", low_memory=False)
hogares["Comuna"].value_counts()
```

## Paso 1. El tamaño de la muestra en su comuna

Filtren los hogares de su comuna y respondan: ¿cuántos hogares encuestados hay?
¿Cuántas personas viven en ellos? (necesitan un merge o un filtro sobre `personas`
usando los identificadores de hogar).

Anoten también la respuesta ponderada: ¿a cuántos hogares y personas de la ciudad
representan, según los factores de expansión?

## Paso 2. Quiénes viven ahí

Con las personas de su comuna:

- Distribución por sexo (con la tabla de códigos, no con el 1 y el 2).
- Edad: mediana, percentiles 25 y 75. Comparen con el Gran Santiago completo.

## Paso 3. Cuánto ganan los hogares

- Ingreso mediano de los hogares de su comuna, comparado con el de todo Santiago.
- Reporten también la media y expliquen en una frase cuál de las dos usarían y por qué.

## Paso 4. Cómo se mueven

- Viajes por persona en su comuna, **incluyendo a quienes no viajaron**.
- Duración mediana de los viajes con origen en su comuna (`ComunaOrigen` en
  `viajes.csv` viene codificada: revisen `tablas_parametros/`).

## Cierre de la sesión (últimos 10 minutos)

Escriban en una celda de markdown los **tres números que mejor retratan a su comuna**
hasta ahora, y una frase que responda: ¿de quién hablan esos números? ¿De su muestra,
de su comuna, de la ciudad?

## Si terminan antes

Comparen el reparto modal de su comuna (con qué medios se mueve la gente) contra el
de todo Santiago, ponderado por factor de expansión, como hicimos en la clase.
