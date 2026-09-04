# INF-396 Introducción a la Ciencia de Datos

Universidad Técnica Federico Santa María, Departamento de Informática.
Electivo de pregrado, 3 créditos UTFSM (5 SCT). Prerrequisitos: INF-239, INF-280 e
INF-285 (o sus equivalentes ILI). Profesora: Daniela Opitz. Ayudante: Flavio Oyarce.

Segundo semestre 2026. Clases los **viernes de 14:40 a 17:15** en la **sala A07**, en
dos bloques de 70 minutos con un recreo de 15. Primera clase: viernes 7 de agosto.
Los anuncios y las entregas van por Aula.

Cuatro viernes sin clases: 14 de agosto (Días Sansanos), 11 y 18 de septiembre
(actividades de Fiestas Patrias y vacaciones) y 16 de octubre (Puertas Abiertas).
Las suspensiones rigen desde las 12:30, así que alcanzan a este curso. Referencia:
[calendario académico oficial USM 2026](https://vra.usm.cl/calendario-academico/).

Material basado en el programa oficial INF-396 (ver `programa/`).

## Evaluación

`NF = 0,1·Q + 0,1·T + 0,5·promedio(C1, C2) + 0,3·P`

| Ítem | Ponderación | Fechas | Detalle |
|------|-------------|--------|---------|
| Controles de lectura (Q) | 10% | **21-ago** (Q1) · **25-sep** (Q2) · Q3 y Q4 por confirmar | 4 controles, al inicio de la clase, duración 20 minutos |
| Tareas (T) | 10% | entregas *(tentativas)*: 10-sep · 9-oct · 4-nov · 20-nov | 4 tareas en parejas, sobre datos reales; gran parte se desarrolla en clase, en el bloque práctico |
| Certámenes (C) | 50% | **2-oct · 27-nov** | promedio de C1 y C2; escritos e individuales |
| Proyecto final (P) | 30% | **25-sep · 6-nov · 4-dic** | en grupo; propuesta, avance y presentación + informe |

### Calendario de evaluaciones

Las tareas se entregan por Aula; algunas entregas caen entre semana. El resto de las
fechas son viernes en el horario de clases. Aquí van solo las evaluaciones formales;
los enunciados de las tareas se publican por Aula y no figuran como hito.

Las fechas de los certámenes, la propuesta y la presentación del proyecto son firmes.
**Las fechas de entrega de las tareas son tentativas**, igual que los controles Q3 y
Q4: se confirman en clase y por Aula, a más tardar una semana antes.

| Fecha | Evaluación | Estado | Detalle |
|-------|------------|--------|---------|
| vie 21-ago | **Control Q1** | ✅ Confirmado | O'Neil, *Armas de destrucción matemática*, Introducción + Cap. 1 |
| vie 28-ago | Hito proyecto | ✅ Confirmado | Se forman los grupos |
| jue 10-sep | [**Entrega T1**](evaluaciones/tareas/tarea1_retrato_comuna.md) | *Tentativo* | El retrato de tu comuna. Se entrega por Aula |
| vie 25-sep | **Control Q2** | ✅ Confirmado | Cairo, *How Charts Lie*, Introducción + Cap. 2 (en inglés) · lectura publicada en Aula. Se movió desde el 04-sep por la extensión de la lectura |
| vie 25-sep | **Propuesta de proyecto** | ✅ Confirmado | Obligatoria: pregunta, datos y plan de trabajo |
| vie 02-oct | **Certamen 1** | ✅ Confirmado | Unidades 1 a 5, incluida la regresión lineal · certamen escrito, individual |
| vie 09-oct | **Entrega T2** | *Tentativo* | |
| vie 30-oct | **Control Q3** | *Tentativo* | Lectura por definir |
| mié 04-nov | **Entrega T3** | *Tentativo* | Se entrega por Aula |
| vie 06-nov | Avance de proyecto *(opcional)* | ✅ Confirmado | Quienes lo presenten parten con 10 puntos de base |
| vie 13-nov | **Control Q4** | *Tentativo* | Lectura por definir |
| vie 20-nov | **Entrega T4** | *Tentativo* | |
| vie 27-nov | **Certamen 2** | ✅ Confirmado | Unidades 6 a 9 · certamen escrito, individual |
| vie 04-dic | **Presentación del proyecto + informe** | ✅ Confirmado | |

## Reglas del curso

- **Trabajo en grupo**: las tareas y el proyecto se hacen en parejas (o grupos pequeños).
- **Datos para el proyecto**: hay [ideas de conjuntos de datos](datasets_proyecto.md)
  con enlaces verificados; se puede usar cualquier conjunto de datos que sirva
  a la pregunta del proyecto.
  Los certámenes son individuales.
- **Entrega de tareas**: se entrega el notebook ejecutado; debe correr de principio a fin en
  el entorno del curso (`uv sync`).
- **Atrasos**: se aceptan con descuento de **10 puntos por día** (escala 0 a 100), hasta un
  máximo de **3 días**. Después de eso, la tarea se califica con nota mínima.
- **Uso de IA generativa (ChatGPT, Copilot, etc.)**: **permitida, con declaración**. Al entregar,
  indiquen qué herramienta usaron y para qué (una línea basta). Deben **entender y poder explicar
  cualquier línea de su código**: en clase se puede preguntar.

## Planificación semana a semana

Las 9 unidades temáticas del programa oficial INF-396, distribuidas en 11 clases de
contenido, 2 certámenes y la presentación del proyecto.

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
| 02 | vie 21-ago | Herramientas + U2. Análisis exploratorio *(parte 1)* | Modelos, inferencia y predicción; correlación (Pearson y Spearman) y causalidad; tipos de datos · Aplicación con Pandas sobre la EOD de Santiago: merge, factores de expansión, estadística descriptiva | [pdf](presentaciones/clase02_pandas_eda.pdf) · [pptx](presentaciones/clase02_pandas_eda.pptx) | [ipynb](02_pandas_eda.ipynb) | **Control Q1** (20 min): O'Neil, *Armas de destrucción matemática*, Introducción + Cap. 1 |
| 03 | vie 28-ago | U2. Análisis exploratorio *(parte 2)* + U4. Visualización | Codificación visual: marcas y canales; percepción; color y paletas · EDA descriptivo: dispersión, boxplots, valores atípicos; calidad de datos | [pdf](presentaciones/clase03_visualizacion_eda.pdf) · [pptx](presentaciones/clase03_visualizacion_eda.pptx) | [ipynb](03_eda_descriptiva.ipynb) | **Se forman los grupos de proyecto** |
| 04 | vie 04-sep | U5. Regresión lineal *(parte 1)* | Matriz de correlación; regresión simple (mínimos cuadrados) y ponderada (WLS); regresión múltiple con statsmodels: R², valor p, dummies | [pdf](presentaciones/clase04_regresion.pdf) · [pptx](presentaciones/clase04_regresion.pptx) | [ipynb](04_regresion.ipynb) | |
| - | vie 11-sep | *Sin clases (actividades de Fiestas Patrias)* | | | | [**Entrega T1**](evaluaciones/tareas/tarea1_retrato_comuna.md) el jueves 10 de septiembre, por Aula |
| - | vie 18-sep | *Vacaciones (14 al 18 de septiembre)* | | | | |
| 05 | vie 25-sep | U5. Inferencia estadística y ajuste de modelos | Estimación, intervalos, contraste de hipótesis, bootstrap · Regresión lineal múltiple | - | - | **Control Q2**: Cairo, *How Charts Lie*, Introducción + Cap. 2 · **Entrega propuesta de proyecto** (de vuelta de vacaciones) |
| 06 | vie 02-oct | Certamen | **Certamen 1** (unidades 1 a 5, incluida la regresión lineal) | | | |
| 07 | vie 09-oct | U8. Sesgo, varianza y regularización | Interpretación de coeficientes y diagnóstico del ajuste · Dilema entre sesgo y varianza · Regularización: ridge y lasso | - | - | **Entrega T2** |
| - | vie 16-oct | *Sin clases (Puertas Abiertas, 14 al 17 de octubre)* | | | | |
| 08 | vie 23-oct | U6. Aprendizaje automático + U7. Clasificación | Tipos de aprendizaje: supervisado, no supervisado y bayesiano; función de pérdida; minimización del riesgo esperado · Regresión logística; análisis discriminante lineal (LDA); KNN | - | - | |
| 09 | vie 30-oct | U8. Evaluación de modelos | Validación cruzada; bootstrap; métricas de desempeño; equidad entre grupos | - | - | **Control Q3** (lectura por definir) |
| 10 | vie 06-nov | U6. No supervisado | Clustering: k-means y jerárquico | - | - | **Entrega T3** el miércoles 4 de noviembre, por Aula · **Avance de proyecto (opcional)**: quienes lo presenten parten con 10 puntos de base y reciben retroalimentación |
| 11 | vie 13-nov | U9. Máquinas de soporte vectorial | SVM en clasificación de 2 o más clases; kernels | - | - | **Control Q4** (lectura por definir) |
| 12 | vie 20-nov | U9. Redes neuronales + U1. Marco legal | Redes neuronales artificiales en clasificación · Marco legal de los datos y la IA: Ley 21.719 y AI Act, con vista al informe del proyecto | - | - | **Entrega T4** |
| 13 | vie 27-nov | Certamen | **Certamen 2** (unidades 6 a 9) | | | |
| - | vie 04-dic | Proyecto | **Presentaciones del proyecto final** + entrega del informe | | | |

### Estructura de cada clase (14:40 a 17:15)

| Bloque | Horario | Contenido |
|--------|---------|-----------|
| 1 | 14:40 a 15:50 | Control de lectura (semanas con control) o repaso de la clase anterior, y teoría (slides en `presentaciones/`) |
| Recreo | 15:50 a 16:05 | |
| 2 | 16:05 a 17:15 | Actividad guiada en notebook, en parejas (`actividades/`); aquí se avanza gran parte de las tareas |

### Material complementario

- [El significado del análisis exploratorio de datos](presentaciones/significado_eda.pdf)
  ([pptx](presentaciones/significado_eda.pptx)): slides de apoyo sobre el origen y el
  sentido del EDA, con un ejemplo sobre las emisiones al aire declaradas en Chile.
- Dataset de emisiones al aire (RUEA 2020, Ministerio del Medio Ambiente), en
  `datos/emisiones_aire_2020.csv`: útil para practicar lo de las clases 02 y 03 con
  otros datos reales (ver [datos/README.md](datos/README.md)).

### Lecturas de los controles

Detalle y enlaces en [`lecturas/README.md`](lecturas/README.md). Resumen:

- **Q1 (21-ago):** O'Neil, *Armas de destrucción matemática*, Introducción + Capítulo 1.
- **Q2 (25-sep):** Cairo, *How Charts Lie*, Introducción + Capítulo 2 (en inglés). La
  lectura está publicada en Aula; el control se movió desde el 04-sep para dar más
  tiempo de lectura.
- **Q3 (30-oct)**: por definir.
- **Q4 (13-nov)**: por definir.

Las lecturas de Q1 y Q2 están definidas; las de Q3 y Q4 se anuncian en clase y por
Aula a más tardar una semana antes de cada control.

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

El curso usa [uv](https://docs.astral.sh/uv/) para que todos trabajen con las mismas
versiones de Python y de las librerías (quedan fijadas en `uv.lock`). Pasos, una sola
vez:

1. Instalar uv. En macOS o Linux:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   En Windows (PowerShell):
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
2. Clonar el repositorio (los datos vienen incluidos, no hay descargas aparte):
   ```bash
   git clone https://github.com/daniopitz/cienciadatos.git
   cd cienciadatos
   ```
3. Crear el entorno e instalar todo (descarga Python si hace falta):
   ```bash
   uv sync
   ```

Para trabajar:

```bash
uv run jupyter lab
```

(o abrir la carpeta en VS Code y elegir el intérprete de `.venv`). Cada semana,
`git pull` trae el material nuevo; si cambian las dependencias, `uv sync` vuelve a
dejar el entorno al día.

## Estructura del repositorio

```
NN_tema.ipynb        notebook de cada clase, en la raíz
presentaciones/      slides: claseNN_tema.pptx y claseNN_tema.pdf
actividades/         enunciados y soluciones de las actividades en clase
evaluaciones/
  tareas/            enunciados de T1 a T4
  controles/         enunciados de Q1 a Q4 (se publican después de aplicarse)
  certamenes/        enunciados de C1 y C2 (se publican después de aplicarse)
  rubricas/          pautas de corrección (se publican después de aplicarse)
  proyecto/          pauta y formato de propuesta
lecturas/            lecturas de los controles (ver lecturas/README.md)
datos/               datasets del curso (ver datos/README.md)
programa/            programa oficial de la asignatura
```

Los enlaces a las slides y al notebook de cada clase están en la tabla de
planificación.

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

## Sobre la elaboración del material

El material de este curso se construye con uso activo de inteligencia artificial
generativa (Claude, de Anthropic) como herramienta de redacción, programación y
revisión. Todo el contenido es revisado, corregido y decidido por la profesora antes
de publicarse, y el historial de este repositorio documenta ese proceso de revisión.
Es el mismo criterio que se pide a los estudiantes en sus entregas: la herramienta
puede usarse, su uso se declara, y la responsabilidad por el resultado es de quien
lo firma. Si encuentra un error en el material, contacte a la profesora de cátedra
para corregirlo.

## Licencia

El material del curso (slides, notebooks, actividades y este README) se publica bajo
la licencia [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es) (ver [LICENSE.md](LICENSE.md)):
se puede reutilizar y adaptar citando la fuente, sin fines comerciales y compartiendo
con la misma licencia. Los datos de `datos/` provienen de fuentes públicas y conservan
las condiciones de su origen (ver `datos/README.md`).
