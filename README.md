# INF-396 Introducción a la Ciencia de Datos

Universidad Técnica Federico Santa María, Departamento de Informática.
Segundo semestre 2026. Clases los **viernes de 14:40 a 17:15**, en dos bloques de 70
minutos con un recreo de 15. Primera clase: viernes 7 de agosto.

Cuatro viernes sin clases: 14 de agosto (Días Sansanos), 11 y 18 de septiembre
(actividades de Fiestas Patrias y vacaciones) y 16 de octubre (Puertas Abiertas).
Las suspensiones rigen desde las 12:30, así que alcanzan a este curso. Referencia:
[calendario académico oficial USM 2026](https://vra.usm.cl/calendario-academico/).

Material basado en el programa oficial INF-396 (ver `programa/`).

## Evaluación

`NF = 0,1·Q + 0,1·T + 0,5·promedio(C1, C2) + 0,3·P`

| Ítem | Ponderación | Fechas | Detalle |
|------|-------------|--------|---------|
| Controles de lectura (Q) | 10% | **21-ago** (Q1) · resto por confirmar | 4 controles, al inicio de la clase, duración 15 a 20 minutos |
| Tareas (T) | 10% | entregas: **10-sep · 9-oct · 30-oct · 20-nov** | 4 tareas en parejas, sobre datos reales; gran parte se desarrolla en clase, en el bloque práctico |
| Certámenes (C) | 50% | **2-oct · 27-nov** | promedio de C1 y C2; escritos e individuales |
| Proyecto final (P) | 30% | **25-sep · 6-nov · 4-dic** | en grupo; propuesta, avance y presentación + informe |

### Calendario de evaluaciones

Salvo la entrega de T1, que es un jueves y se hace por Aula, todas las fechas son
viernes en el horario de clases. Aquí van solo las evaluaciones formales. Los enunciados de las tareas se publican por Aula y no figuran aquí como
hito: lo que cuenta es la fecha de entrega.

Las fechas de los certámenes, la propuesta y la presentación del proyecto son firmes.
Los controles Q2 a Q4 y las entregas de tareas se ajustan sobre la marcha: se confirman
en clase y por Aula, a más tardar una semana antes.

| Fecha | Evaluación | Estado | Detalle |
|-------|------------|--------|---------|
| vie 21-ago | **Control Q1** | ✅ Confirmado | O'Neil, *Armas de destrucción matemática*, Introducción + Cap. 1 |
| vie 28-ago | Hito proyecto | ✅ | Se forman los grupos |
| vie 04-sep | **Control Q2** | *Tentativo* | Lectura por definir |
| **jue 10-sep** | **Entrega T1** | ✅ Confirmado | Exploración de datos. Se entrega por Aula, antes de las actividades de Fiestas Patrias |
| vie 25-sep | **Propuesta de proyecto** | ✅ Confirmado | Obligatoria: pregunta, datos y plan de trabajo |
| vie 02-oct | **Certamen 1** | ✅ Confirmado | Unidades 1 a 5, incluida la regresión lineal · certamen escrito, individual |
| vie 09-oct | **Entrega T2** | *Tentativo* | |
| vie 23-oct | **Control Q3** | *Tentativo* | Lectura por definir |
| vie 30-oct | **Entrega T3** | *Tentativo* | |
| vie 06-nov | Avance de proyecto *(opcional)* | ✅ | Quienes lo presenten parten con 10 puntos de base |
| vie 13-nov | **Control Q4** | *Tentativo* | Lectura por definir |
| vie 20-nov | **Entrega T4** | *Tentativo* | |
| vie 27-nov | **Certamen 2** | ✅ Confirmado | Unidades 6 a 9 · certamen escrito, individual |
| vie 04-dic | **Presentación del proyecto + informe** | ✅ Confirmado | |

## Reglas del curso

- **Trabajo en grupo**: las tareas y el proyecto se hacen en parejas (o grupos pequeños).
  Los certámenes son individuales.
- **Entrega de tareas**: se entrega el notebook ejecutado; debe correr de principio a fin en
  el entorno del curso (`uv sync`).
- **Atrasos**: se aceptan con descuento de **10 puntos por día** (escala 0 a 100), hasta un
  máximo de **3 días**. Después de eso, la tarea se califica con nota mínima.
- **Uso de IA generativa (ChatGPT, Copilot, etc.)**: **permitida, con declaración**. Al entregar,
  indiquen qué herramienta usaron y para qué (una línea basta). Deben **entender y poder explicar
  cualquier línea de su código**: en clase se puede preguntar.

## Planificación semana a semana

Las 9 unidades temáticas del programa oficial INF-396, distribuidas en 13 sesiones
más la presentación del proyecto.

Cuatro viernes sin clases, porque las suspensiones empiezan a las 12:30 y el curso es
a las 14:40: **14 de agosto** (Días Sansanos), **11 y 18 de septiembre** (actividades
de Fiestas Patrias y vacaciones) y **16 de octubre** (Puertas Abiertas). El contenido
del 14 de agosto se junta con la clase del 21, el del 11 de septiembre con la del 4, y
el del 16 de octubre con la del 23.

Para no sobrecargar la clase del 21 (que además tiene el control Q1), el análisis
exploratorio se reparte entre el **21 y el 28 de agosto**: se avanza lo que se alcance
el 21 y se retoma el 28, antes de entrar a visualización.

Los enlaces se van publicando a medida que avanza el semestre.

| Clase | Fecha | Unidad (programa) | Contenidos | Slides | Notebook | Evaluaciones e hitos |
|-------|-------|-------------------|------------|--------|----------|----------------------|
| 01 | vie 07-ago | U1. Fundamentos y ética | Qué es la ciencia de datos; reglas del curso; IA responsable | [pdf](presentaciones/clase01_ia_responsable.pdf) · [pptx](presentaciones/clase01_ia_responsable.pptx) | - | Se publica lectura de Q1 |
| - | vie 14-ago | *Sin clases (Días Sansanos)* | | | | |
| 02 | vie 21-ago | Herramientas + U2. Análisis exploratorio *(parte 1)* | Pandas: selección, filtros, groupby y merge · Inicio de EDA: estadística descriptiva | [pdf](presentaciones/clase02_pandas_eda.pdf) · [pptx](presentaciones/clase02_pandas_eda.pptx) | [ipynb](02_pandas_eda.ipynb) | **Control Q1** (15 a 20 min): O'Neil, *Armas de destrucción matemática*, Introducción + Cap. 1 |
| 03 | vie 28-ago | U2. Análisis exploratorio *(parte 2)* + U4. Visualización | EDA: métodos gráficos · Matplotlib y Seaborn; datos multivariados; buenas prácticas | - | - | **Se forman los grupos de proyecto** |
| 04 | vie 04-sep | U3. Pre-procesamiento y reducción de dimensión | Limpieza, imputación, outliers, transformaciones · Selección de características; PCA; métodos no lineales: t-SNE y UMAP | - | - | Avance mínimo T1 · **Control Q2** (lectura por definir) |
| - | vie 11-sep | *Sin clases (actividades de Fiestas Patrias)* | | | | **Entrega T1** el jueves 10 de septiembre, por Aula |
| - | vie 18-sep | *Vacaciones (14 al 18 de septiembre)* | | | | |
| 05 | vie 25-sep | U5. Inferencia estadística y ajuste de modelos | Estimación, intervalos, contraste de hipótesis, bootstrap · Regresión lineal múltiple | - | - | **Entrega propuesta de proyecto** (de vuelta de vacaciones) |
| 06 | vie 02-oct | Certamen | **Certamen 1** (unidades 1 a 5, incluida la regresión lineal) | | | |
| 07 | vie 09-oct | U8. Sesgo, varianza y regularización | Interpretación de coeficientes y diagnóstico del ajuste · Dilema entre sesgo y varianza · Regularización: ridge y lasso | - | - | **Entrega T2** |
| - | vie 16-oct | *Sin clases (Puertas Abiertas, 14 al 17 de octubre)* | | | | |
| 08 | vie 23-oct | U6. Aprendizaje automático + U7. Clasificación | Tipos de aprendizaje: supervisado, no supervisado y bayesiano; función de pérdida; minimización del riesgo esperado · Regresión logística; análisis discriminante lineal (LDA); KNN | - | - | **Control Q3** (lectura por definir) |
| 09 | vie 30-oct | U8. Evaluación de modelos | Validación cruzada; bootstrap; métricas de desempeño; equidad entre grupos | - | - | **Entrega T3** |
| 10 | vie 06-nov | U6. No supervisado | Clustering: k-means y jerárquico | - | - | **Avance de proyecto (opcional)**: quienes lo presenten parten con 10 puntos de base y reciben retroalimentación |
| 11 | vie 13-nov | U9. Máquinas de soporte vectorial | SVM en clasificación de 2 o más clases; kernels | - | - | **Control Q4** (lectura por definir) |
| 12 | vie 20-nov | U9. Redes neuronales | Redes neuronales artificiales en clasificación | - | - | **Entrega T4** |
| 13 | vie 27-nov | Certamen | **Certamen 2** (unidades 6 a 9) | | | |
| - | vie 04-dic | Proyecto | **Presentaciones del proyecto final** + entrega del informe | | | |

### Estructura de cada clase (14:40 a 17:15)

| Bloque | Horario | Contenido |
|--------|---------|-----------|
| 1 | 14:40 a 15:50 | Control de lectura (semanas con control) o repaso de la clase anterior, y teoría (slides en `presentaciones/`) |
| Recreo | 15:50 a 16:05 | |
| 2 | 16:05 a 17:15 | Actividad guiada en notebook, en parejas (`actividades/`); aquí se avanza gran parte de las tareas |

Son 140 minutos de clase efectivos, repartidos en dos bloques de 70.

### Lecturas de los controles

Detalle y enlaces en [`lecturas/README.md`](lecturas/README.md). Resumen:

- **Q1 (21-ago):** O'Neil, *Armas de destrucción matemática*, Introducción + Capítulo 1.
- **Q2 (04-sep)**: por definir.
- **Q3 (23-oct)**: por definir.
- **Q4 (13-nov)**: por definir.

Solo la lectura de Q1 está definida. Las otras tres se anuncian en clase y por Aula a
más tardar una semana antes de cada control.

### Proyecto final

En grupos, sobre un problema y datos elegidos por el grupo (se sugieren datos chilenos).

- **Grupos**: se forman el 28 de agosto.
- **Propuesta** (obligatoria): se entrega el **25 de septiembre**, de vuelta de las
  vacaciones. Pregunta, datos y plan de trabajo.
- **Avance** (opcional): el **6 de noviembre**. No es obligatorio; los grupos que lo
  presenten **parten con 10 puntos de base** (escala 0 a 100) en la nota del proyecto
  y reciben retroalimentación para la entrega final.
- **Presentación e informe**: el **4 de diciembre**. El informe debe explicar qué hace
  el modelo, para qué sirve, dónde falla y a quién podría perjudicar.

## Entorno

Requiere [uv](https://docs.astral.sh/uv/):

```bash
uv sync
uv run jupyter lab
```

## Estructura del repositorio

```
NN_tema.ipynb        notebook de cada clase, en la raíz
presentaciones/      slides: claseNN_tema.pptx y claseNN_tema.pdf
actividades/         enunciados y soluciones de las actividades en clase
evaluaciones/
  tareas/            enunciados de T1 a T4
  controles/         enunciados de Q1 a Q4
  certamenes/        enunciados de C1 y C2
  rubricas/          pautas de corrección
  proyecto/          pauta y formato de propuesta
lecturas/            lecturas de los controles (ver lecturas/README.md)
datos/               datasets del curso (ver datos/README.md)
programa/            programa oficial de la asignatura
```

El material se agrupa por tipo y no por clase, porque buena parte no pertenece a
una sola clase: los datasets se reutilizan, las lecturas están amarradas a los
controles y las tareas cruzan varias semanas. La navegación por clase se hace desde
la tabla de planificación de más arriba, que enlaza directo a cada archivo.

Las actividades quedan fuera de `evaluaciones/` a propósito: son formativas, se
trabajan en el bloque práctico y no se califican por separado.

## Bibliografía

### Bibliografía del programa

- James, G., Witten, D., Hastie, T. y Tibshirani, R. *An Introduction to Statistical
  Learning: with Applications in R*. Springer. Usamos la edición equivalente en Python,
  *An Introduction to Statistical Learning: with Applications in Python* (2023), de
  descarga gratuita en https://www.statlearning.com
- Saltz, J. S. y Stanton, J. M. (2018). *An Introduction to Data Science*. SAGE
  Publications, primera edición.
- Ozdemir, S. (2016). *Principles of Data Science*. Packt Publishing.
- García, S., Luengo, J. y Herrera, F. (2015). *Data Preprocessing in Data Mining*.
  Springer.

### Bibliografía adicional

- Bruce, P., Bruce, A. y Gedeck, P. (2020). *Practical Statistics for Data Scientists:
  50+ Essential Concepts Using R and Python*, 2ª ed. O'Reilly. Capítulo 1, "Exploratory
  Data Analysis". Notebooks en Python de acceso libre en
  https://github.com/gedeck/practical-statistics-for-data-scientists
- VanderPlas, J. (2016). *Python Data Science Handbook: Essential Tools for Working
  with Data*. O'Reilly. https://jakevdp.github.io/PythonDataScienceHandbook/
- O'Neil, C. (2017). *Armas de destrucción matemática: cómo el Big Data aumenta la
  desigualdad y amenaza la democracia*. Capitán Swing. Lectura del control Q1.
- Russell, S. y Norvig, P. (2021). *Artificial Intelligence: A Modern Approach*, 4ª ed.
  Pearson. Capítulo 1.
