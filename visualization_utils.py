import math
import matplotlib.pyplot as plt
import numpy as np

def crear_graficos_categoricos_automaticos(dataframe, tipo_grafico='bar', ncols=2, figsize_per_plot=(6, 4)):
    """
    Crea gráficos automáticamente para todas las columnas categóricas de un dataframe

    Ejemplos de uso:

    print("=== Gráficos de barras verticales ===")
    crear_graficos_categoricos_automaticos(df, tipo_grafico='bar')

    print("\n=== Gráficos de pastel ===")
    crear_graficos_categoricos_automaticos(df, tipo_grafico='pie', ncols=3, figsize_per_plot=(5, 5))

    print("\n=== Gráficos mixtos (alternando pie y barras) ===")
    crear_graficos_categoricos_automaticos(df, tipo_grafico='mixed', figsize_per_plot=(5, 4))

    
    Parameters:
    - dataframe: DataFrame de pandas
    - tipo_grafico: 'bar', 'barh', 'pie', o 'mixed' (mezcla barras y pie)
    - ncols: número de columnas en el subplot
    - figsize_per_plot: tamaño de cada subplot individual
    """
    # Obtener columnas categóricas
    columnas_categoricas = dataframe.select_dtypes(exclude=[np.number]).columns.tolist()
    
    if not columnas_categoricas:
        print("No se encontraron columnas categóricas en el DataFrame")
        return
    
    n_columnas = len(columnas_categoricas)
    nrows = math.ceil(n_columnas / ncols)
    
    # Crear figura con tamaño dinámico
    fig_width = ncols * figsize_per_plot[0]
    fig_height = nrows * figsize_per_plot[1]
    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(fig_width, fig_height))
    
    # Manejar diferentes casos de axes
    if n_columnas == 1:
        axes = np.array([[axes]])
    elif nrows == 1:
        axes = axes.reshape(1, -1)
    elif ncols == 1:
        axes = axes.reshape(-1, 1)
    
    # Paleta de colores
    colores = plt.cm.Set3(np.linspace(0, 1, 12))  # Set3 tiene 12 colores
    
    # Crear gráficos con bucle for
    for i, columna in enumerate(columnas_categoricas):
        fila = i // ncols
        col = i % ncols
        
        # Obtener conteos de valores
        conteos = dataframe[columna].value_counts()
        
        # Determinar tipo de gráfico
        if tipo_grafico == 'mixed':
            # Alternar entre pie y barras
            grafico_actual = 'pie' if i % 2 == 0 else 'bar'
        else:
            grafico_actual = tipo_grafico
        
        # Crear el gráfico según el tipo
        if grafico_actual == 'pie':
            # Gráfico de pastel
            wedges, texts, autotexts = axes[fila, col].pie(conteos.values, 
                                                          labels=conteos.index,
                                                          autopct='%1.1f%%',
                                                          colors=colores[:len(conteos)],
                                                          startangle=90)
            # Hacer el texto más legible
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
                
        elif grafico_actual == 'barh':
            # Gráfico de barras horizontales
            barras = axes[fila, col].barh(conteos.index, conteos.values,
                                         color=colores[:len(conteos)], alpha=0.7)
            axes[fila, col].set_xlabel('Frecuencia')
            axes[fila, col].set_ylabel(columna)
            
            # Añadir valores al final de las barras
            for j, barra in enumerate(barras):
                ancho = barra.get_width()
                axes[fila, col].text(ancho + 0.1, barra.get_y() + barra.get_height()/2.,
                                   f'{int(ancho)}',
                                   ha='left', va='center', fontsize=10)
            
        else:  # 'bar' por defecto
            # Gráfico de barras verticales
            barras = axes[fila, col].bar(conteos.index, conteos.values,
                                       color=colores[:len(conteos)], alpha=0.7)
            axes[fila, col].set_xlabel(columna)
            axes[fila, col].set_ylabel('Frecuencia')
            axes[fila, col].tick_params(axis='x', rotation=45)
            
            # Añadir valores encima de las barras
            for barra in barras:
                altura = barra.get_height()
                axes[fila, col].text(barra.get_x() + barra.get_width()/2., altura,
                                   f'{int(altura)}',
                                   ha='center', va='bottom', fontsize=10)
        
        # Configurar título
        axes[fila, col].set_title(f'{columna} ({grafico_actual})\n(n={len(dataframe[columna].dropna())})', 
                                  fontsize=12, fontweight='bold')
        
        # Grid solo para gráficos de barras
        if grafico_actual in ['bar', 'barh']:
            if grafico_actual == 'bar':
                axes[fila, col].grid(True, alpha=0.3, axis='y')
            else:
                axes[fila, col].grid(True, alpha=0.3, axis='x')
    
    # Ocultar subplots vacíos
    for i in range(n_columnas, nrows * ncols):
        fila = i // ncols
        col = i % ncols
        axes[fila, col].axis('off')
    
    plt.tight_layout()
    plt.suptitle(f'Análisis de Variables Categóricas - {n_columnas} Variables ({tipo_grafico})', 
                 fontsize=16, fontweight='bold', y=1.02)
    plt.show()