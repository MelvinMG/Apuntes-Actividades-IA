
##  Ejemplo de Redes Neuronales Feedforward

A continuación, se presenta un ejemplo de una **Red Neuronal Feedforward** utilizando el dataset **Iris**, implementado con `scikit-learn`. En este modelo, se utiliza la normalización de datos para mejorar el rendimiento y se emplea un **MLPClassifier** para la clasificación de datos.

---
###  **Entrenamiento del modelo y guardado con `joblib`**

El modelo se entrena utilizando una capa oculta de 10 neuronas, activación ReLU y el optimizador Adam. Una vez entrenado, el modelo es guardado para su reutilización sin necesidad de volver a entrenarlo.

Se realiza una división del conjunto de datos en entrenamiento y prueba, asegurando que los datos sean normalizados antes de ser procesados por la red neuronal. El modelo es evaluado en función de su precisión y se guarda junto con el escalador utilizado para la normalización.

----------

###  **Carga del modelo y predicción con nuevos datos**

El modelo previamente guardado puede ser cargado para realizar predicciones sin necesidad de reentrenarlo. Para ello, se normaliza el nuevo dato con el mismo escalador utilizado durante el entrenamiento, asegurando que las características se mantengan en la misma escala.

El modelo realiza la predicción y devuelve un valor numérico que representa la clase de la flor en el dataset de Iris. Para interpretar este resultado de manera comprensible, se utiliza un diccionario que traduce los valores numéricos en el nombre correspondiente de la especie.

----------

###  **Uso del Diccionario de Clases**

En los modelos de clasificación de `scikit-learn`, las predicciones se devuelven como valores numéricos correspondientes a cada clase en el conjunto de datos. Para hacer la salida más comprensible, se utiliza un diccionario que asigna cada número a su respectivo nombre en el dataset de Iris.

De esta forma, los valores predichos por el modelo se traducen en nombres de especies de flores, permitiendo una interpretación más clara de los resultados.

---
## Resumen
Se entrenó una red neuronal **feedforward** con el dataset Iris utilizando un modelo de **Perceptrón Multicapa (MLP)**.  
 
 - Se normalizaron los datos para mejorar el rendimiento de la red neuronal.  
 - Se guardó el modelo utilizando `joblib`, permitiendo su reutilizaciónsin necesidad de reentrenarlo.   
 - Se cargó el modelo guardado y se realizaron predicciones sobre nuevos datos.
- Se utilizó un    **diccionario de clases** para interpretar losresultados de manera clara y comprensible.

 Este proceso permite implementar **redes neuronales feedforward** de manera eficiente en problemas de clasificación.