# Apuntes-Actividades-IA
Repositorio de apuntes, actividades y proyectos de la materia de IA, de Melvin Marin Gonzalez.
## 1.- Actividad 05/02/2025

En esta actividad, se busca encontrar el camino óptimo desde un **punto de inicio (A)** hasta un **punto final (B)** dentro de una cuadrícula. Esto se realiza utilizando conceptos de **teoría de grafos** y cálculos específicos asociados a los costos de movimiento.
#### **Reglas del Movimiento en la Cuadrícula**

1.  **Movimientos permitidos:**
    
    -   **Lateral (horizontal o vertical):** El costo de cada movimiento es de **10 unidades**.
    -   **Diagonal:** El costo de cada movimiento es de **14 unidades**.
2.  **Cálculo del costo total:**
    
    -   **G (Costo acumulado):** Es el costo total de los movimientos realizados desde el punto inicial hasta el cuadro actual. Por ejemplo:
        -   Si el primer movimiento es horizontal, G = 10.
        -   Si se mueve diagonalmente después de esto, G = 10 + 14 = 24.
    -   **H (Costo heurístico):** Es una estimación del costo restante para llegar al punto final (B). Se calcula basándose en la cantidad de movimientos que faltan.
    -   **F (Costo total estimado):** Es la suma de G y H, es decir: F=G+H.
#### **Descripción del Procedimiento**

1.  **Inicio:**
    
    -   Se selecciona el punto de partida (A) y se inicializa G = 0.
2.  **Exploración de caminos:**
    
    -   A partir del cuadro actual, se calculan las posibles posiciones adyacentes(LA:Lista Abierta) donde se puede mover.
    -   Para cada posición, se calculan los valores de G, H y F.
3.  **Selección del camino óptimo:**
    
    -   Entre todas las opciones disponibles, se selecciona el cuadro con el valor más bajo de F.
    -   Si dos cuadros tienen el mismo valor de F, se elige el primero que se evaluó o según otro criterio preestablecido.
4.  **Avance hacia el punto final (B):**
    
    -   El proceso se repite hasta alcanzar el punto final (B), registrando los cálculos en cada paso(LC: Lista Cerrada). 
---

### Recursos Adicionales

- ![Gráfico de la Actividad](Actividad Grafos.jpg)
- [Ver el PDF de la Actividad](Actividad Grafos.pdf)    