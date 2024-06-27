import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo CSV
file_path = 'categorias.csv'
data = pd.read_csv(file_path)

# Función para crear gráficos de barras lado a lado
def crear_barras_lado_a_lado(data, columnas, titulo, categorias):
    bar_width = 0.35
    indices = np.arange(len(columnas))
    
    fig, ax = plt.subplots()
    
    for i, columna in enumerate(columnas):
        hombres = data[data['is_male'] == True][columna].sum()
        mujeres = data[data['is_male'] == False][columna].sum()
        
        ax.bar(indices[i] - bar_width/2, hombres, bar_width, label=f'Hombres - {categorias[i]}', align='edge', color='blue')
        ax.bar(indices[i] + bar_width/2, mujeres, bar_width, label=f'Mujeres - {categorias[i]}', align='edge', color='red')
    
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Cantidad')
    ax.set_title(titulo)
    ax.set_xticks(indices)
    ax.set_xticklabels(categorias)
    ax.legend(['Hombres', 'Mujeres'], loc='upper right')
    
    plt.show()

# Definir las columnas y categorías
columnas = ['has_anaemia', 'has_diabetes', 'is_smoker', 'is_dead']
categorias = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']

# Gráfico de barras para las categorías
crear_barras_lado_a_lado(data, columnas, 'Histograma agrupado por sexo', categorias)