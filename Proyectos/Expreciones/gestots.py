"""
! Proyecto dde Expresiones faciales y gestos
Usando la libreria mediapipe y opencv
Debemos dectectar la cara y los gestos que son la felicidad, tristeza, enojo y sorpresa
? Autor Melvin Marin Gonzalez
"""
import cv2
import mediapipe as mp
import numpy as np
import time

# Inicializamos Mediapipe para la detección de rostros y gestos
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Captura de video
cap = cv2.VideoCapture(0)  # Cambia el índice si tienes varias cámaras

# Inicializar variables
prev_landmarks = None
last_movement_time = time.time()

MOVEMENT_THRESHOLD = 1.0  # Más sensible
NO_MOVEMENT_DURATION = 1  # Menos tolerante

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

# Funciones para detectar expresiones faciales
def calcular_distancia(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

# Funcion para los puntos de la cara
# Funcion para los puntos de la cara
def draw_landmarks(image, landmarks):
    # Solo dibujamos los puntos faciales sin modificar el fondo
    for idx, landmark in enumerate(landmarks.landmark):
        x = int(landmark.x * image.shape[1])
        y = int(landmark.y * image.shape[0])
        cv2.circle(image, (x, y), 1, (0, 255, 0), 2)  # Solo dibujamos los puntos


# Inicialización de variables
prev_landmarks = None
last_movement_time = time.time()

MOVEMENT_THRESHOLD = 1.0  # Más sensible
NO_MOVEMENT_DURATION = 1  # Menos tolerante

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Conversión a RGB para MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_frame)

    if result.multi_face_landmarks:
        for landmarks in result.multi_face_landmarks:
            draw_landmarks(frame, landmarks)

    # Mostrar solo los puntos faciales (con el fondo negro)
    cv2.imshow('Puntos Faciales', frame)

    # Esperar a que se presione la tecla 'Esc' para cerrar
    if cv2.waitKey(1) & 0xFF == 27:  # 27 es el código ASCII para 'Esc'
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()