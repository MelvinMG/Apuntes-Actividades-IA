# Ejercicio 1 red neuronal
Melvin Marin Gonzalez. 03/05/2025
## 1.- Definición del tipo de red neuronal y descripción de cada una de las partes
Se va utilizar la  red neuronal convolucional (CNN) o Inteligencia artificial convencional, ya que es eficaz de procesar datos que tienen una estructura en forma de grid, tambien nos ayuda a tomar decisiones mientras se resuelven ciertos problemas concretos.

### *1) Capa de entradas:*
Ya que es una matriz de 20x20 entonces serian 400 valores, y en cada valor o celda podría estar ocupándola un jugador1(nosotros o la ia), jugador2 (el contrario) y/o vacío.

### *2) Capas convolucionales:*
Estas serán responsables de detectar patrones locales en los datos. Con el contexto del juego, estas capas van a identificar los patrones como si fueran líneas de 5 celdas consecutivas, no importan si estan en vertical, horizontal o en diagonal, esto va ser clave principal para el juego. Tambien contara con filtros que van aplicar a la entrada para generar mapas de características.

### *3)Capas de Pooling*
Se utilizara para reducir la dimensionalidad de los mapas de características ya generados por las capas convolucionales, esto nos ayudara a; reducir el tiempo, evitar sobreajuste y la extracción de características mas relevantes.

### *4) Capas de Activación:*
Se puede utilizar la función ReLU para activarlo, ya que ayuda a que la red aprenda patrones no lineales, esto va ser necesario para las tareas complejas como en los juegos.


## 2.- Definir los patrones a utilizar.
### *1) Capa de entradas:*
los datos que se van a utilizar van hacer los estados del tablero:
° Jugador 1(+1, tener posibilidad de ser continua) 
° Jugador 2(-1, perder espacio)
° Vacío (0, espacio vacío)


### *2) Capas convolucionales:*
Esta va ser responsable de identificar las alineaciones de 5 celdas continuas, y los filtros serán aplicados para detectar patrones espaciales, si se encuentras líneas horizontales, verticales y/o diagonales, esto proporcionara características sobre el estado actual del juego.

### *3) Capas de Activación:*
Se utilizara la función ReLU para activar las capas y hacer que la red neuronal aprenda de las relaciones no lineales entra las celdas dentro del tablero. Esta función ayudara a identificar patrones complejos que no pueden ser aprendidos por una red sin activación no lineal.

## 3.- Definición de la función de activación.
Se va utilizar la función ReLU