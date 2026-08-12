# Datos del curso

Datasets usados en clases, actividades y tareas.

Los archivos livianos (menos de 10 MB) se versionan aquí. Los pesados no se suben:
en su lugar se deja un script o una celda de descarga en el notebook que los usa.

| Dataset | Archivo | Fuente | Se usa en |
|---------|---------|--------|-----------|
| Emisiones al aire de fuentes puntuales, 2020 | `emisiones_aire_2020.csv` (5,5 MB) | Registro de Emisiones y Transferencias de Contaminantes (RETC), Ministerio del Medio Ambiente. https://datosretc.mma.gob.cl | Clase 02 (Pandas y EDA) |

### emisiones_aire_2020.csv

27.015 filas y 13 columnas. Cada fila es la emisión de un contaminante declarada por
un establecimiento durante 2020. Cubre 16 regiones, 287 comunas y 19 rubros.

Es un subconjunto del Registro Único de Emisiones Atmosféricas (RUEA) de fuentes
puntuales, que en su versión completa tiene 217.609 filas y pesa 113 MB. Nos quedamos
con los tres contaminantes de los planes de descontaminación atmosférica: MP2,5, MP10
y dióxido de azufre.

Se genera con `preparar_emisiones.py`, que descarga el archivo original y lo recorta:

```bash
uv run python datos/preparar_emisiones.py
```

Conserva los valores faltantes del original, que son reales y sirven para practicar.

## Fuentes chilenas sugeridas para el proyecto

- [datos.gob.cl](https://datos.gob.cl): portal de datos abiertos del Estado
- [INE](https://www.ine.gob.cl): Censo, encuestas de empleo, precios
- [Observatorio Social (CASEN)](https://observatoriosocial.ministeriodesarrollosocial.gob.cl)
- [Ministerio de Educación](https://datosabiertos.mineduc.cl): SIMCE, matrícula, rendimiento
- [Banco Central de Chile](https://si3.bcentral.cl): series económicas
- [Servel](https://www.servel.cl): resultados electorales
