import joblib
import numpy as np
import os

# Definir la ruta donde están los archivos
directorio = "Ejemplos/Ejemplo_Feedforward"

# Cargar el modelo y el scaler desde la carpeta específica
mlp_loaded = joblib.load(os.path.join(directorio, 'mlp_model.pkl'))
scaler_loaded = joblib.load(os.path.join(directorio, 'scaler.pkl'))

print("Modelo y scaler cargados correctamente.\n")

# Nuevo dato (4 características como en el dataset Iris)
nuevo_dato = np.array([
    [5.1, 3.5, 1.4, 0.2],  # Ejemplo 1
    [6.7, 3.1, 4.7, 1.5],  # Ejemplo 2
    [5.9, 3.0, 5.1, 1.8]   # Ejemplo 3
])

# Normalizar el nuevo dato
nuevo_dato_escalado = scaler_loaded.transform(nuevo_dato)

# Hacer la predicción
prediccion = mlp_loaded.predict(nuevo_dato_escalado)

# Diccionario para interpretar la clase
clases = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

# Mostrar resultados
for i, pred in enumerate(prediccion):
    print(f' Ejemplo {i+1}: La flor pertenece a la clase {clases[pred]}')
