# Certamen 1

**Universidad Técnica Federico Santa María** · Departamento de Informática  
**INF-396 Introducción a la Ciencia de Datos** · Segundo semestre 2026 · Profesora Daniela Opitz  
**Viernes 9 de octubre de 2026** · Duración: 2 horas · Puntaje total: 100 puntos

**Nombre:** &#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95; **Rol:** &#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;&#95;

**Instrucciones.** El certamen es individual, sin computador ni apuntes. Se permite calculadora. Responda en las hojas de desarrollo que entrega la profesora, indicando la letra o el número de cada pregunta.

Los datos de viajes provienen de la Encuesta Origen Destino de Santiago 2012 (EOD), los mismos de las clases. En las tablas y gráficos, Bip! designa los viajes en transporte público (buses y metro, pagados con la tarjeta bip!). En los ejes de los gráficos, el punto es el separador decimal: 1.25 equivale a 1,25.

| Parte | Preguntas | Puntaje |
|-------|-----------|---------|
| 1. Alternativas | A a J (2 puntos cada una) | 20 |
| 2. Desarrollo | 1 o 2, a elección (40 puntos) | 40 |
| 3. Cálculo | 3 (15 puntos), 4 (25 puntos) | 40 |

## Parte 1. Alternativas (20 puntos)

Responda en la hoja de desarrollo escribiendo la letra de la pregunta y la opción elegida, una sola por pregunta. Una pregunta con más de una opción se corrige con 0 puntos.

**A.** El gráfico muestra, para las 45 comunas del Gran Santiago, el ingreso medio del hogar contra la proporción de viajes en auto. El coeficiente de Pearson es 0,90 y el de Spearman es 0,73. ¿Qué explica la diferencia entre los dos?

![Ingreso y viajes en auto por comuna](figuras/c1_ingreso_auto.png)

- a) Que Spearman descarta las comunas de ingreso extremo antes de calcular el coeficiente, y por eso resulta menor.
- b) Que Pearson usa los valores y Spearman los rangos, y las comunas de ingreso más alto influyen mucho en Pearson.
- c) Que Pearson siempre es mayor que Spearman cuando la asociación es positiva.
- d) Que Spearman está mal calculado, porque con una relación creciente los dos coeficientes deben coincidir.

**B.** En una tabla de la EOD, la columna Comuna viene codificada con un número entero (el código de cada comuna), y `describe()` informa que su promedio es 23,4. ¿Qué tipo de variable es y qué significa ese promedio?

- a) Numérica discreta; el promedio indica que la comuna típica es la número 23.
- b) Categórica ordinal; el promedio indica una comuna de nivel socioeconómico medio.
- c) Categórica nominal; el promedio carece de significado, aunque pandas lo calcule.
- d) Numérica continua; el promedio debe ponderarse por el factor de expansión para que signifique algo.

**C.** El boxplot muestra la duración de los viajes de un día laboral según el modo, con los valores atípicos ocultos. ¿Cuál afirmación es correcta?

![Boxplot de la duración por modo](figuras/c1_boxplot_modo.png)

- a) La mitad central de los viajes en Bip! queda completamente por sobre la mediana de los viajes en auto.
- b) El bigote superior de Bip! marca el viaje en Bip! más largo de toda la muestra.
- c) El auto y Bip! tienen aproximadamente el mismo rango intercuartil, aunque distinta mediana.
- d) El 75% de los viajes en auto dura menos de 15 minutos.

**D.** El gráfico muestra, por hora de inicio, el número de viajes de un día laboral (eje izquierdo) y la proporción de esos viajes hecha en transporte público (eje derecho). Las dos líneas se cruzan en más de un punto. Según Cairo, ¿qué se puede concluir de esos cruces?

![Viajes por hora y proporción en transporte público](figuras/c1_doble_escala.png)

