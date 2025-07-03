# Visualización de datos


Crear entorno virtual:

```bash
python -m venv .venv
```

Activar entorno virtual:

* Windows powershell: .venv\Scripts\activate
* Bash: source .venv/Scripts/activate

Instalar todas las dependencias de golpe:

```bash
pip install -r requirements.txt
```

## NUMPY

Numerical Python - NumPy

* Es una librería de manipulación de vectores, operaciones matemáticas, formulación matemática.
* Proporciona arrays eficientes para operaciones matemáticas: np.array
* Son más rápidas que las listas normales de Python.
* Proporciona métodos para calcular estadísticas.
* Proporciona vectores (arrays de 1 dimensión) y también matrices (2 o más dimensiones).
* ``pip install numpy``
* Ya viene preinstalada en Google Colaboratory, también Anaconda
* Importarlo: ``import numpy as np``

## MATPLOTLIB

Matplotlib es una librería de visualización de datos de las más populares.

* Acepta arrays de NumPy.
* Acepta columnas de Pandas (se llaman Series, y por debajo son arrays de NumPy)

Instalación:

```bash
pip install matplotlib
```

Importarlo:

```python
import matplotlib.pyplot as plt
```

## PANDAS

* Pandas es una librería de manipulación y análisis de datos.
* Pandas está basado en NumPy.
* Pandas integra de forma nativa Matplotlib. Incorpora funciones como .plot que usan matplotlib por debajo.
* Es de más alto nivel que NumPy.

```bash
pip install pandas
```

Importarlo:

```python
import pandas as pd
```

## TIPOS DE VISUALIZACIÓN HABITUALES

https://python-graph-gallery.com/

Matplotlib se puede usar de 3 formas diferentes:

* Opción 1: Directamente desde Pandas usando métodos de pandas como hist, plot...
    * df.hist()
    * df['col].hist()
* Opción 2: usando directamente matplotlib usando la interfaz plt: plt.plot()
    * una lista de python
    * un array de numpy
    * una columna de pandas
* Opción 3: usando directamente matplotlib usando la interfaz orientada a objetos: 
    * fig, ax = plt.subplots(figsize = (9, 6))
    * ax.hist(hours, bins=5, edgecolor="black")


* Histograma: muestra la distribución de UNA variable numérica dividida en bins. Permite ver rápidamente donde se concentran los datos.
    * df.hist()
    * df['total_bill'].hist(bins=50)


* Curva de densidad: como un histograma pero con una curva suave en lugar de barras
    * df['total_bill'].plot.density()
    * df['total_bill'].plot.kde()

* Boxplot: gráfico de caja, resumen de estadísticas
    * df.boxplot()
    * df.boxplot(column=['total_bill', 'tip'])
    * df.boxplot(column='total_bill', by='day')
    * df.plot.box(column='total_bill')
    * Línea del medio es la mediana
    * La caja: del 25 % al 75 % de los datos, osea el 50 % central
    * Puntos sueltos: outliers o anómalos, es decir, valores muy extremos

* Línea: gráfico de línea
    * evolución
    * ideal para series temporales, datos agrupados por fecha
    * df['col1'].plot.line()

* Barras:
    * verticales: .plot.bar()
    * horizontales: .plot.barh()
    * Ideal para agrupaciones por categoría como conteo por categoría o suma por categoría
    * CUIDADO: se suele agrupar para evitar crear una barra por cada registro lo cual es un problema.

* Pie chart (tarta)
    * plt.plot.pie
    * representar un todo, porcentajes con respecto al total
    * df['time'].value_counts().plot.pie(autopct='%1.0f%%', startangle=90)

* scatter (gráfico de puntos)
    * Observar la relación entre dos variables 
    * df.plot.scatter(x='total_bill', y='tip');
    * df.plot.scatter(x='total_bill', y='tip', c='size', colormap='viridis');

* hexbin
    * Muestra la concentración de puntos en forma de hexágonos, similar a scatter pero agrupando puntos en hexágonos
    * df.plot.hexbin(x='total_bill', y='tip', cmap='Blues', gridsize=15);

* area
    * evolución acumulada o acumulativa
    * el área debajo de la línea está rellena de un color
    * ideal para consumos en plataformas de pago por uso como Azure, AWS, GCP, Digital Ocean, OpenIA
    * consumo de facturas de electricidad o gas
    * Gráficas de estadísticas de seguidores en Meta: IG, Threads etc con perfil de creador
    * Gráficas de consumo de batería en android, en windows
    * df.groupby('day')[['tip']].sum()

* Mapa de calor imshow en matplotlib

* Crear gráficos directamente con matplotlib usando plt

* Crear gráficos directamente con matplotlib con la api orientada a objetos

* Combinar gráficos

* Tablas pivotantes: son bastante útiles para agregar datos en función de varias categorías
    * suma de propinas por día de la semana y si es fumador o no
    * ventas medias por categoría de producto y por ciudad
    * visitas a una web a lo largo de la semana y las horas del día como hace google analytics
    * Opcionalmente: Sobre esta tabla resultante se puede crear un gráfico de área o de mapa de calor

* Pasos previos para hacer gráficas:
    * En ciertas ocasiones necesitaremos primero hacer un cálculo con Pandas como por ejemplo groupby o pivot_table para poder tener datos que pintar en un gráfico
    * No obstante, librerías como seaborn son capaces de hacer esos cálculos de forma automática para no tener que hacerlos manualmente nosotros.
    * También Microsoft Power BI hace automáticamente los cálculos y los muestra en gráficos
    * Metabase también hace lo mismo que Power Bi y es open source

## RENDIMIENTO

* Matplotlib y seaborn generan gráficos estáticos, es decir, son imágenes estáticas no interactivas por tanto se generan rápido ya que no cargan javascript.

* Plotly: genera gráficos interactivos, que se puede hacer zoom, rotar, filtrar, cargan javascript por tanto son algo más lentos de generar.

También depende el tipo de gráfico y la cantidad de filas que tengamos en el dataframe.