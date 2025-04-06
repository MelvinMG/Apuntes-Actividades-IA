"""
! Proyecto de Expresiones Faciales y Gestos
Usando la librería MediaPipe y OpenCV
Detectamos la cara y clasificamos las expresiones faciales
Detectamos las siguientes expresiones:
- Enojado
-Triste
- Sorprendida
- Feliz
- Neutral
? Autor: Melvin Marin Gonzalez
"""

import cv2
import mediapipe as mp
import numpy as np
import time
import os

# Opcional: Oculta mensajes de TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Inicializamos MediaPipe para la detección de puntos faciales
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Captura de video
cap = cv2.VideoCapture(0)  # Cambia el índice si tienes varias cámaras

# Índices faciales para expresiones
LEFT_MOUTH = 61
RIGHT_MOUTH = 291
TOP_MOUTH = 13
BOTTOM_MOUTH = 14
LEFT_BROW = 21
RIGHT_BROW = 22
EYE_TOP_R = 159  # párpado superior ojo derecho
EYE_TOP_L = 386  # párpado superior ojo izquierdo
EYE_TOP = 159
EYE_BOTTOM = 145

# Variable global para controlar la impresión cada 1 segundo (para depuración)
last_print_time = time.time()

def draw_landmarks(image, landmarks):
    """Dibuja los puntos faciales sobre la imagen sin modificar el fondo."""
    for idx, landmark in enumerate(landmarks.landmark):
        x = int(landmark.x * image.shape[1])
        y = int(landmark.y * image.shape[0])
        cv2.circle(image, (x, y), 1, (0, 255, 0), 2)

def imprimir_valores(width, height, ratio):
    global last_print_time
    if time.time() - last_print_time >= 1:
        print(f"Ancho: {width}, Alto: {height}")
        print(f"Radio: {ratio}")
        last_print_time = time.time()



def imprimir_distancia_cejas(brow_distance, eye_distance, ratio):
    global last_print_time
    if time.time() - last_print_time >= 1:
        print(f"Distancia cejas: {brow_distance}, Distancia ojos: {eye_distance}")
        print(f"Ratio: {ratio}")
        last_print_time = time.time()

def imprimir_valores_tristeza( left_diff_norm, right_diff_norm, suma):
    global last_print_time
    if time.time() - last_print_time >= 1:
      
        
        print(f"Diferencia normalizada izquierda: {left_diff_norm}, Diferencia normalizada derecha: {right_diff_norm}")
        print(f"Suma: {suma}")
        last_print_time = time.time()




def detectar_sorpresa(landmarks, image_shape):
    """
    Determina si la persona está sorprendida basándose en la relación
    entre el ancho y el alto de la boca.
    Se considera sorprendida cuando el ancho es pequeño y la altura es grande,
    es decir, cuando la relación (width/height) es baja.
    """
    h, w, _ = image_shape
    left_mouth = np.array([landmarks.landmark[LEFT_MOUTH].x * w, landmarks.landmark[LEFT_MOUTH].y * h])
    right_mouth = np.array([landmarks.landmark[RIGHT_MOUTH].x * w, landmarks.landmark[RIGHT_MOUTH].y * h])
    top_mouth = np.array([landmarks.landmark[TOP_MOUTH].x * w, landmarks.landmark[TOP_MOUTH].y * h])
    bottom_mouth = np.array([landmarks.landmark[BOTTOM_MOUTH].x * w, landmarks.landmark[BOTTOM_MOUTH].y * h])
    
    width = np.linalg.norm(left_mouth - right_mouth)
    height = np.linalg.norm(top_mouth - bottom_mouth)
    
    if height <= 0:
        return False
    
    ratio = width / height
    # Puedes descomentar la siguiente línea para depurar:
    # imprimir_valores(width, height, ratio)
    
    # Se considera sorprendida cuando la relación es baja (ajusta el umbral según sea necesario)
    return ratio < 2

def detectar_felicidad(landmarks, image_shape):
    """
    Determina si la persona está feliz (Feliz) basándose en la relación
    entre el ancho y el alto de la boca.
    """
    h, w, _ = image_shape
    left_mouth = np.array([landmarks.landmark[LEFT_MOUTH].x * w, landmarks.landmark[LEFT_MOUTH].y * h])
    right_mouth = np.array([landmarks.landmark[RIGHT_MOUTH].x * w, landmarks.landmark[RIGHT_MOUTH].y * h])
    top_mouth = np.array([landmarks.landmark[TOP_MOUTH].x * w, landmarks.landmark[TOP_MOUTH].y * h])
    bottom_mouth = np.array([landmarks.landmark[BOTTOM_MOUTH].x * w, landmarks.landmark[BOTTOM_MOUTH].y * h])
    
    width = np.linalg.norm(left_mouth - right_mouth)
    height = np.linalg.norm(top_mouth - bottom_mouth)
    
    if height <= 0:
        return False
    
    ratio = width / height

    # Imprime los valores cada 1 segundo para depuración
    #imprimir_valores(width, height, ratio)
    
    # Se considera feliz si el ratio se encuentra en un rango específico.
    # Ajusta los umbrales según sea necesario; este es un ejemplo ilustrativo.
    return 5 <= ratio <= 10

