import os
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Cargar el dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

# Dividir en conjunto de entrenamiento y prueba (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar las características (importante para MLP)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Definir la red neuronal con una capa oculta de 10 neuronas
mlp = MLPClassifier(hidden_layer_sizes=(10,), activation='relu', solver='adam', max_iter=500, random_state=42)

# Entrenar el modelo
mlp.fit(X_train, y_train)

# Hacer predicciones
y_pred = mlp.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'\nPrecisión en test: {accuracy:.4f}')


# Definir la ruta donde quieres guardar los archivos
directorio = "Ejemplos/Ejemplo_Feedforward"
# Crear el directorio si no existe
os.makedirs(directorio, exist_ok=True)
# Guardar el modelo y el scaler para su uso posterior
joblib.dump(mlp, os.path.join(directorio, 'mlp_model.pkl'))
joblib.dump(scaler, os.path.join(directorio, 'scaler.pkl'))
print("\nModelo y scaler guardados correctamente.")