"""Construye las slides de la clase 02.

Las figuras las produce presentaciones/figuras_clase02.py, que hay que correr antes.

Uso:
    uv run python presentaciones/figuras_clase02.py
    uv run python presentaciones/build_clase02_ppt.py
"""

from pathlib import Path

from pptx import Presentation

import estilo

carpeta = Path(__file__).parent
figuras = carpeta / "figuras"
salida = carpeta / "clase02_pandas_eda.pptx"

prs = Presentation()
prs.slide_width = estilo.ANCHO
prs.slide_height = estilo.ALTO

estilo.portada(
    prs,
    "Manipulación de datos y análisis exploratorio",
    "Clase 2 · Pandas y EDA",
    "Daniela Opitz",
    "INF-396 · Departamento de Informática · UTFSM · viernes 21 de agosto, 2026",
)

estilo.contenido(
    prs,
    "Qué veremos hoy",
    [
        "Cargar datos reales y describir su estructura.",
        "Seleccionar, filtrar y tratar los datos faltantes.",
        "Resumir con groupby y combinar tablas con merge.",
        "Empezar el análisis exploratorio: medidas de resumen y primeras figuras.",
        ("Cerramos con la actividad en parejas, en el segundo bloque.", True),
    ],
)

estilo.seccion(prs, "Los datos de hoy", "Emisiones al aire declaradas en Chile")

estilo.contenido(
    prs,
    "De dónde vienen los datos",
    [
        "Registro de Emisiones y Transferencias de Contaminantes (RETC), del Ministerio del Medio Ambiente.",
        "Emisiones al aire de fuentes puntuales, año 2020.",
        [
            "Una fila es un contaminante emitido por un establecimiento.",
            "27.015 filas, 16 regiones, 287 comunas y 19 rubros.",
            "MP2,5, MP10 y SO2: los contaminantes de los planes de descontaminación.",
        ],
        ("Son datos reales, con faltantes y con una distribución muy despareja.", True),
    ],
)

estilo.seccion(prs, "Pandas", "La herramienta para manipular tablas")

estilo.contenido(
    prs,
    "Las dos estructuras de Pandas",
    [
        "DataFrame: una tabla, con filas y columnas con nombre.",
        "Series: una columna, con su índice.",
        [
            "Al seleccionar una columna de un DataFrame se obtiene una Series.",
            "El índice es lo que permite alinear datos entre tablas distintas.",
        ],
        ("Casi todo el trabajo del curso pasa por estas dos estructuras.", True),
    ],
)

estilo.codigo(
    prs,
    "Cargar y mirar antes de calcular",
    [
        "emisiones = pd.read_csv('datos/emisiones_aire_2020.csv')",
        "",
        "emisiones.shape      # cuántas filas y columnas",
        "emisiones.head()     # las primeras filas",
        "emisiones.info()     # tipo de cada columna y cuántos no nulos",
    ],
    "Nunca calcule nada antes de saber qué tiene entre manos.",
)

estilo.codigo(
    prs,
    "Seleccionar columnas",
    [
        "emisiones['region']                      # una Series",
        "emisiones[['region', 'comuna']]          # un DataFrame",
    ],
    "Los dobles corchetes son la lista de nombres dentro de la selección.",
)

estilo.codigo(
    prs,
    "loc y iloc: no confundirlos",
    [
        "emisiones.iloc[0:3]                      # por posición",
        "emisiones.loc[0:2, ['region', 'comuna']] # por etiqueta",
    ],
    "iloc excluye el extremo derecho, como las listas de Python; loc lo incluye.",
)

estilo.codigo(
    prs,
    "Filtrar con condiciones",
    [
        "mp25 = emisiones[emisiones['contaminante'] == 'MP2,5']",
        "",
        "rm = emisiones[",
        "    (emisiones['contaminante'] == 'MP2,5')",
        "    & (emisiones['region'] == 'Metropolitana')",
        "]",
    ],
    "Cada condición va entre paréntesis, y se combinan con & y con |.",
)

estilo.contenido(
    prs,
    "Datos faltantes",
    [
        "Pandas los representa como NaN, y en datos reales siempre hay.",
        "En este archivo faltan 58 valores de toneladas y 12 pares de coordenadas.",
        [
            "isna().sum() cuenta cuántos faltan en cada columna.",
            "dropna() elimina filas; fillna() las rellena.",
        ],
        ("Qué hacer con ellos no es automático: depende de la pregunta.", True),
    ],
)

