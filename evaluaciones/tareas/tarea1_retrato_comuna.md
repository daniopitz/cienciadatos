# Tarea 1: el retrato de tu comuna

**INF-396 Introducción a la Ciencia de Datos** · Segundo semestre 2026
**Modalidad**: en parejas · **Publicación**: viernes 21 de agosto
**Entrega**: jueves 10 de septiembre por Aula *(fecha tentativa; se confirma en clase)*
**Puntaje**: 100 puntos · Atrasos según las reglas del curso (ver README)

## La idea

Van a construir el **retrato de movilidad de una comuna del Gran Santiago** usando
los microdatos de la Encuesta Origen Destino 2012: quiénes viven ahí, cuánto ganan
sus hogares, cómo y cuánto se mueven, y en qué se parece o se diferencia del resto
de la ciudad.

La tarea se desarrolla por etapas en los bloques prácticos de las clases 02, 03 y 04,
así que si aprovechan esos bloques llegarán a la entrega con la mayor parte avanzada.
Cada pareja trabaja una comuna distinta (se reservan en el hilo de Aula, por orden de
llegada) y toda comparación se hace contra el Gran Santiago completo.

## Qué se entrega

Un **notebook ejecutado** (`tarea1_apellido1_apellido2.ipynb`) que corra de principio
a fin en el entorno del curso (`uv sync`), leyendo los datos desde `datos/eod_stgo/`.
Las respuestas van en celdas de markdown junto al código que las produce: interesa
tanto el número como la interpretación.

Incluyan al final la **declaración de uso de IA generativa**: qué herramienta usaron
y para qué (una línea basta). Recuerden que deben poder explicar cualquier línea de
su código si se les pregunta en clase.

## Parte 1. Retrato numérico (30 puntos)

*Se avanza en la clase 02 (21 de agosto); la guía paso a paso está en
`actividades/clase02_actividad.md`.*

1. Tamaño de la muestra en su comuna: hogares y personas encuestadas, y a cuántos
   representan según los factores de expansión. **(6 pts)**
2. Composición: distribución por sexo (con su tabla de códigos) y edad (mediana y
   percentiles 25 y 75), comparadas con el Gran Santiago. **(8 pts)**
3. Ingresos: mediana y media del ingreso de los hogares de su comuna contra la
   ciudad, con una frase que justifique cuál de las dos medidas reportar. **(8 pts)**
4. Movilidad básica: viajes por persona (incluyendo a quienes no viajaron) y duración
   mediana de los viajes con origen en su comuna. **(8 pts)**

## Parte 2. Retrato gráfico (30 puntos)

*Se avanza en la clase 03 (28 de agosto), después de ver métodos gráficos.*

5. La distribución de ingresos de su comuna contra la de Santiago, en un gráfico que
   permita compararlas de verdad. **(10 pts)**
6. El reparto modal de su comuna contra el de Santiago (ponderado por factor de
   expansión), en el tipo de gráfico que mejor compare categorías. **(10 pts)**
7. Un tercer gráfico a elección que muestre algo interesante de su comuna (propósitos
   de viaje, horarios, duración, lo que su exploración sugiera). **(10 pts)**

En los tres: títulos que digan algo, ejes rotulados con unidades, y una frase de
lectura debajo de cada figura. Un gráfico correcto pero ilegible no está terminado.

## Parte 3. Decisiones sobre los datos (20 puntos)

*Se avanza en la clase 04 (4 de septiembre), con pre-procesamiento visto.*

8. Identifiquen los datos faltantes que afectan su retrato (ingresos, factores,
   duraciones) y declaren qué decidieron hacer con ellos y por qué. **(10 pts)**
9. Busquen valores extremos o sospechosos en las duraciones de viaje de su comuna.
   Investíguenlos y declaren la decisión: mantener, corregir o excluir. **(10 pts)**

## Parte 4. La síntesis (20 puntos)

10. Cierren con una sección "El retrato de [su comuna]": máximo 10 líneas que
    integren los hallazgos de las partes anteriores. **(12 pts)**
11. Terminen respondiendo la pregunta del curso: **¿de quién hablan sus números?**
    ¿De la muestra, de la comuna, de la ciudad? ¿Qué personas o viajes podrían estar
    quedando fuera de este retrato? **(8 pts)**

## Hitos

| Fecha | Hito |
|-------|------|
| vie 21-ago | Sale la tarea; en el bloque práctico se avanza la parte 1 |
| vie 28-ago | En el bloque práctico se avanza la parte 2 |
| vie 04-sep | **Avance mínimo**: partes 1 y 2 completas en el notebook |
| jue 10-sep | **Entrega por Aula** *(tentativa)* |

## Los datos

Todo está en `datos/eod_stgo/` del repositorio del curso. La fuente es la Encuesta
Origen Destino de Viajes Santiago 2012, de SECTRA (Ministerio de Transportes):
https://www.sectra.gob.cl/biblioteca/detalle1.asp?mfn=3253
