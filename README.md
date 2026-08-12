# INF-396 Introducción a la Ciencia de Datos

Universidad Técnica Federico Santa María, Departamento de Informática.
Segundo semestre 2026. Clases los viernes, 2 horas. Primera clase: viernes 7 de agosto.
Sin clases el 14 de agosto (Días Sansanos) ni el 18 de septiembre (vacaciones de
Fiestas Patrias). Fechas según el [calendario académico oficial USM 2026](https://vra.usm.cl/calendario-academico/).

Material basado en el programa oficial INF-396 (ver `programa/`). El texto guía es
*An Introduction to Statistical Learning*; las primeras unidades se apoyan en otras
fuentes, porque el texto guía no las cubre (ver [Bibliografía](#bibliografía)).

## Evaluación

`NF = 0,1·Q + 0,1·T + 0,5·promedio(C1, C2) + 0,3·P`

| Ítem | Ponderación | Fechas | Detalle |
|------|-------------|--------|---------|
| Controles de lectura (Q) | 10% | **21-ago** (Q1) · resto por confirmar | 4 controles, al inicio de la clase, duración 15 a 20 minutos |
| Tareas (T) | 10% | entregas: **11-sep · 9-oct · 30-oct · 20-nov** | 4 tareas en parejas, sobre datos reales; gran parte se desarrolla en clase, en el bloque práctico |
| Certámenes (C) | 50% | **2-oct · 27-nov** | promedio de C1 y C2, individuales |
| Proyecto final (P) | 30% | **25-sep · 6-nov · 4-dic** | en grupo; propuesta, avance y presentación + informe con ficha del modelo |

### Calendario de evaluaciones

Todas las fechas son viernes, en el horario de clases. Aquí van solo las evaluaciones
formales. Los enunciados de las tareas se publican por Aula y no figuran aquí como
hito: lo que cuenta es la fecha de entrega.

Las fechas de los certámenes, la propuesta y la presentación del proyecto son firmes.
Los controles Q2 a Q4 y las entregas de tareas se ajustan sobre la marcha: se confirman
en clase y por Aula, a más tardar una semana antes.

| Fecha | Evaluación | Estado | Detalle |
|-------|------------|--------|---------|
| vie 21-ago | **Control Q1** | ✅ Confirmado | O'Neil, *Armas de destrucción matemática*, Introducción + Cap. 1 |
| vie 28-ago | Hito proyecto | ✅ | Se forman los grupos |
| vie 04-sep | **Control Q2** | *Tentativo* | Q2: *Datasheets for Datasets* |
| vie 11-sep | **Entrega T1** | *Tentativo* | Exploración de datos. Última clase antes de las vacaciones |
| vie 25-sep | **Propuesta de proyecto** | ✅ Confirmado | Obligatoria: pregunta, datos y plan de trabajo |
| vie 02-oct | **Certamen 1** | ✅ Confirmado | Unidades 1 a 5 · individual, sin IA |
| vie 09-oct | **Entrega T2** | *Tentativo* | |
| vie 23-oct | **Control Q3** | *Tentativo* | *Model Cards* |
| vie 30-oct | **Entrega T3** | *Tentativo* | |
| vie 06-nov | Avance de proyecto *(opcional)* | ✅ | Quienes lo presenten parten con 10 puntos de base |
| vie 13-nov | **Control Q4** | *Tentativo* | Q4: paper aplicado, por definir |
| vie 20-nov | **Entrega T4** | *Tentativo* | |
| vie 27-nov | **Certamen 2** | ✅ Confirmado | Unidades 6 a 9 · individual, sin IA |
| vie 04-dic | **Presentación del proyecto + informe** | ✅ Confirmado | Con ficha del modelo |

## Reglas del curso

- **Trabajo en grupo**: las tareas y el proyecto se hacen en parejas (o grupos pequeños).
  Los certámenes son individuales.
- **Entrega de tareas**: se entrega el notebook ejecutado; debe correr de principio a fin en
  el entorno del curso (`uv sync`).
- **Atrasos**: se aceptan con descuento de **10 puntos por día** (escala 0 a 100), hasta un
  máximo de **3 días**. Después de eso, la tarea se califica con nota mínima.
- **Uso de IA generativa (ChatGPT, Copilot, etc.)**: **permitida, con declaración**. Al entregar,
  indiquen qué herramienta usaron y para qué (una línea basta). Deben **entender y poder explicar
  cualquier línea de su código**: en clase se puede preguntar. Los certámenes son sin IA.

## Planificación semana a semana

Las 9 unidades temáticas del programa oficial INF-396, distribuidas en 15 sesiones
más la presentación del proyecto.

Dos viernes sin clases: **14 de agosto** (Días Sansanos) y **18 de septiembre**
(Fiestas Patrias). El contenido del 14 de agosto se junta con la clase del 21.

Para no sobrecargar la clase del 21 (que además tiene el control Q1), el análisis
exploratorio se reparte entre el **21 y el 28 de agosto**: se avanza lo que se alcance
el 21 y se retoma el 28, antes de entrar a visualización.

Los enlaces se van publicando a medida que avanza el semestre.

| Clase | Fecha | Unidad (programa) | Contenidos | Slides | Notebook | Evaluaciones e hitos |
|-------|-------|-------------------|------------|--------|----------|----------------------|
| 01 | vie 07-ago | U1. Fundamentos y ética | Qué es la ciencia de datos; reglas del curso; IA responsable; marco legal (Ley 21.719, AI Act) | [pdf](presentaciones/clase01_ia_responsable.pdf) · [pptx](presentaciones/clase01_ia_responsable.pptx) | - | Se publica lectura de Q1 |
| - | vie 14-ago | *Sin clases (Días Sansanos)* | | | | |
| 02 | vie 21-ago | Herramientas + U2. Análisis exploratorio *(parte 1)* | Manipulación de datos con Pandas: DataFrames, indexación, selección, groupby, merge · Inicio de EDA: estadística descriptiva | - | - | **Control Q1** (15 a 20 min): O'Neil, *Armas de destrucción matemática*, Introducción + Cap. 1 |
| 03 | vie 28-ago | U2. Análisis exploratorio *(parte 2)* + U4. Visualización | EDA: métodos gráficos · Matplotlib y Seaborn; datos multivariados; buenas prácticas | - | - | **Se forman los grupos de proyecto** |
| 04 | vie 04-sep | U3. Pre-procesamiento | Limpieza, imputación, outliers, transformaciones | - | - | Avance mínimo T1 (revisión en clase) · **Control Q2** *(lectura tentativa)*: *Datasheets for Datasets* (Gebru et al., 2021) |
| 05 | vie 11-sep | U3. Reducción de dimensión | Selección de características; PCA; métodos no lineales: t-SNE y UMAP | - | - | **Entrega T1**: exploración de datos · última clase antes de las vacaciones (14 al 18 de septiembre) |
| - | vie 18-sep | *Vacaciones (14 al 18 de septiembre)* | | | | |
| 06 | vie 25-sep | U5. Inferencia estadística | Estimación, intervalos, contraste de hipótesis, bootstrap | - | - | **Entrega propuesta de proyecto** (de vuelta de vacaciones) |
| 07 | vie 02-oct | Certamen | **Certamen 1** (unidades 1 a 5) | | | |
| 08 | vie 09-oct | U6. Aprendizaje automático | Tipos de aprendizaje: supervisado, no supervisado y bayesiano; función de pérdida; minimización del riesgo esperado; API de scikit-learn | - | - | **Entrega T2** |
| 09 | vie 16-oct | U7. Clasificación *(parte 1)* | Regresión lineal múltiple | - | - | ⚠️ **Puertas Abiertas**: actividades suspendidas desde las 12:30 |
| 10 | vie 23-oct | U7. Clasificación *(parte 2)* | Regresión logística; análisis discriminante lineal (LDA); KNN | - | - | **Control Q3** *(lectura tentativa)*: *Model Cards* (Mitchell et al., 2019) |
| 11 | vie 30-oct | U8. Evaluación de modelos | Sesgo y varianza; validación cruzada; bootstrap; métricas de desempeño; regularización (ridge y lasso); equidad entre grupos | - | - | **Entrega T3** |
| 12 | vie 06-nov | U6. No supervisado | Clustering: k-means y jerárquico | - | - | **Avance de proyecto (opcional)**: quienes lo presenten parten con 10 puntos de base y reciben retroalimentación |
| 13 | vie 13-nov | U9. Máquinas de soporte vectorial | SVM en clasificación de 2 o más clases; kernels | - | - | **Control Q4** *(lectura tentativa)*: paper aplicado, por definir |
| 14 | vie 20-nov | U9. Redes neuronales | Redes neuronales artificiales en clasificación | - | - | **Entrega T4** |
| 15 | vie 27-nov | Certamen | **Certamen 2** (unidades 6 a 9) | | | |
| - | vie 04-dic | Proyecto | **Presentaciones del proyecto final** + entrega del informe | | | |

### Estructura de cada clase (2 horas)

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| Inicio | 15 a 20 min (solo semanas con control) o 10 min de repaso | Control de lectura o repaso de la clase anterior |
| Teoría | 50 min | Presentación (slides en `presentaciones/`) |
| Práctica | 45 a 50 min | Actividad guiada en notebook, en parejas (`actividades/`); aquí se avanza gran parte de las tareas |

### Lecturas de los controles

Detalle y enlaces en [`lecturas/README.md`](lecturas/README.md). Resumen:

- **Q1 (21-ago):** O'Neil, *Armas de destrucción matemática*, Introducción + Capítulo 1.
- **Q2 (04-sep)** *(tentativa)*: Gebru et al. (2021), *Datasheets for Datasets*, CACM.
- **Q3 (23-oct)** *(tentativa)*: Mitchell et al. (2019), *Model Cards for Model Reporting*, FAT*.
- **Q4 (13-nov)** *(tentativa)*: artículo aplicado, por definir según los intereses del grupo.

Solo Q1 está confirmada. Las demás pueden cambiar; se confirman a más tardar una semana
antes de cada control.

### Proyecto final

En grupos, sobre un problema y datos elegidos por el grupo (se sugieren datos chilenos).

- **Grupos**: se forman el 28 de agosto.
- **Propuesta** (obligatoria): se entrega el **25 de septiembre**, de vuelta de las
  vacaciones. Pregunta, datos y plan de trabajo.
- **Avance** (opcional): el **6 de noviembre**. No es obligatorio; los grupos que lo
  presenten **parten con 10 puntos de base** (escala 0 a 100) en la nota del proyecto
  y reciben retroalimentación para la entrega final.
- **Presentación e informe**: el **4 de diciembre**. El informe debe incluir una
  **ficha del modelo** (model card simplificada): qué hace, para qué sirve, dónde falla
  y a quién podría perjudicar.

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
  proyecto/          pauta, formato de propuesta y ficha del modelo
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

### Texto guía

El programa oficial indica **James, Witten, Hastie y Tibshirani, *An Introduction to
Statistical Learning*, Springer**, en su edición con R. En el curso usamos la **edición
en Python (ISLP, 2023)**, que es el mismo libro con el lenguaje que ocupamos.
Descarga gratuita en https://www.statlearning.com

### Complementaria (del programa oficial)

- Saltz, J. S. y Stanton, J. M. (2018). *An Introduction to Data Science*. SAGE.
- Ozdemir, S. (2016). *Principles of Data Science*. Packt.
- García, S., Luengo, J. y Herrera, F. (2015). *Data Preprocessing in Data Mining*. Springer.

### Material adicional del curso

No están en el programa oficial, pero cubren unidades que el texto guía no aborda.

- VanderPlas, J. (2016). *Python Data Science Handbook*. Herramientas: Pandas,
  Matplotlib y Seaborn. https://jakevdp.github.io/PythonDataScienceHandbook/
- O'Neil, C. (2017). *Armas de destrucción matemática*. Capitán Swing. Ética y
  sesgo algorítmico. Lectura del control Q1.
- Russell, S. y Norvig, P. (2021). *Artificial Intelligence: A Modern Approach*,
  4ª ed. Capítulo 1.

### Qué fuente cubre cada unidad

El texto guía cubre muy bien la segunda mitad del curso y casi nada de la primera.
Por eso el material del inicio se apoya en otras fuentes.

| Unidad del programa | Fuente principal |
|---------------------|------------------|
| U1. Fundamentos y ética | Ninguno de los textos del programa. Se usa O'Neil |
| U2. Análisis exploratorio | Ningún texto lo trata como EDA. VanderPlas caps. 3 y 4 dan las herramientas |
| U3. Pre-procesamiento | García, Luengo y Herrera (complementario del programa). VanderPlas cap. 3 (datos faltantes) y cap. 5 (ingeniería de características) |
| U4. Visualización | VanderPlas cap. 4, incluida la sección de Seaborn |
| U5. Inferencia estadística | ISLP cap. 5 (validación cruzada y bootstrap) y cap. 13 (contraste de hipótesis) |
| U6. Aprendizaje automático | ISLP cap. 2. Para lo bayesiano, VanderPlas cap. 5 (Naive Bayes) |
| U7. Clasificación | ISLP cap. 3 (regresión lineal) y cap. 4 (logística, LDA, KNN) |
| U8. Evaluación de modelos | ISLP cap. 2 (sesgo y varianza), cap. 5 (validación cruzada) y cap. 6 (regularización) |
| U9. SVM y redes neuronales | ISLP cap. 9 (SVM) y cap. 10 (deep learning) |