- a) Que en las horas del cruce el número de viajes y el uso del transporte público alcanzan el mismo nivel.
- b) Nada: la posición de los cruces y la inclinación relativa de las líneas dependen de las escalas elegidas para cada eje.
- c) Que el gráfico es incorrecto, porque dos variables con unidades distintas no pueden compartir un mismo gráfico.
- d) Que en la madrugada el alto uso del transporte público mantiene bajo el número de viajes, porque las líneas van en sentido contrario.

**E.** Al convertir el modo de transporte, con seis categorías, en variables dummies para una regresión lineal, se crean cinco columnas y no seis. ¿Por qué?

- a) Porque la categoría más frecuente no necesita columna: su efecto ya está en las demás.
- b) Porque seis columnas más la constante serían colineales: sumarían 1 en todas las filas.
- c) Para que el R² ajustado no castigue el modelo por tener demasiadas variables.
- d) Porque con seis columnas el R² del modelo sería artificialmente igual a 1.

**F.** En una empresa, la mediana de los sueldos es $800.000 y la media es $1.400.000. ¿Qué indica esa diferencia?

- a) Que hay un error en los datos, porque la media y la mediana de un mismo conjunto deben parecerse.
- b) Que la mitad de las personas gana más de $1.400.000 y la otra mitad menos.
- c) Que la mitad de los sueldos está entre $800.000 y $1.400.000.
- d) Que la distribución es asimétrica hacia la derecha: unos pocos sueldos muy altos elevan la media.

**G.** De un conjunto de datos solo se sabe que el primer cuartil es 20 y el tercer cuartil es 60. ¿Cuál afirmación es correcta?

- a) La mediana es 40, porque es el promedio de los dos cuartiles.
- b) El 75% de los datos es menor que 20.
- c) Un valor de 125 quedaría más allá de la cerca superior del boxplot.
- d) El rango intercuartil es 80, la suma de los dos cuartiles.

**H.** Tres personas encuestadas, con factores de expansión 100, 100 y 600, declararon 0, 0 y 4 viajes en el día. La media simple es 1,33 viajes y la media ponderada por el factor es 3,0. ¿Cuál de las dos describe a la población?

- a) La simple, porque cada persona encuestada es una observación y todas valen lo mismo.
- b) La simple, porque los factores de expansión sirven para estimar totales, no promedios.
- c) La ponderada, pero solo si los factores se corrigen para que sumen 1.000.
- d) La ponderada, porque cada fila representa a tantas personas de la población como indica su factor.

**I.** Un banco entrena un modelo de riesgo de no pago sin usar el ingreso de las personas, porque no lo conoce, y en su lugar usa la comuna de residencia. Según O'Neil, ¿qué problema tiene esa decisión?

- a) Ninguno: la comuna es un dato público y, según O'Neil, usar datos públicos nunca produce un arma de destrucción matemática.
- b) Que la comuna es un proxy del ingreso: juzga a cada persona por el promedio de su barrio y no por su conducta.
- c) Que la comuna no sirve como proxy, porque O'Neil solo acepta variables medidas directamente en cada persona.
- d) Ninguno, siempre que el modelo sea transparente: O'Neil solo objeta los modelos opacos.

**J.** Una variable toma los valores 1, 2 y 3 para indicar nivel educacional básico, medio y superior. ¿Qué resumen tiene sentido para describirla?

- a) La media, porque la variable es ordinal y sus códigos están igualmente espaciados.
- b) La desviación estándar, para medir cuánto varía el nivel educacional.
- c) Ninguno, porque es una variable categórica nominal y solo se puede contar.
- d) La mediana o la moda, porque la variable es ordinal: hay orden, pero no distancias iguales.

## Parte 2. Desarrollo (40 puntos)

Responda solo una de las dos preguntas, la 1 o la 2. Si responde las dos, se corrige únicamente la pregunta 1. Se evalúa el argumento, no solo el resultado: escriba los pasos.

**1. Interpretación de una regresión lineal (40 puntos).** Se ajustó, con 69.183 viajes de un día laboral de la EOD, una regresión lineal de la duración del viaje (en minutos, en logaritmo base 10) sobre la distancia en línea recta (en kilómetros, en logaritmo base 10) y el modo de transporte (auto, bicicleta, Bip!, caminata, taxi y taxi colectivo), convertido en variables dummies. La tabla de coeficientes del summary es la siguiente:

