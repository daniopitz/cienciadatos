# Datos de la clase 6: regresión logística

| Archivo | Filas | Contenido | Origen |
|---|---|---|---|
| `default_islr.csv` | 10.000 | Clientes de una tarjeta de crédito: si dejaron de pagar (`default`), si son estudiantes (`student`), deuda en la tarjeta en dólares (`balance`: lo que el cliente debe después del pago mensual) e ingreso anual en dólares (`income`). Datos simulados por los autores del libro. | James, G., Witten, D., Hastie, T. y Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2a ed.). Archivo `Default.csv` del zip de datos en [statlearning.com](https://www.statlearning.com/resources-second-edition). |
| `titanic.csv` | 891 | Pasajeros del Titanic: si sobrevivieron (`survived`), clase del pasaje (`pclass`), sexo (`sex`), edad (`age`, con 177 valores faltantes), tarifa y otras columnas. | Repositorio de datos de ejemplo de seaborn, [github.com/mwaskom/seaborn-data](https://github.com/mwaskom/seaborn-data). |

El script `preparar_clase06.py` vuelve a descargar ambos archivos desde su origen.
