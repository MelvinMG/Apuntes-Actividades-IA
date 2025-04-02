import cv2
import mediapipe as mp
import numpy as np
import json
import os

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=2, 
                                  min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

# Landmarks necesarios
selected_points = [33, 263, 1, 97, 326, 61, 291]  # Ojos, nariz, boca

def distancia(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def guardar_json(nombre, puntos, medidas):
    with open(nombre, 'w') as f:
        json.dump({'puntos': puntos, 'medidas': medidas}, f)
    print(f"{nombre} guardado.")

def cargar_json(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            data = json.load(f)
        puntos = {int(k): tuple(v) for k, v in data['puntos'].items()}
        return {'puntos': puntos, 'medidas': data['medidas']}
    return None

def calcular_medidas(puntos):
    dist_ojos = distancia(puntos[33], puntos[263])
    ancho_nariz = distancia(puntos[97], puntos[326])
    ancho_boca = distancia(puntos[61], puntos[291])
    centro_ojos = ((puntos[33][0] + puntos[263][0]) // 2,
                   (puntos[33][1] + puntos[263][1]) // 2)
    ojos_a_nariz = distancia(centro_ojos, puntos[1])
    return {
        "dist_ojos": dist_ojos,
        "ancho_nariz": ancho_nariz,
        "ancho_boca": ancho_boca,
        "ojos_a_nariz": ojos_a_nariz
    }

# Cargar personas
persona1 = cargar_json("persona1.json")
persona2 = cargar_json("persona2.json")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            puntos = {}
            for idx in selected_points:
                x = int(face_landmarks.landmark[idx].x * frame.shape[1])
                y = int(face_landmarks.landmark[idx].y * frame.shape[0])
                puntos[idx] = (x, y)
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            medidas_actuales = calcular_medidas(puntos)

            # Mostrar líneas y distancias , el espacio escala entre distancias para que no cambien las distancias de las caras
            cv2.line(frame, puntos[33], puntos[263], (0, 255, 255), 2)
            cv2.putText(frame, f"Ojos: {int(medidas_actuales['dist_ojos'])} px", 
                        (puntos[33][0], puntos[33][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)

            cv2.line(frame, puntos[97], puntos[326], (255, 0, 0), 2)
            cv2.putText(frame, f"Nariz: {int(medidas_actuales['ancho_nariz'])} px", 
                        (puntos[97][0], puntos[97][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)

            cv2.line(frame, puntos[61], puntos[291], (0, 0, 255), 2)
            cv2.putText(frame, f"Boca: {int(medidas_actuales['ancho_boca'])} px", 
                        (puntos[61][0], puntos[61][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

            centro_ojos = ((puntos[33][0] + puntos[263][0]) // 2,
                           (puntos[33][1] + puntos[263][1]) // 2)
            cv2.line(frame, centro_ojos, puntos[1], (255, 255, 0), 2)
            cv2.putText(frame, f"Ojos-Nariz: {int(medidas_actuales['ojos_a_nariz'])} px", 
                        (centro_ojos[0], centro_ojos[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)

            # Comparación por distancias totales (solo usando medidas)
            etiqueta = "Desconocido"
            if persona1 and persona2:
                d1 = sum(abs(medidas_actuales[k] - persona1['medidas'][k]) for k in medidas_actuales)
                d2 = sum(abs(medidas_actuales[k] - persona2['medidas'][k]) for k in medidas_actuales)
                etiqueta = "Persona 1" if d1 < d2 else "Persona 2"
            elif persona1:
                etiqueta = "Persona 1"
            elif persona2:
                etiqueta = "Persona 2"

            cv2.putText(frame, etiqueta, (puntos[33][0], puntos[33][1] - 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Reconocimiento Facial", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('1') and results.multi_face_landmarks:
        lm = results.multi_face_landmarks[0]
        puntos_guardados = {idx: [lm.landmark[idx].x, lm.landmark[idx].y] for idx in selected_points}
        medidas = calcular_medidas({idx: (int(lm.landmark[idx].x * frame.shape[1]), 
                                          int(lm.landmark[idx].y * frame.shape[0])) for idx in selected_points})
        guardar_json('persona1.json', puntos_guardados, medidas)
        persona1 = cargar_json('persona1.json')
    elif key == ord('2') and results.multi_face_landmarks:
        lm = results.multi_face_landmarks[0]
        puntos_guardados = {idx: [lm.landmark[idx].x, lm.landmark[idx].y] for idx in selected_points}
        medidas = calcular_medidas({idx: (int(lm.landmark[idx].x * frame.shape[1]), 
                                          int(lm.landmark[idx].y * frame.shape[0])) for idx in selected_points})
        guardar_json('persona2.json', puntos_guardados, medidas)
        persona2 = cargar_json('persona2.json')

cap.release()
cv2.destroyAllWindows()
