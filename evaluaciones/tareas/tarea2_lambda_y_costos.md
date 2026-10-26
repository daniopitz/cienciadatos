# Tarea 2

Departamento de Informática  
**Universidad Técnica Federico Santa María**  
**INF-396 Introducción a la Ciencia de Datos** · Segundo semestre 2026  
**Modalidad**: en parejas · **Publicación**: lunes 26 de octubre  
**Entrega**: martes 10 de noviembre por Aula  
**Puntaje**: 100 puntos · Atrasos: 10 puntos menos por día, hasta 3 días; después, nota mínima

## Qué se entrega

1. **Parte 1**: un PDF escrito en LaTeX, `tarea2_apellido1_apellido2_parte1.pdf`.
2. **Partes 2 a 4**: un notebook ejecutado, `tarea2_apellido1_apellido2.ipynb`, a
   partir de la plantilla [`tarea2_plantilla.ipynb`](tarea2_plantilla.ipynb), que corra
   de principio a fin en el entorno del curso (`uv sync`) leyendo los datos desde
   `datos/tarea2/`. Al final, la declaración de uso de IA generativa, en una línea.

Los contenidos de esta tarea entran en el Certamen 2. Por eso, a diferencia de la
Tarea 1, el uso de IA generativa se limita a consultas breves: las demostraciones, el
código y las interpretaciones deben ser trabajo propio de la pareja.

La plantilla separa entrenamiento y prueba, con el 30% en prueba y la semilla 396. En
los tumores la separación es estratificada: se sortea el 30% de cada clase, de modo que
ambas mitades conservan la proporción de malignos. No cambien esa separación.

## Parte 1. Teoría (20 puntos)

**1. Soluciones de Ridge y Lasso en una variable (15 pts).** Sea x ∈ ℝⁿ una variable
estandarizada, con Σxᵢ = 0 y Σxᵢ² = n, sea y ∈ ℝⁿ una respuesta centrada, y considere el
modelo sin intercepto y = b·x. Sea b_mco = (1/n)·Σxᵢyᵢ el estimador de mínimos cuadrados.

- Demuestren que, para λ > 0, el minimizador de Σ(yᵢ − b·xᵢ)² + λb² es
  b_ridge = b_mco · n / (n + λ).
- Demuestren que el minimizador de (1/2n)·Σ(yᵢ − b·xᵢ)² + λ|b| es b_lasso = b_mco − λ
  si b_mco > λ, b_lasso = b_mco + λ si b_mco < −λ, y b_lasso = 0 si |b_mco| ≤ λ.
  Indicación: la función objetivo es convexa y no es diferenciable en b = 0; analicen
  los casos b > 0, b < 0 y b = 0.
- A partir de ambas expresiones, expliquen por qué Lasso anula coeficientes y Ridge
  solo los contrae.

Estas son las funciones objetivo que utiliza scikit-learn.

**2. Monotonía de la norma de la solución de Ridge (5 pts).** Sean b₁ y b₂ las
soluciones de Ridge para λ₁ y λ₂, con 0 < λ₁ < λ₂. Demuestren que ‖b₂‖² ≤ ‖b₁‖².
Indicación: cada solución minimiza su propia función objetivo; escriban las dos
desigualdades correspondientes y súmenlas.

## Parte 2. Implementación (25 puntos)

En esta parte se trabaja con las viviendas de California: se predice el precio mediano
de la zona a partir de las otras 8 variables. Estandaricen las 8 variables con el
entrenamiento, centren el precio restándole su media de entrenamiento y no usen
intercepto, de modo que la fórmula de Ridge aplique directamente.

**3. Ridge con la fórmula (12 pts).** La solución de Ridge es b = (XᵀX + λI)⁻¹ Xᵀy.
Programen esa fórmula con numpy. Para λ igual a 0, 10, 1.000 y 100.000, comparen sus
coeficientes con los de scikit-learn y reporten la mayor diferencia en valor absoluto.
Grafiquen los 8 coeficientes contra λ, con λ en escala logarítmica, y comenten qué pasa
con ellos al crecer λ.

**4. Validación cruzada a mano (13 pts).** Programen la validación cruzada de 5 grupos
sin las funciones de scikit-learn que la hacen: barajen los índices del entrenamiento
con la semilla 396, repártanlos en 5 grupos y, para cada λ de una grilla logarítmica
entre 0,01 y 100.000, ajusten con cuatro grupos usando su función y midan el RMSE en
el quinto, rotando. Grafiquen el error promedio contra λ, reporten el λ elegido y
compárenlo con el de RidgeCV. Expliquen por qué pueden no coincidir y qué indica la
forma de la curva sobre la necesidad de regularizar en este caso.

## Parte 3. Clasificación con costos (30 puntos)

