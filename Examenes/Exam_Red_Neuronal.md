# Evaluacion Redes Neuronales Mediapipe

Nombre: Melvin Marin Gonzalez 
Calificaion:
---

Modelar una red neuronal que pueda identificar emociones a través de los valores obtenidos de los landmakrs que genera mediapipe.

## 1. Definir el tipo de red neuronal y describir cada una de sus partes.

Para este modelado se podria utilizar una Red Neuronal Artifical (ANN).
Con parametros de entradas serian los valores numéricos(coordenadas X,Y y Z) de los lanmarks faciales obtenidos de MediaPipe. Las capas ocultas se pueden utilizar multiples capas densamente conectadas (fully connect) o incluir capas convolucionales si se busca extraer patrones espaciales.
Las funciones de activación es factible usar ReLU (Rectified Linear Unit) en las capas ocultas para introducir no linealidad en la red. Para la capa de salida, se usa Softmax si el modelado debe clasificiar emociones en categorías discretas.
Y la para la Salida un vector con probabilidades asociadas a cada emoción detectada. 

## 2. Definir los patrones a utilizar.

Para los patrones se puede utilzar un modelo basado en características faciales extraídas de MediaPipe. Con algunos aspectos más relevantes, como cuales:

- Posiciones de los Landmarks faciales en coordenadas X, Y y Z.
- La distancia entre puntos clave, como en la separación entre las cejas, la apertura de los ojos y la forma de la boca.
- Cambios en la simetría facil y en ángulo de inclinación de la cabeza.
- Las expresiones comunes relacionadas con cada emoción, por ejemplo, la sonrisa para la felicidad, cejas fruncidas para enojo y/o cara en largada para tristeza.

## 3. Definir funcion de activacion es ncesaria para este problema.

Se podria utilizar como **ReLU** y/o **Softmax**.

- ReLU: se utiliza comúnmente en las cpaas ocultas de las redes neuronales. Ya que su principal ventaja es que permite que el modelo aprenda relaciones no linealess entre las características de entrada. Tambien es eficiente y evita el problema del desvanecimiento del gradiente, lo que esto ayuda a acelerar el entrenamiento, permitiendo una convergencia más rápida.

- Softmax: Es una capa de salida que se utiliza para convertir los valores de activación en probabilidad, que son más fáciles de interpretar. Esto asegura que la malisa del modelo se comporte como una distribución de probalidad, asignado una probabilidad a cada clase, de manera que la suma de todas las probabilidades sea igual a 1.


## 4. Definir el numero máximo de entradas.

El número máximo de entradas dependerá de cuántos **landmarks faciales** se utilicen para la detección. MediaPipe proporciona **468 puntos de referencia faciales** en 3D (coordenadas X, Y, Z). Esto da un total de


$$
468 landmarks × 3 coordenadas (X, Y, Z)= 1404 entrada
$$
Sin embargo, no todos los landmarks son igualmente relevantes para la detección de emociones. Si se eligen solo los 68 landmarks principales o aquellos que representan las partes más importantes del rostro, el número de entradas sería:

$$
68 landmarks ×3 coordenadas (X, Y, Z)= 204 entrada
$$


El modelo puede ajustarse para trabajar con el número óptimo de entradas según los resultados obtenidos en la fase de entrenamiento.

## 5. ¿Que valores a la salida de la red se podrian esperar?

La salida de la red será un vector de probabilidades, donde cada valor representará la probabilidad de que la emoción detectada sea una de las categorías posibles. Por ejemplo, si el modelo clasifica 5 emociones (felicidad, tristeza, enojo, sorpresa, neutralidad), la salida podría verse así:

$$
[0.75,0.10,0.05,0.05,0.05]
$$

En este caso, la red predice con 75% de confianza que la emoción es felicidad. Los valores de salida estarán entre 0 y 1, y la suma de todos los valores será 1 debido a la función de activación Softmax en la capa de salida.

## 6. ¿Cuales son los valores máximos que puede tener el bias?

Para los valores iniciales serian generalmente cercanos a cero, como ejemplo, 0.01,0.02.,etc. Esta inicializacion puede ser aleatoria o fija, depediendo de la implementación.

Para el entrenamiento se puede ajustar de manera similiar a los pesos mediante algoritmos como el descenso de gradiente. Con el objetivo de minimizar el rerorr entre las predciciones de la red y las salidas deseadas.

La escalación de los datos, estos valores de entredas entras normalizados entres 0s y 1s, ya que los valores del bias también se mantiene en un rango pequeño.Sin embargo, si los datos de entrada no están normalizados o tienen una escala mayor, es posible que el bias tome valores más grandes para ajustarse correctamente.
