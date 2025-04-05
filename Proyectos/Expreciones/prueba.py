import cv2
import mediapipe as mp
import numpy as np
import time

# Inicializar MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh 
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1,
                                  min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

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

def calcular_distancia(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

def detectar_enojo(landmarks):
    # Cejas y párpados superiores
    left_brow = landmarks[LEFT_BROW]
    right_brow = landmarks[RIGHT_BROW]
    left_eye_top = landmarks[EYE_TOP_L]
    right_eye_top = landmarks[EYE_TOP_R]

    # Distancia ceja-parpado (mientras más chica, más fruncido)
    dist_izq = calcular_distancia(left_brow, left_eye_top)
    dist_der = calcular_distancia(right_brow, right_eye_top)

    return dist_izq < 15 and dist_der < 15  # umbral ajustado a rostro común

def detectar_tristeza(landmarks):
    left = landmarks[LEFT_MOUTH]
    right = landmarks[RIGHT_MOUTH]
    top = landmarks[TOP_MOUTH]
    return left[1] > top[1] and right[1] > top[1]  # comisuras caídas

def detectar_sorpresa(landmarks):
    top = landmarks[TOP_MOUTH]
    bottom = landmarks[BOTTOM_MOUTH]
    eye_top = landmarks[EYE_TOP]
    eye_bottom = landmarks[EYE_BOTTOM]

    boca_abierta = calcular_distancia(top, bottom) > 18
    ojo_abierto = calcular_distancia(eye_top, eye_bottom) > 6
    return boca_abierta and ojo_abierto

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            current_landmarks = []
            h, w, _ = frame.shape
            points = {}

            for idx, lm in enumerate(face_landmarks.landmark):
                x, y = int(lm.x * w), int(lm.y * h)
                current_landmarks.append((x, y))
                points[idx] = (x, y)
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

            if prev_landmarks:
                diffs = [calcular_distancia(a, b) for a, b in zip(prev_landmarks, current_landmarks)]
                avg_movement = np.mean(diffs)

                if avg_movement > MOVEMENT_THRESHOLD:
                    last_movement_time = time.time()

                cv2.putText(frame, f"Mov: {avg_movement:.2f}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

            prev_landmarks = current_landmarks

            emocion_actual = "Ninguna"

            if detectar_sorpresa(points):
                emocion_actual = "Sorpresa"
            elif detectar_enojo(points):
                emocion_actual = "Enojo"
            elif detectar_tristeza(points):
                emocion_actual = "Tristeza"

            if time.time() - last_movement_time > NO_MOVEMENT_DURATION or emocion_actual == "Ninguna":
                cv2.putText(frame, "IMAGEN", (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                cv2.putText(frame, "Persona", (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 0), 2)

            cv2.putText(frame, f"Emocion: {emocion_actual}", (10, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.imshow('Verificacion de Vida con Expresiones', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