| | coef | std err | t | P>\|t\| | [0,025 | 0,975] |
|---|---|---|---|---|---|---|
| const | 1,164 | 0,002 | 479,0 | 0,000 | 1,159 | 1,169 |
| log_km | 0,368 | 0,002 | 160,5 | 0,000 | 0,363 | 0,372 |
| Bicicleta | 0,055 | 0,006 | 9,7 | 0,000 | 0,044 | 0,066 |
| Bip! | 0,263 | 0,003 | 98,5 | 0,000 | 0,257 | 0,268 |
| Caminata | 0,015 | 0,004 | 4,1 | 0,000 | 0,008 | 0,021 |
| Taxi | 0,008 | 0,008 | 1,0 | 0,317 | −0,008 | 0,024 |
| Taxi Colectivo | 0,119 | 0,006 | 20,6 | 0,000 | 0,108 | 0,131 |

Errores estándar redondeados a tres decimales. El R² del modelo es 0,617 y el R² ajustado es 0,617. Sin controlar por la distancia, la duración media de los viajes es de 32 minutos en auto, 62 en Bip!, 32 en taxi colectivo y 15 en caminata.

Se pide:

- **a)** (12 pts) Escriba la ecuación ajustada y explique cómo se lee el coeficiente de log_km. Indique cuál es la categoría de referencia y qué representa el intercepto para esa categoría.
- **b)** (14 pts) Interprete en una frase cada uno de los coeficientes de Bip! y de taxi colectivo. Explique qué se concluye sobre el taxi a partir de su valor p y de su intervalo de confianza.
- **c)** (14 pts) Una persona concluye: "si un pasajero cambia de Bip! a auto, su viaje se acorta a casi la mitad". ¿Respalda el modelo esa conclusión? Explique qué afirma el modelo y qué habría que suponer para que la frase fuera válida. Mencione al menos una variable no incluida en el modelo que podría explicar parte de la diferencia.

**2. Dos correlaciones para las mismas variables (40 puntos).** Con los datos de la EOD, la correlación entre el ingreso del hogar y la duración del viaje es −0,34 cuando cada punto es una comuna (el ingreso medio y la duración media de sus viajes) y 0,00 cuando cada punto es un viaje (el ingreso del hogar del viajero y la duración de ese viaje). Un estudiante concluye que uno de los dos cálculos debe contener un error. Para analizarlo, considere este ejemplo reducido con seis viajes de tres comunas:

<!-- ancho=62 -->

| Comuna | Viaje | Ingreso del hogar (millones) | Duración (min) |
|--------|-------|------------------------------|----------------|
| A | 1 | 0,3 | 35 |
| A | 2 | 0,7 | 85 |
| B | 1 | 0,8 | 20 |
| B | 2 | 1,2 | 70 |
| C | 1 | 1,3 | 5 |
| C | 2 | 1,7 | 55 |

Se pide:

- **a)** (16 pts) Calcule el ingreso medio y la duración media de cada comuna. Luego calcule el coeficiente de Pearson entre ingreso y duración de dos maneras: con los tres promedios comunales como puntos y con los seis viajes como puntos. Compare los dos coeficientes.
- **b)** (12 pts) ¿Tiene razón el estudiante? Explique, a partir del ejemplo, qué está comparando cada una de las dos correlaciones de la EOD y si pueden ser correctas al mismo tiempo.
- **c)** (12 pts) Indique cuál de las dos correlaciones responde a la pregunta "¿las personas de mayor ingreso hacen viajes más cortos?" y cuál a "¿las comunas de mayor ingreso tienen viajes más cortos?". ¿Es válido usar la correlación por comuna para afirmar algo sobre las personas?

<h2 style="page-break-before: always">Parte 3. Cálculo (40 puntos)</h2>

Se evalúa el procedimiento, no solo el resultado: escriba los pasos.

