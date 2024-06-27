import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
file_path = 'categorias.csv'
data = pd.read_csv(file_path)

# Extraer la columna de edades
edades = data['age']

# Crear el histograma con más bins y ajustar el tamaño de la figura
plt.figure(figsize=(10, 6))
plt.hist(edades, bins=20, edgecolor='black')

# Añadir título y etiquetas
plt.title('Distribución de Edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')

# Mostrar la gráfica
plt.show()

