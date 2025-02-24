from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Cargamos el dataset
iris = load_iris()
X,Y = iris.data, iris.target

# Dividimos el dataset en entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Escalamos los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Entrenamos el modelo
mpl = MLPClassifier(hidden_layer_sizes=(10,),activiation='relu',solver='adam',max_iter=500,random_state=42)

# Hacemos predicciones
mpl.fit(X_train, Y_train)

# Evaluamos el modelo
Y_pred = mpl.predict(X_test)

# Calculamos la precisión
accuracy = accuracy_score(Y_test, Y_pred)
print(f'\nPrecisión en test: {accuracy:4f}\n')