En esta parte se trabaja con los tumores de Wisconsin. La respuesta vale 1 si el tumor
es maligno y 0 si es benigno; estandaricen las 30 variables con el entrenamiento.

**5. Dos regresiones logísticas (8 pts).** Sea yᵢ ∈ {0, 1} el diagnóstico del tumor i y
pᵢ = 1 / (1 + e^(−(a + xᵢᵀb))) la probabilidad de maligno que le asigna el modelo, con
xᵢ ∈ ℝ³⁰. La regresión logística sin regularización elige a y b minimizando la pérdida
logística

L(a, b) = −Σ [ yᵢ·log pᵢ + (1 − yᵢ)·log(1 − pᵢ) ],

que equivale a maximizar la verosimilitud. La regresión logística con la penalización
de Ridge minimiza L(a, b) + λ‖b‖², sin penalizar el intercepto: el castigo impide que
los coeficientes crezcan sin límite cuando las 30 variables separan perfectamente el
entrenamiento. En scikit-learn la fuerza de la penalización se indica con C = 1/λ, y la
logística viene penalizada por defecto.

Ajusten ambos modelos en scikit-learn, no en statsmodels, con las 30 variables
estandarizadas; para el segundo, elijan C por validación cruzada de 5 grupos. Reporten el mayor |bⱼ| y el AUC en
entrenamiento y en prueba de cada modelo, e interpreten la diferencia entre ambos AUC
en cada caso.

**6. Clasificar con umbral 0,5 (6 pts).** Cada modelo asigna a cada tumor una
probabilidad de ser maligno; clasifiquen como maligno los tumores con probabilidad
mayor o igual a 0,5. Para los dos modelos, reporten en prueba la matriz de confusión,
la sensibilidad, la especificidad y la exactitud. Indiquen cuál de los dos errores es
más grave en este problema.

**7. El costo de cada error (10 pts).** Dejar pasar un tumor maligno cuesta 20 veces lo
que cuesta una falsa alarma. Obtengan el umbral que minimiza el costo esperado y
aplíquenlo a los dos modelos: matriz de confusión y costo total, 20·FN + FP, contra el
del umbral 0,5. Expliquen por qué un modelo responde al cambio de umbral y el otro
casi no. Después fijen una meta, detectar al 99% de los malignos, elijan el umbral con
el entrenamiento y reporten en prueba la sensibilidad y la especificidad que logra.

**8. Curva ROC y AUC (6 pts).** Las dos curvas ROC en prueba en una sola figura, con los
tres umbrales marcados. ¿Cuál modelo es mejor, y depende del umbral?

## Parte 4. Regresión con muchas variables (25 puntos)

En esta parte se vuelve a las viviendas de California, ahora con intercepto y con la
respuesta sin centrar: el precio mediano de la zona, en cientos de miles de dólares.
Aquí pueden elegir λ con las funciones de scikit-learn.

**9. Fabricar variables (5 pts).** A partir de las 8 variables estandarizadas,
construyan los 8 cuadrados y los 28 productos de pares: 44 variables en total. Vuelvan
a estandarizarlas con el entrenamiento y reporten las dimensiones de las tablas.

**10. Mínimos cuadrados, Ridge y Lasso (12 pts).** Ajusten mínimos cuadrados con 8 y
con 44 variables, y Ridge y Lasso con 44, con λ por validación cruzada de 5 grupos.
Tabla con el RMSE en entrenamiento y en prueba de los cuatro modelos y del que predice
siempre el promedio. Grafiquen, para Ridge y para Lasso, el RMSE de validación cruzada
contra λ, marcando el λ elegido. Interpreten qué le pasa a mínimos cuadrados al pasar
de 8 a 44 variables y qué hacen Ridge y Lasso con eso.

**11. Qué conserva Lasso (8 pts).** Grafiquen los coeficientes de Lasso contra λ (los 44,
o los más relevantes), con λ en escala logarítmica, marcando el λ elegido. Cuántas de las 44 variables conserva
Lasso con ese λ y cuáles son las cinco de mayor coeficiente. Cierre de media página: qué modelo usarían para tasar
viviendas y por qué, y si sus coeficientes se pueden leer como efectos o solo sirven
para predecir.

## Los datos

En `datos/tarea2/` del repositorio, con un `README.md` que describe cada columna.

- `viviendas_california.csv`: 20.640 zonas censales de California, censo de 1990. Pace,
  R. K. y Barry, R. (1997), *Sparse Spatial Autoregressions*, Statistics and
  Probability Letters, 33, 291 a 297. Vía scikit-learn.
- `tumores_wisconsin.csv`: 569 tumores de mama con 30 medidas del núcleo celular.
  Street, W. N., Wolberg, W. H. y Mangasarian, O. L. (1993), *Nuclear feature
  extraction for breast tumor diagnosis*, IS&T/SPIE. Repositorio UCI, vía scikit-learn.