estilo.codigo(
    prs,
    "groupby: separar, resumir y juntar",
    [
        "mp25.groupby('region')['cantidad_toneladas'].sum()",
        "",
        "mp25.groupby('region')['cantidad_toneladas'].agg(",
        "    total='sum', promedio='mean', mediana='median',",
        ")",
    ],
    "Responde la mayoría de las preguntas descriptivas de un conjunto de datos.",
)

estilo.figura_grande(
    prs,
    "Emisiones de MP2,5 por región",
    figuras / "04_regiones.png",
    "Antofagasta y O'Higgins están arriba con mucha menos población: pesa el perfil productivo.",
)

estilo.codigo(
    prs,
    "merge: combinar dos tablas",
    [
        "mp25_zonas = mp25.merge(macrozonas, on='region', how='left')",
        "",
        "mp25_zonas['macrozona'].isna().sum()   # revisar siempre",
    ],
    "Un nombre escrito distinto en las dos tablas produce NaN sin avisar.",
)

estilo.seccion(prs, "Análisis exploratorio", "Mirar los datos antes de modelarlos")

estilo.contenido(
    prs,
    "Qué es el análisis exploratorio",
    [
        "El término lo acuña John Tukey en 1977, en el libro Exploratory Data Analysis.",
        "La idea: mirar los datos antes de suponer un modelo.",
        [
            "Describir la forma de la distribución, no solo su centro.",
            "Detectar errores, valores extremos y patrones inesperados.",
        ],
        ("Es la etapa donde uno se entera de con qué está trabajando.", True),
    ],
)

estilo.contenido_con_figura(
    prs,
    "El promedio puede engañar",
    [
        "En las emisiones de MP2,5:",
        [
            "Media: 0,382 toneladas.",
            "Mediana: 0,006 toneladas.",
            "Máximo: 299 toneladas.",
        ],
        "La media es unas 66 veces la mediana.",
        ("Decir 'el establecimiento promedio emite 0,38 t' describe a casi ninguno.", True),
    ],
    figuras / "03_media_vs_mediana.png",
)

estilo.contenido(
    prs,
    "Medidas robustas",
    [
        "Una medida es robusta cuando los valores extremos no la alteran demasiado.",
        [
            "Media completa: 0,382 toneladas.",
            "Media truncada al 10%: 0,017 toneladas.",
            "Mediana: 0,006 toneladas.",
        ],
        "La media truncada descarta un porcentaje de cada extremo antes de promediar.",
        ("Con distribuciones asimétricas, la mediana describe mejor el caso típico.", True),
    ],
)

estilo.contenido(
    prs,
    "Percentiles: la forma completa",
    [
        "El percentil 90 es el valor bajo el cual queda el 90% de las observaciones.",
        [
            "Percentil 50: 0,006 t.",
            "Percentil 90: 0,153 t.",
            "Percentil 95: 0,672 t.",
            "Percentil 99: 5,809 t.",
        ],
        ("El 95% emite menos de 0,7 t al año, y el máximo llega a 299.", True),
    ],
)

estilo.figura_grande(
    prs,
    "Un histograma que no se puede leer",
    figuras / "01_histograma_crudo.png",
    "Pasa siempre que la distribución es muy asimétrica: todo cae en la primera barra.",
)

estilo.figura_grande(
    prs,
    "El mismo histograma en escala logarítmica",
    figuras / "02_histograma_log.png",
    "Ojo: los intervalos también deben ser logarítmicos, no basta con cambiar el eje.",
)

estilo.figura_grande(
    prs,
    "Comparar grupos con diagramas de caja",
    figuras / "05_boxplot_macrozona.png",
    "La caja va del percentil 25 al 75, y la línea del medio es la mediana.",
)

estilo.contenido(
    prs,
    "Síntesis",
    [
        "Antes de calcular: shape, info() y datos faltantes.",
        "loc es por etiqueta, iloc por posición, y los filtros son condiciones booleanas.",
        "groupby más una función de resumen responde casi todas las preguntas descriptivas.",
        "Después de un merge, revise si quedaron filas sin pareja.",
        ("Con distribuciones asimétricas, la mediana y los percentiles son más honestos que la media.", True),
    ],
)

estilo.contenido(
    prs,
    "Actividad de hoy",
    [
        "En parejas, en el segundo bloque, sobre el mismo archivo de emisiones.",
        [
            "Cargar los datos y describir su estructura.",
            "Comparar MP10 y MP2,5 por región.",
            "Encontrar los establecimientos que más emiten SO2.",
            "Decidir qué medida de resumen reportar y justificarlo.",
        ],
        ("El enunciado está en actividades/clase02_actividad.md.", True),
    ],
)

prs.save(salida)
print(f"Slides guardadas en {salida.name}: {len(prs.slides._sldIdLst)} slides")
