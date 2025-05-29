# Proyecto Juego ML: Esquivar y Retornar

**Alumno:**  Melvin Marin Gonzalez 21120229

---

## Avance 1: Juego básico con movimiento, salto, disparos y menú de selección de modos — 28/05/2025

Este proyecto implementa un juego sencillo en Pygame donde un jugador debe esquivar balas disparadas desde dos naves enemigas. El jugador puede moverse lateralmente y saltar para evitar los proyectiles. Además, incorpora un menú para seleccionar entre control manual o automático usando modelos de machine learning para predecir acciones de salto y movimiento.

---

### Descripción General

1. **Movimiento y salto del jugador**

   - El jugador se mueve lateralmente usando las teclas **A** (izquierda) y **D** (derecha).
   - El salto se realiza solo con la barra espaciadora (**Space**).
   - Se implementa física simple de salto con velocidad inicial y gravedad para simular el ascenso y descenso.

2. **Balas y enemigos**

   - Hay dos balas: una disparada horizontalmente desde una nave inferior, y otra que cae verticalmente desde una nave superior.
   - Las balas se reinician automáticamente cuando salen de la pantalla.
   - Las naves y balas tienen representaciones visuales mediante imágenes cargadas de recursos.

3. **Detección de colisiones**

   - Si una bala impacta al jugador, se reinicia el juego.
   - Se lleva un contador de colisiones, y cada impacto imprime un mensaje claro indicando el número de colisiones.

4. **Modelos de Machine Learning**

   - Se recolectan datos durante el modo manual para el entrenamiento de modelos de salto y movimiento.
   - Los modelos disponibles son: Árbol de Decisión, Red Neuronal y K-Nearest Neighbors.
   - Al iniciar el juego, se puede elegir el modo manual o automático con alguno de estos modelos para controlar al jugador.
   - Al entrenar los modelos, se imprime un mensaje con la cantidad de datos usados para el entrenamiento.

5. **Menú inicial**

   - Al comenzar, aparece un menú gráfico con instrucciones para seleccionar el modo de juego o salir.
   - El menú usa imágenes de fondo y texto claro.
   - Las opciones son:
     - **M**: Modo manual (control completo del jugador)
     - **D**: Modo automático con Árbol de Decisión
     - **N**: Modo automático con Red Neuronal
     - **K**: Modo automático con KNN
     - **Q**: Salir del juego

6. **Guardado y recolección de datos**

   - Durante el modo manual, se guardan los datos de posición y velocidad de balas, junto con las acciones realizadas, para entrenar los modelos posteriormente.
   - Esto permite que el sistema aprenda a predecir cuándo saltar o moverse para evitar balas.

7. **Visuales y animaciones**

   - Se carga una animación para el jugador con 10 frames personalizados, representando a **Link** como personaje principal.
   - Se usa un fondo desplazable para dar sensación de movimiento.
   - Se personalizan el lobby, el fondo y el personaje usando imágenes propias para mejorar la experiencia visual.
   - Las naves y balas también usan imágenes propias para un estilo consistente.

---

### Funcionamiento general


- El jugador se mueve y salta respondiendo a las teclas o a las predicciones del modelo.
- Las balas se mueven automáticamente, y la física del salto está simulada.
- En caso de colisión, se muestra un mensaje y se reinicia el juego.
- En modo automático, el jugador intenta esquivar usando los modelos entrenados.
- En modo manual, el jugador controla el personaje y puede generar datos para entrenar los modelos.

---


