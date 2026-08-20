# Datos del curso

Datasets usados en clases, actividades y tareas.

Los datasets del curso se versionan aquí para que todo corra al clonar el
repositorio. Cuando un archivo original es demasiado pesado, se versiona un
subconjunto y se deja el script que lo genera.

| Dataset | Archivo | Fuente | Se usa en |
|---------|---------|--------|-----------|
| Encuesta Origen Destino de Viajes Santiago 2012 | `eod_stgo/` (47 MB) | SECTRA, Ministerio de Transportes. https://www.sectra.gob.cl/biblioteca/detalle1.asp?mfn=3253 | Clases 02 y 03, Tarea 1 |
| Emisiones al aire de fuentes puntuales, 2020 | `emisiones_aire_2020.csv` (5,5 MB) | Registro de Emisiones y Transferencias de Contaminantes (RETC), Ministerio del Medio Ambiente. https://datosretc.mma.gob.cl | Material complementario |

### eod_stgo/

Microdatos de la EOD 2012, la encuesta de movilidad del Gran Santiago: 18.264 hogares,
60.054 personas y 113.591 viajes de un día, con factores de expansión.

Es una base relacional en CSV (separador punto y coma, coma decimal):

- `Hogares.csv`, `personas.csv`, `viajes.csv`, `Etapas.csv`: las tablas principales,
  conectadas por las llaves `Hogar`, `Persona`, `Viaje` y `Etapa`.
- `DistanciaViaje.csv`, `ViajesDifusion.csv`, `Edadpersonas.csv`, `Vehiculo.csv`:
  tablas satélite, conectadas por sus identificadores.
- `tablas_parametros/`: el significado de cada código (comuna, propósito, modo, etc.).
- `zona777/`: la zonificación en 777 zonas usada por la encuesta.

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
