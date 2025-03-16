

# **Proyecto A***

**Alumo**: Melvin Marin Gonzalez 21120229


# Avance 1: Búsqueda de todos los vecinos posibles 16/03/2025

En este avance se implementa la **búsqueda de todos los vecinos** en la cuadrícula, es decir, se exploran todos los nodos posibles.  Además, se pintan de color **verde** los nodos actualizados y se muestran en pantalla los valores de `g`, `h` y `f` tanto en la ventana gráfica como en la terminal. También se agregó la funcionalidad de que la exploración comience al presionar la tecla **Espacio**.

## Descripción General

1. **Nodos con Costos**

    - Se han añadido atributos en la clase `Nodo` para manejar los costos asociados al algoritmo A*. Estos son:
      
      ```python
      self.g = float("inf")  # Costo acumulado desde el nodo inicial. "inf" representa un valor infinito, lo que indica que inicialmente no se conoce un camino hacia el nodo.
      self.h = 0             # Heurística (estimación de la distancia al nodo final).
      self.f = float("inf")  # Costo total estimado (f = g + h). Inicialmente es infinito hasta que se actualiza.
      ```
      
    - Inicialmente, cada nodo tiene `g = inf` y `f = inf`, lo que significa que aún no se ha asignado un camino con un costo real. El valor `inf` (infinito) se utiliza como marcador para indicar que el costo es tan alto que, por el momento, se considera inalcanzable.

2. **Búsqueda de Todos los Vecinos**
En esta función se exploran todos los nodos o vecinos existentes en la cuadrícula. Para cada nodo actual, se obtienen sus vecinos en todas las direcciones (horizontales, verticales y diagonales). Si se detecta que un vecino tiene un costo (calculado como el costo acumulado más el costo del movimiento) menor que el valor actual almacenado en ese vecino, se actualizan sus valores de `g`, `h` y `f` y se agrega a la lista de nodos pendientes de explorar. De esta forma, se ajustan los datos de cada vecino según la ruta más barata encontrada hasta ese momento.
    
3. **Visualización de Costos**

    - **En la ventana de Pygame:**  
      Cada nodo que ha sido actualizado (es decir, cuyo valor de `g` es menor que `inf`) se pinta de **verde** y se muestra el siguiente texto en la esquina superior izquierda de la celda:
      
      ```
      G: <valor_de_g>
      H: <valor_de_h>
      F: <valor_de_f>
      ```
      
    - **En la terminal:**  
      Cada vez que se visita un nodo, se imprime un mensaje con sus coordenadas y los cálculos correspondientes:
      
      ```
      Visitado: (fila, columna) :: Calculos(G=<g>, H=<h>, F=<f>)
      ```

4. **Inicio de la Exploración con la Tecla Espacio**

    - Se agregó la funcionalidad para que la exploración comience únicamente cuando el usuario presione la tecla **Espacio**.  
    - Esto permite al usuario definir previamente el nodo de inicio, el nodo final y las paredes, asegurando que la búsqueda se inicie solo cuando se hayan configurado todos los elementos necesarios.

## Ejemplo de Resultado

![Avance 1](./Proyectos/asterisco/Images/Avance_1.png)

En la captura se observa cómo los nodos transitables (excluyendo las paredes, el nodo de inicio y el nodo final) aparecen en **verde** y muestran sus costos actualizados. Además, en la consola se reporta cada nodo visitado junto con los valores de `g`, `h` y `f`.