def detectar_enojado(landmarks, image_shape):
    """
    Determina si la persona está enojada (Enojado) utilizando la distancia entre
    las cejas en relación con la distancia entre los ojos.
    Se asume que, al estar enojada, las cejas (usando LEFT_BROW y RIGHT_BROW)
    se acercan y los ojos (usando EYE_TOP_R y EYE_TOP_L) permanecen relativamente separados.
    La relación (distancia entre cejas / distancia entre ojos) baja indica enojo.
    """
    h, w, _ = image_shape

    # Extraer coordenadas de las cejas
    left_brow = np.array([landmarks.landmark[LEFT_BROW].x * w, landmarks.landmark[LEFT_BROW].y * h])
    right_brow = np.array([landmarks.landmark[RIGHT_BROW].x * w, landmarks.landmark[RIGHT_BROW].y * h])
    
    # Extraer coordenadas de los ojos usando los índices proporcionados
    # EYE_TOP_R: párpado superior del ojo derecho
    # EYE_TOP_L: párpado superior del ojo izquierdo
    right_eye = np.array([landmarks.landmark[EYE_TOP_R].x * w, landmarks.landmark[EYE_TOP_R].y * h])
    left_eye = np.array([landmarks.landmark[EYE_TOP_L].x * w, landmarks.landmark[EYE_TOP_L].y * h])
    
    # Calcular distancias
    brow_distance = np.linalg.norm(left_brow - right_brow)
    eye_distance = np.linalg.norm(left_eye - right_eye)
    
    ratio = brow_distance / eye_distance
    #imprimir_distancia_cejas(brow_distance, eye_distance, ratio)
    
    # Se considera enojado si la relación es baja (ajusta el umbral según tus pruebas)
    return ratio >= 0.71

def detectar_tristeza(landmarks, image_shape):
    """
    Determina si la persona está triste evaluando la posición vertical de las esquinas
    de la boca en relación al centro vertical de la boca.
    
    Se calcula:
      - El centro vertical de la boca (promedio entre TOP_MOUTH y BOTTOM_MOUTH).
      - La altura total de la boca.
      - Las diferencias (normalizadas por la altura) entre la posición vertical de 
        las esquinas (LEFT_MOUTH y RIGHT_MOUTH) y el centro de la boca.
    
    Se asume que la persona está triste si la suma de las diferencias normalizadas es mayor a 0.3,
    lo que indica que ambas esquinas están caídas en relación con el centro.
    """
    h, w, _ = image_shape
    left_corner_y = landmarks.landmark[LEFT_MOUTH].y * h  # Posición vertical de la esquina izquierda
    right_corner_y = landmarks.landmark[RIGHT_MOUTH].y * h  # Posición vertical de la esquina derecha
    top_y = landmarks.landmark[TOP_MOUTH].y * h  # Posición vertical del borde superior de la boca
    bottom_y = landmarks.landmark[BOTTOM_MOUTH].y * h  # Posición vertical del borde inferior de la boca

    # Calcula el centro vertical de la boca
    mouth_mid_y = (top_y + bottom_y) / 2.0
    # Calcula la altura total de la boca
    mouth_height = bottom_y - top_y
    if mouth_height <= 0:
        return False

    # Calcula las diferencias normalizadas entre las esquinas y el centro
    left_diff_norm = (left_corner_y - mouth_mid_y) / mouth_height
    right_diff_norm = (right_corner_y - mouth_mid_y) / mouth_height

    suma = left_diff_norm + right_diff_norm

    # Se imprimen los valores cada 1 segundo para reajuste (la función de impresión debe estar definida globalmente)
    imprimir_valores_tristeza(left_diff_norm, right_diff_norm, suma)
    
    # Se considera que la persona está triste si la suma de las diferencias normalizadas supera 0.3.
    return suma > 0.3






while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Por defecto se asume "Neutral"
    expression = "Neutral"

    # Convertir la imagen a RGB para MediaPipe.
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_frame)
    
    if result.multi_face_landmarks:
        for landmarks in result.multi_face_landmarks:
            # Dibuja los puntos faciales
            draw_landmarks(frame, landmarks)
            # Prioridad de detección:
            # Primero se evalúa si está enojado, luego sorprendido, luego feliz.
            if detectar_enojado(landmarks, frame.shape):
                expression = "Enojado"
            elif detectar_sorpresa(landmarks, frame.shape):
                expression = "Sorprendida"
            elif detectar_felicidad(landmarks, frame.shape):
                expression = "Feliz"
            elif detectar_tristeza(landmarks, frame.shape):
                expression = "Triste"    
            else:
                expression = "Neutral"
    
    # Usamos match-case (switch) para mostrar la etiqueta en la imagen.
    match expression:
        case "Enojado":
            cv2.putText(frame, "Enojado", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        case "Sorprendida":
            cv2.putText(frame, "Sorprendida", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        case "Feliz":
            cv2.putText(frame, "Feliz", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        case "Triste":
            cv2.putText(frame, "Triste", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        case _:
            cv2.putText(frame, "Neutral", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    cv2.imshow('Expresiones', frame)
        
    # Cierra la ventana al presionar 'Esc'
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
