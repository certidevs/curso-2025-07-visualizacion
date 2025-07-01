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


* Histograma: muestra la distribución de UNA variable numérica dividia en bins. Permite ver rápidamente donde se concentran los datos.
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

* Línea: gráfico de línea, ideal para series temporales, datos agrupados por fecha
    * df['col1'].plot.line()

* Barras:
    * verticales: .plot.bar()
    * horizontales: .plot.barh()
    * Ideal para agrupaciones por categoría como conteo por categoría o suma por categoría
    * CUIDADO: se suele agrupar para evitar crear una barra por cada registro lo cual es un problema.
