# Tarea 1: el retrato de tu comuna

**Universidad Técnica Federico Santa María** · Departamento de Informática
**INF-396 Introducción a la Ciencia de Datos** · Segundo semestre 2026
**Modalidad**: en parejas · **Publicación**: viernes 21 de agosto
**Entrega**: jueves 10 de septiembre por Aula *(fecha tentativa; se confirma en clase)*
**Puntaje**: 100 puntos · Atrasos según las reglas del curso (ver README)

## La idea

Van a construir el **retrato de movilidad de una comuna del Gran Santiago** usando
los microdatos de la Encuesta Origen Destino 2012. La tarea acumula los contenidos
de las clases 02, 03 y 04: cada parte exige lo visto esa semana, y los bloques
prácticos de esas clases son para avanzarla.

Cada pareja trabaja una comuna distinta (se reservan en el hilo de Aula, por orden
de llegada). Además del Gran Santiago completo, elegirán una **comuna de contraste**
para comparar.

## Qué se entrega

Un **notebook ejecutado** (`tarea1_apellido1_apellido2.ipynb`) que corra de principio
a fin en el entorno del curso (`uv sync`), leyendo los datos desde `datos/eod_stgo/`.
Las respuestas van en celdas de markdown junto al código: interesa el número y la
interpretación. Un resultado correcto sin interpretación no otorga el puntaje completo.

Salvo que se indique lo contrario, **toda cifra que hable de la población debe estar
ponderada por los factores de expansión**; reportar una cifra muestral como si fuera
poblacional descuenta en el ítem correspondiente.

Incluyan al final la **declaración de uso de IA generativa**: qué herramienta usaron
y para qué (una línea basta). Deben poder explicar cualquier línea de su código si se
les pregunta en clase.

## Parte 1. Retrato numérico (25 puntos)

*Con los contenidos de la clase 02. Se avanza en su bloque práctico; guía en
`actividades/clase02_actividad.md`.*

1. **La muestra y a quién representa (5 pts).** Hogares y personas encuestadas en su
   comuna, y a cuántos representan según los factores de expansión. Expliquen en una
   frase por qué las dos cifras responden preguntas distintas.
2. **Composición (6 pts).** Distribución por sexo y edad (mediana y percentiles 25 y
   75), ponderadas, comparadas con el Gran Santiago.
3. **Ingresos (7 pts).** Media, mediana y media truncada al 10% del ingreso de los
   hogares de su comuna, contra la ciudad. Decidan qué medida reportar y justifíquenla
   a partir de la forma de la distribución (no como regla de memoria).
4. **Una tabla que no vimos en clase (7 pts).** Incorporen `Etapas.csv` o
   `Vehiculo.csv` al retrato: por ejemplo, la proporción de viajes con transbordo
   (más de una etapa) en su comuna, o la tasa de vehículos por hogar. Documenten las
   llaves que usaron y verifiquen el merge.

## Parte 2. Retrato gráfico y asociaciones (30 puntos)

*Con la correlación de la clase 02 y los métodos gráficos de la clase 03.*

5. **Distribución de ingresos (8 pts).** Su comuna contra el Gran Santiago, en un
   gráfico que permita comparar las dos distribuciones completas. Justifiquen el tipo
   de gráfico elegido y qué alternativa descartaron y por qué.
6. **La comuna de contraste (8 pts).** Elijan una segunda comuna con un perfil de
   movilidad distinto al de la suya y justifiquen la elección con datos. Comparen el
   reparto modal ponderado de las tres unidades (su comuna, la de contraste, el Gran
   Santiago) en una sola figura.
7. **Asociación dentro de su comuna (8 pts).** Para los viajes con origen en su
   comuna, calculen la correlación de Pearson y la de Spearman entre distancia y
   duración, grafiquen la relación e interpreten: ¿qué indica la diferencia entre
   ambos coeficientes en su comuna? ¿Difiere del patrón del Gran Santiago visto en
   clase?
8. **Un hallazgo propio (6 pts).** Un gráfico adicional a elección que muestre algo
   del retrato que los ítems anteriores no capturan, con su lectura en dos o tres
   líneas. Se evalúa que el hallazgo no sea trivial.

## Parte 3. Decisiones sobre los datos (25 puntos)

*Con el pre-procesamiento de la clase 04.*

9. **Los que faltan (8 pts).** Identifiquen los datos faltantes que afectan su
   retrato (ingresos, factores, duraciones, coordenadas). ¿Siguen algún patrón, o
   pueden tratarse como ausencias sin estructura? Declaren qué decidieron hacer con
   ellos y cómo cambiarían sus cifras con la decisión contraria.
10. **Los extremos (8 pts).** Busquen valores extremos o sospechosos en las duraciones
    y distancias de los viajes de su comuna. Investíguenlos (¿error de registro o
    viaje real?) y declaren la decisión: mantener, corregir o excluir, con su efecto
    sobre las medidas que reportaron.
11. **Una transformación (9 pts).** Apliquen una transformación justificada a una
    variable de su retrato (por ejemplo, logaritmo al ingreso o a la duración) y
    muestren su efecto: cómo cambia la forma de la distribución y qué medidas se
    vuelven más o menos informativas después de transformar.

## Parte 4. Síntesis (20 puntos)

12. **El retrato (8 pts).** Una sección final "El retrato de [su comuna]": máximo 10
    líneas que integren los hallazgos numéricos y gráficos. Debe poder leerse sola,
    sin el resto del notebook.
13. **¿De quién hablan sus números? (6 pts).** ¿De la muestra, de la comuna, de la
    ciudad? ¿Qué personas o viajes podrían estar quedando fuera del retrato (piensen
    en quién responde una encuesta de 2012 y quién no)?
14. **Una hipótesis para más adelante (6 pts).** Formulen una hipótesis verificable
    que su exploración sugiere pero no demuestra (por ejemplo, sobre la relación
    entre dos variables de su comuna). En la unidad 5 veremos cómo ponerla a prueba;
    por ahora se evalúa que sea precisa, comprobable y motivada por sus datos.

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
