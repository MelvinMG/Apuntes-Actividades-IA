import pygame
import random
import os
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
W, H = 800, 400
pantalla = pygame.display.set_mode((W, H))
pygame.display.set_caption("Juego: Disparo de Bala, Salto, Nave y Menú")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Nivel del suelo
suelo_y = H - 100

# Variables de jugador
jugador = pygame.Rect(50, suelo_y, 32, 48)
salto = False
vel_salto = 0
gravedad = 1
en_suelo = True
vel_x = 5

# Variables de animación jugador
run_frames_path = 'assets/sprites/run_frames'
jugador_frames = []
for i in range(1, 11):
    img_path = os.path.join(run_frames_path, f'link_frame_{i}.png')
    try:
        img = pygame.image.load(img_path).convert_alpha()
        jugador_frames.append(img)
    except:
        jugador_frames = []
        break

current_frame = 0
frame_count = 0
frame_speed = 10

# Variables bala
bala_img = pygame.image.load('assets/sprites/purple_ball.png')
bala = pygame.Rect(W - 50, H - 90, 16, 16)
vel_bala = -10
bala_disparada = False

# Fondo único
fondo_img = pygame.image.load('assets/game/fondo_1.jpg')
fondo_img = pygame.transform.scale(fondo_img, (W, H))
fondo_x1 = 0
fondo_x2 = W

# Variables menú y pausa
fuente = pygame.font.SysFont('Arial', 24)
menu_activo = True
pausa = False

# Modos de juego
modo_manual = False
modo_nn = False
modo_knn = False
modo_arbol = False

# Datos para modelo (puedes mantener o quitar si no usas)
datos_modelo = []

# Funciones
def mostrar_menu():
    global menu_activo, modo_manual, modo_nn, modo_knn, modo_arbol
    modo_manual = modo_nn = modo_knn = modo_arbol = False
    menu_activo = True

    # Cargar la imagen del lobby
    lobby_img = pygame.image.load('assets/game/Lobby.jpg')
    lobby_img = pygame.transform.scale(lobby_img, (W, H))

    while menu_activo:
        pantalla.blit(lobby_img, (0, 0))

        opciones = [
            "M - Manual",
            "N - Modo Automático NN",
            "K - Modo Automático KNN",
            "A - Modo Automático Árbol",
            "Q - Salir"
        ]
        for i, opcion in enumerate(opciones):
            texto = fuente.render(opcion, True, BLANCO)
            pantalla.blit(texto, (20, 250 + i * 30))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m:
                    modo_manual = True
                    menu_activo = False
                elif evento.key == pygame.K_n:
                    modo_nn = True
                    menu_activo = False
                elif evento.key == pygame.K_k:
                    modo_knn = True
                    menu_activo = False
                elif evento.key == pygame.K_a:
                    modo_arbol = True
                    menu_activo = False
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def manejar_salto():
    global jugador, salto, vel_salto, gravedad, en_suelo

    if salto:
        jugador.y -= vel_salto
        vel_salto -= gravedad

        if jugador.y >= suelo_y:
            jugador.y = suelo_y
            salto = False
            en_suelo = True
            vel_salto = 0

def disparar_bala():
    global bala_disparada, vel_bala
    if not bala_disparada:
        vel_bala = random.randint(-8, -3)
        bala_disparada = True

def reset_bala():
    global bala, bala_disparada
    bala.x = W - 50
    bala_disparada = False

def update():
    global fondo_x1, fondo_x2, current_frame, frame_count, bala

    # Fondo en movimiento continuo (mismo fondo repetido)
    fondo_x1 -= 1
    fondo_x2 -= 1
    if fondo_x1 <= -W:
        fondo_x1 = W
    if fondo_x2 <= -W:
        fondo_x2 = W
    pantalla.blit(fondo_img, (fondo_x1, 0))
    pantalla.blit(fondo_img, (fondo_x2, 0))

    # Animación jugador
    global current_frame, frame_count
    frame_count += 1
    if frame_count >= frame_speed:
        current_frame = (current_frame + 1) % len(jugador_frames) if jugador_frames else 0
        frame_count = 0

    # Dibujar jugador
    if jugador_frames:
        pantalla.blit(jugador_frames[current_frame], (jugador.x, jugador.y))
    else:
        pygame.draw.rect(pantalla, (255, 0, 0), jugador)

    # Mover y dibujar bala
    if bala_disparada:
        bala.x += vel_bala
    if bala.x < 0:
        reset_bala()
    pantalla.blit(bala_img, (bala.x, bala.y))

    # Colisión bala-jugador
    if jugador.colliderect(bala):
        print("¡Colisión detectada!")
        reiniciar_juego()

def guardar_datos():
    global datos_modelo, jugador, bala, vel_bala, salto
    distancia = abs(jugador.x - bala.x)
    salto_hecho = 1 if salto else 0
    datos_modelo.append((vel_bala, distancia, salto_hecho))

def pausa_juego():
    global pausa
    pausa = not pausa
    if pausa:
        print("Juego pausado. Datos recopilados hasta ahora:", datos_modelo)
    else:
        print("Juego reanudado.")

def reiniciar_juego():
    global menu_activo, jugador, bala, bala_disparada, salto, en_suelo
    menu_activo = True
    jugador.x, jugador.y = 50, suelo_y
    bala.x = W - 50
    bala_disparada = False
    salto = False
    en_suelo = True
    print("Datos recopilados:", datos_modelo)
    mostrar_menu()

def main():
    global salto, vel_salto, en_suelo, bala_disparada, pausa, menu_activo
    global modo_manual, modo_nn, modo_knn, modo_arbol

    reloj = pygame.time.Clock()
    mostrar_menu()

    mover_izquierda = False
    mover_derecha = False

    while True:
        reloj.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w and en_suelo and not pausa:
                    salto = True
                    en_suelo = False
                    vel_salto = 15
                if evento.key == pygame.K_p:
                    pausa_juego()
                if evento.key == pygame.K_q:
                    print("Juego terminado. Datos recopilados:", datos_modelo)
                    pygame.quit()
                    sys.exit()
                if evento.key == pygame.K_a:
                    mover_izquierda = True
                if evento.key == pygame.K_d:
                    mover_derecha = True
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_a:
                    mover_izquierda = False
                if evento.key == pygame.K_d:
                    mover_derecha = False

        if not pausa:
            if mover_izquierda:
                jugador.x -= vel_x
                if jugador.x < 0:
                    jugador.x = 0
            if mover_derecha:
                jugador.x += vel_x
                if jugador.x > W - jugador.width:
                    jugador.x = W - jugador.width

            if modo_manual:
                if salto:
                    manejar_salto()
                guardar_datos()
            else:
                # Lógica para modos automáticos si quieres luego agregarla aquí
                if salto:
                    manejar_salto()
                guardar_datos()

            if not bala_disparada:
                disparar_bala()

            update()

        pygame.display.flip()

if __name__ == "__main__":
    main()