**3. Coeficiente de Spearman (15 puntos).** La tabla muestra, para cinco comunas de la EOD, el ingreso medio del hogar (millones de pesos) y la proporción de viajes en transporte público, ambos ponderados por el factor de expansión:

| Comuna | Ingreso medio (millones) | Viajes en transporte público (%) |
|--------|--------------------------|----------------------------------|
| La Pintana | 0,50 | 49,3 |
| Conchalí | 0,65 | 51,8 |
| Santiago | 0,71 | 29,3 |
| Providencia | 1,47 | 18,5 |
| Ñuñoa | 1,50 | 26,1 |

Se pide:

- **a)** (10 pts) Calcule el coeficiente de Spearman entre el ingreso y la proporción de viajes en transporte público. Muestre los rangos de cada variable y la tabla de diferencias.
- **b)** (5 pts) Interprete el signo y la magnitud del resultado en una frase.

**4. Regresión lineal por comuna, inferencia y bootstrap (25 puntos).** Para las 45 comunas del Gran Santiago se calcularon la duración media de los viajes (minutos) y la distancia media en línea recta (kilómetros), ambas ponderadas por el factor de expansión, y se ajustó la recta duración = a + b · distancia. La tabla de coeficientes del summary, sin la columna t:

| | coef | std err | P>\|t\| | [0,025 | 0,975] |
|---|---|---|---|---|---|
| const | 24,1 | 1,94 | 0,000 | 20,2 | 28,0 |
| distancia | 1,93 | 0,337 | 0,000 | 1,25 | 2,61 |

R² = 0,433.

Se pide:

- **a)** (4 pts) Escriba la ecuación ajustada y lea la pendiente y el intercepto en una frase cada uno.
- **b)** (4 pts) Quilicura tiene una distancia media de 5,2 km y una duración media observada de 44,0 minutos. Calcule su residuo e interprete el signo.
- **c)** (4 pts) Calcule el coeficiente de correlación r a partir del R² e interprete el 0,433 en una frase.
- **d)** (5 pts) Calcule t = coef / std err y explique qué significa el valor obtenido. ¿Por qué el valor p aparece como 0,000?
- **e)** (8 pts) Considere ahora una estimación por bootstrap: la duración media de los viajes de una comuna, estimada a partir de una muestra de solo cinco viajes, de 10, 20, 30, 40 y 100 minutos (media 40, desviación estándar 35,4). Tres remuestreos con reemplazo dieron: (10, 10, 10, 20, 100), (10, 10, 30, 100, 100) y (20, 20, 30, 30, 40).
    - (i) (1 pt) Calcule la media de cada remuestreo.
    - (ii) (2 pts) Con 2.000 remuestreos, la desviación estándar de las 2.000 medias fue 14,3 y los percentiles 2,5 y 97,5 fueron 18 y 70 minutos: ¿en qué posiciones de las 2.000 medias ordenadas se leen esos percentiles? Escriba el intervalo bootstrap.
    - (iii) (3 pts) Calcule el intervalo con la fórmula media ± 2 · s / √n y compárelo con el intervalo bootstrap: ¿a qué se debe la diferencia?
    - (iv) (2 pts) ¿Cuál de los dos intervalos reportaría, y qué cambiaría si la muestra tuviera 500 viajes?

## Formulario

- **Pearson:** r = Σ (xᵢ − x̄)(yᵢ − ȳ) / √( Σ (xᵢ − x̄)² · Σ (yᵢ − ȳ)² ).
- **Spearman:** ρ = 1 − 6 · Σ dᵢ² / ( n · (n² − 1) ), con dᵢ la diferencia entre los rangos de la observación i en las dos variables.
- **Error estándar de la media:** EE = s / √n, con s la desviación estándar de la muestra.
- **Error estándar de la pendiente:** EE(b) = s / √Σ (xᵢ − x̄)², con s = √( Σ eᵢ² / (n − 2) ) la desviación estándar de los residuos eᵢ = yᵢ − ŷᵢ.
- **Intervalo de confianza del 95%:** coeficiente ± 1,96 · EE (en la práctica, coeficiente ± 2 · EE).
