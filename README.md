# INF-396 Introducción a la Ciencia de Datos

Universidad Técnica Federico Santa María, Departamento de Informática.
Segundo semestre 2026. Clases los viernes, 2 horas. Primera clase: viernes 7 de agosto.

Material inspirado en el [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)
de Jake VanderPlas (adaptado y traducido, licencia MIT/CC-BY-NC-ND), siguiendo el
programa oficial INF-396 (ver `programa/`).

## Evaluación

`NF = 0,1·Q + 0,1·T + 0,5·promedio(C1, C2) + 0,3·P`

| Ítem | Ponderación | Detalle |
|------|-------------|---------|
| Controles de lectura (Q) | 10% | 4 controles, al inicio de la clase, duración 15 a 20 minutos |
| Tareas (T) | 10% | 4 tareas en parejas, sobre datos reales; gran parte se desarrolla en clase, en el bloque práctico |
| Certámenes (C) | 50% | promedio de C1 (2 de octubre) y C2 (27 de noviembre), individuales |
| Proyecto final (P) | 30% | en grupo; propuesta, avance y presentación + informe con ficha del modelo |

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
- **Honestidad académica**: copiar código de otro grupo sin atribución se considera falta.
  Reutilizar código con atribución (fuente, compañero, IA) siempre es válido.

## Planificación semana a semana

Las 9 unidades temáticas del programa oficial INF-396, distribuidas en 16 clases.
Sin clases el viernes 18 de septiembre (Fiestas Patrias).

Los enlaces se van publicando a medida que avanza el semestre.

| Clase | Fecha | Unidad (programa) | Contenidos | Slides | Notebook | Evaluaciones e hitos |
|-------|-------|-------------------|------------|--------|----------|----------------------|
| 01 | vie 07-ago | U1. Fundamentos y ética | Qué es la ciencia de datos; reglas del curso; IA responsable; marco legal (Ley 21.719, AI Act) | [pdf](presentaciones/clase01_ia_responsable.pdf) · [pptx](presentaciones/clase01_ia_responsable.pptx) | — | Se publica lectura de Q1 |
| 02 | vie 14-ago | Herramientas (apoyo U2) | NumPy y Pandas: arreglos, DataFrames, groupby, merge | — | — | **Sale Tarea 1** (Pandas y EDA) |
| 03 | vie 21-ago | U2. Análisis exploratorio | EDA: estadística descriptiva, métodos gráficos | — | — | **Control Q1** (15 a 20 min): O'Neil, *Armas de destrucción matemática*, Introducción + Cap. 1 |
| 04 | vie 28-ago | U4. Visualización | Matplotlib y Seaborn; datos multivariados; buenas prácticas | — | — | Avance mínimo T1 (revisión en clase) · **Se forman los grupos de proyecto** |
| 05 | vie 04-sep | U3. Pre-procesamiento | Limpieza, imputación, outliers, transformaciones | — | — | **Entrega T1** · **Sale Tarea 2** · **Control Q2** *(lectura tentativa)*: *Datasheets for Datasets* (Gebru et al., 2021) |
| 06 | vie 11-sep | U3. Reducción de dimensión | Selección de características; PCA; efectos no lineales | — | — | **Entrega propuesta de proyecto** (antes de Fiestas Patrias) |
| — | vie 18-sep | *Feriado (Fiestas Patrias)* | | | | |
| 07 | vie 25-sep | U5. Inferencia estadística | Estimación, intervalos, contraste de hipótesis, bootstrap | — | — | **Entrega T2** |
| 08 | vie 02-oct | Certamen | **Certamen 1** (unidades 1 a 5) | | | |
| 09 | vie 09-oct | U6. Aprendizaje automático | Tipos de aprendizaje; función de pérdida; minimización del riesgo esperado; API de scikit-learn | — | — | |
| 10 | vie 16-oct | U7. Regresión | Regresión lineal múltiple; regularización (ridge y lasso) | — | — | **Sale Tarea 3** |
| 11 | vie 23-oct | U7. Clasificación | Regresión logística; análisis discriminante lineal (LDA); KNN | — | — | **Control Q3** *(lectura tentativa)*: *Model Cards* (Mitchell et al., 2019) |
| 12 | vie 30-oct | U8. Evaluación de modelos | Sesgo y varianza; validación cruzada; métricas de desempeño; equidad entre grupos | — | — | **Entrega T3** · **Sale Tarea 4** |
| 13 | vie 06-nov | U6. No supervisado | Clustering: k-means y jerárquico | — | — | **Avance de proyecto (opcional)**: quienes lo presenten parten con 10 puntos de base y reciben retroalimentación |
| 14 | vie 13-nov | U9. Máquinas de soporte vectorial | SVM en clasificación de 2 o más clases; kernels | — | — | **Control Q4** *(lectura tentativa)*: paper aplicado, por definir · **Entrega T4** |
| 15 | vie 20-nov | U9. Redes neuronales | Redes neuronales artificiales en clasificación | — | — | |
| 16 | vie 27-nov | Certamen | **Certamen 2** (unidades 6 a 9) | | | |
| — | vie 04-dic | Proyecto | **Presentaciones del proyecto final** + entrega del informe | | | |

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
- **Propuesta** (obligatoria): se entrega el **11 de septiembre**, antes de Fiestas Patrias.
  Pregunta, datos y plan de trabajo.
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

- `NN_tema.ipynb`: notebook de cada clase, en la raíz (material de referencia para estudiar).
- `presentaciones/`: slides de cada clase, como `claseNN_tema.pptx` y `claseNN_tema.pdf`.
- `actividades/`: enunciados y soluciones de las actividades en clase.
- `lecturas/`: lecturas de los controles (ver `lecturas/README.md`).
- `datos/`: datasets del curso (ver `datos/README.md`).
- `tareas/`: enunciados de tareas y pauta del proyecto.
- `programa/`: programa oficial de la asignatura.

## Bibliografía

- James, G., Witten, D., Hastie, T., Tibshirani, R. *An Introduction to Statistical Learning,
  with Applications in Python* (2023). Texto guía; descarga gratuita en https://www.statlearning.com
- VanderPlas, J. *Python Data Science Handbook* (2016). https://jakevdp.github.io/PythonDataScienceHandbook/
- Russell, S., Norvig, P. *Artificial Intelligence: A Modern Approach*, 4ª ed. (2021). Capítulo 1.
- O'Neil, C. *Armas de destrucción matemática* (2016).
