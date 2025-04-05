# **DOCUMENTACIÓN**: Identificación de Personas y Reconocimiento de Gestos Faciales con MediaPipe

 ## 1. El sistema debe detectar a la persona
El objetivo principal de este sistema es detectar la presencia de una persona viva frente a una cámara en tiempo real, utilizando tecnologías de visión por computadora. Esta detección se realiza mediante el análisis de imágenes capturadas en vivo por una cámara web, procesadas de manera automática y continua.
Una vez que el sistema reconoce la presencia de una persona, el siguiente paso consiste en analizar su rostro en busca de expresiones faciales que permitan inferir el estado emocional del individuo. Esto incluye emociones básicas como:

 - Felicidad (caracterizada por una sonrisa visible, ojos relajados, comisuras de la boca elevadas).
 - Tristeza (comisuras de la boca caídas, cejas inclinadas hacia arriba en el centro).
-   Enojo (cejas fruncidas, labios tensos o presionados, mirada fija), entre otras.

## 2.  Tecnologias a utilizar
Para implementar este sistema se utilizarán las siguientes tecnologías:

- MediaPipe: Herramienta de Google para detección y seguimiento facial en tiempo real. Permite identificar hasta 468 puntos del rostro con alta precisión.
- OpenCV: Biblioteca para capturar video desde la cámara y mostrar visualmente los resultados del análisis facial.
- NumPy: Se usa para cálculos matemáticos como distancias entre puntos faciales, necesarios para reconocer gestos y expresiones.

## 3. Proceso para detectar e identificar a una persona viva

El sistema debe capturar video en tiempo real utilizando la cámara. Cada fotograma (imagen) se convierte a formato RGB, ya que es el formato requerido por MediaPipe para procesar imágenes.

Luego, MediaPipe analiza la imagen y detecta si hay un rostro presente. Si encuentra los puntos clave del rostro (landmarks), se confirma que hay una persona viva frente a la cámara. Esta detección se repite constantemente mientras el sistema está activo.

En caso de que se trate de una persona muerta, el sistema no puede determinarlo biológicamente. Sin embargo, si los rasgos faciales son visibles y definidos, MediaPipe igualmente detectará el rostro como válido, ya que no distingue entre una persona viva o muerta.

## 4. Reconocimiento de gestos faciales o emeciones

Para reconocer expresiones faciales, el sistema interpreta la posición relativa entre puntos clave del rostro (landmarks). Analiza zonas como los ojos, la boca y las cejas para detectar cambios en su forma o distancia.

Por ejemplo:

-   Si la boca está abierta y las comisuras están elevadas, puede indicar **felicidad**.
    
-   Si las cejas están fruncidas y los labios tensos, puede interpretarse como **enojo**.
    
-   Si las comisuras de la boca están hacia abajo y las cejas caídas, puede reflejar **tristeza**.
    

A partir de estos patrones, el sistema infiere la emoción predominante en el rostro.

### Emociones comunes que se pueden detectar:

-   **Felicidad**: boca abierta, comisuras elevadas, ojos relajados.
    
-   **Tristeza**: comisuras caídas, cejas inclinadas hacia afuera.
    
-   **Enojo**: cejas juntas y bajas, labios comprimidos.
    
-   **Sorpresa**: ojos muy abiertos, boca abierta.
    

El sistema  compara las posiciones de los puntos clave con patrones definidos previamente. También se pueden usar  umbrales de distancia o entrenar modelos con ejemplos reales para hacer el reconocimiento más preciso y confiable.