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