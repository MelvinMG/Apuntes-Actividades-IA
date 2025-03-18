import pygame

# Configuraciones iniciales
pygame.init()  # Inicializa Pygame (para usar fuentes)
ANCHO_VENTANA = 800
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ANCHO_VENTANA))
pygame.display.set_caption("Visualización de Nodos")

# Colores (RGB)
BLANCO = (255, 255, 255)  # Vacíos
NEGRO = (0, 0, 0)         # Paredes
GRIS = (128, 128, 128)    # Nodos visitados
VERDE = (0, 255, 0)       # Camino óptimo (ruta rápida)
ROJO = (255, 0, 0)
NARANJA = (255, 165, 0)   # Inicio
PURPURA = (128, 0, 128)   # Fin

def escribir_texto(ventana, texto, x, y, color=(0, 0, 0), tam=18):
    """Dibuja el texto en la ventana en la posición (x, y)."""
    fuente = pygame.font.SysFont(None, tam)
    superficie_texto = fuente.render(texto, True, color)
    ventana.blit(superficie_texto, (x, y))

class Nodo:
    def __init__(self, fila, col, ancho, total_filas):
        self.fila = fila
        self.col = col
        self.x = fila * ancho
        self.y = col * ancho
        self.color = BLANCO
        self.ancho = ancho
        self.total_filas = total_filas

        # Costos para el algoritmo A*
        self.g = float("inf")  # Costo acumulado (inicialmente infinito)
        self.h = 0             # Heurística (distancia estimada al final)
        self.f = float("inf")  # f = g + h
        self.parent = None     # Para reconstruir el camino óptimo
        self.optimo = False    # Bandera: True si el nodo es parte del camino óptimo

    def get_pos(self):
        return self.fila, self.col

    def es_pared(self):
        return self.color == NEGRO

    def es_inicio(self):
        return self.color == NARANJA

    def es_fin(self):
        return self.color == PURPURA

    def restablecer(self):
        self.color = BLANCO
        self.g = float("inf")
        self.h = 0
        self.f = float("inf")
        self.parent = None
        self.optimo = False

    def hacer_inicio(self):
        self.color = NARANJA

    def hacer_pared(self):
        self.color = NEGRO

    def hacer_fin(self):
        self.color = PURPURA

    def marcar_optimo(self):
        """Marca el nodo como parte del camino óptimo."""
        self.optimo = True

    def dibujar(self, ventana):
        """
        Pinta el nodo según su estado:
         - NARANJA si es el inicio
         - PÚRPURA si es el fin
         - NEGRO si es pared
         - VERDE si es parte del camino óptimo
         - GRIS si ha sido visitado (g < inf)
         - BLANCO si no se ha actualizado
        """
        if self.es_inicio():
            color = NARANJA
        elif self.es_fin():
            color = PURPURA
        elif self.es_pared():
            color = NEGRO
        elif self.optimo:
            color = VERDE
        elif self.g < float("inf"):
            color = GRIS
        else:
            color = BLANCO

        pygame.draw.rect(ventana, color, (self.x, self.y, self.ancho, self.ancho))


# Funciones para obtener los vecinos de un nodo
def obtener_vecinos(grid, nodo):
    vecinos = []
    filas = len(grid)
    # Direcciones: horizontales, verticales y diagonales.
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1),
                   (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for d in direcciones:
        f = nodo.fila + d[0]
        c = nodo.col + d[1]
        if 0 <= f < filas and 0 <= c < filas:
            vecinos.append(grid[f][c])
    return vecinos


# Funcion para explorar todos los nodos posibles
def explorar_nodos(grid, fila_inicio, col_inicio, fila_fin, col_fin):
 
    lista_abierta = []  # Nodos pendientes de explorar
    lista_cerrada = []  # Nodos ya explorados

    nodo_inicio = grid[fila_inicio][col_inicio]
    nodo_inicio.g = 0
    # Heurística: usamos la distancia Manhattan multiplicada por 10 unidades
    
    nodo_inicio.h = (abs(fila_inicio - fila_fin) + abs(col_inicio - col_fin)) * 10

    nodo_inicio.f = nodo_inicio.g + nodo_inicio.h

    nodo_fin = grid[fila_fin][col_fin]
    lista_abierta.append(nodo_inicio)

    while len(lista_abierta) > 0:
        lista_abierta.sort(key=lambda nodo: nodo.f)
        nodo_actual = lista_abierta.pop(0)
        lista_cerrada.append(nodo_actual)
        print(f"Visitado: {nodo_actual.get_pos()} :: G={nodo_actual.g}, H={nodo_actual.h}, F={nodo_actual.f}")
        print("Lista abierta:", [n.get_pos() for n in lista_abierta])
        print("Lista cerrada:", [n.get_pos() for n in lista_cerrada])

        if nodo_actual == nodo_fin:           
            break

        vecinos = obtener_vecinos(grid, nodo_actual)
        for vecino in vecinos:
            if not vecino.es_pared() and vecino not in lista_cerrada:
                if vecino.fila == nodo_actual.fila or vecino.col == nodo_actual.col:
                    costo_movimiento = 10
                else:
                    costo_movimiento = 14

                temp_g = nodo_actual.g + costo_movimiento

                if temp_g < vecino.g:
                    vecino.g = temp_g
                    vecino.h = (abs(vecino.fila - fila_fin) + abs(vecino.col - col_fin)) * 10
                    vecino.f = vecino.g + vecino.h
                    vecino.parent = nodo_actual
                    if vecino not in lista_abierta:
                        lista_abierta.append(vecino)

        # Actualiza pantalla y espera para visualizar la expansión
        dibujar(VENTANA, grid, len(grid), ANCHO_VENTANA)
        pygame.time.delay(100)  # Delay de 100 ms

    return nodo_fin

def reconstruir_camino(nodo_fin):
    """
    Reconstruye el camino óptimo desde el nodo final hasta el nodo de inicio
    utilizando los predecesores.
    Imprime la lista del camino óptimo.
    """
    camino = []
    nodo_actual = nodo_fin
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = nodo_actual.parent
    camino.reverse()  # Orden de inicio a fin
    print("Camino óptimo:", [n.get_pos() for n in camino])
    return camino

def pintar_camino(camino):
    """
    Pinta de VERDE (camino óptimo) cada nodo del camino, excepto el inicio y el fin.
    """
    for nodo in camino:
        if not nodo.es_inicio() and not nodo.es_fin():
            nodo.marcar_optimo()

def crear_grid(filas, ancho):
    grid = []
    ancho_nodo = ancho // filas
    for i in range(filas):
        grid.append([])
        for j in range(filas):
            nodo = Nodo(i, j, ancho_nodo, filas)
            grid[i].append(nodo)
    return grid

def dibujar_grid(ventana, filas, ancho):
    ancho_nodo = ancho // filas
    for i in range(filas):
        pygame.draw.line(ventana, GRIS, (0, i * ancho_nodo), (ancho, i * ancho_nodo))
    for j in range(filas):
        pygame.draw.line(ventana, GRIS, (j * ancho_nodo, 0), (j * ancho_nodo, ancho))

def dibujar(ventana, grid, filas, ancho):
    ventana.fill(BLANCO)
    for fila in grid:
        for nodo in fila:
            nodo.dibujar(ventana)
            if nodo.g < float("inf"):
                offset_x = nodo.x + 2
                offset_y = nodo.y + 2
                escribir_texto(ventana, f"G:{nodo.g}", offset_x, offset_y, color=BLANCO, tam=15)
                escribir_texto(ventana, f"H:{nodo.h}", offset_x, offset_y+16, color=BLANCO, tam=15)
                escribir_texto(ventana, f"F:{nodo.f}", offset_x, offset_y+32, color=BLANCO, tam=15)
    dibujar_grid(VENTANA, filas, ancho) 
    pygame.display.update()


def obtener_click_pos(pos, filas, ancho):
    ancho_nodo = ancho // filas
    y, x = pos
    fila = y // ancho_nodo
    col = x // ancho_nodo
    return fila, col

def main(ventana, ancho):
    FILAS = 11
    grid = crear_grid(FILAS, ancho)
    inicio = None
    fin = None
    corriendo = True

    while corriendo:
        dibujar(VENTANA, grid, FILAS, ancho)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

            # Click izquierdo: definir inicio, fin y paredes
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                fila, col = obtener_click_pos(pos, FILAS, ancho)
                nodo = grid[fila][col]
                if not inicio and nodo != fin:
                    inicio = nodo
                    inicio.hacer_inicio()
                elif not fin and nodo != inicio:
                    fin = nodo
                    fin.hacer_fin()
                elif nodo != fin and nodo != inicio:
                    nodo.hacer_pared()

            # Click derecho: restablecer la celda
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                fila, col = obtener_click_pos(pos, FILAS, ancho)
                nodo = grid[fila][col]
                nodo.restablecer()
                if nodo == inicio:
                    inicio = None
                elif nodo == fin:
                    fin = None

            # Tecla Espacio: iniciar la exploración y luego pintar el camino óptimo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and inicio and fin:
                    nodo_final = explorar_nodos(grid, inicio.fila, inicio.col, fin.fila, fin.col)
                    camino = reconstruir_camino(nodo_final)
                    pintar_camino(camino)
                # Tecla Delete: reinicia toda la cuadrícula
                elif event.key == pygame.K_DELETE:
                    grid = crear_grid(FILAS, ancho)
                    inicio = None
                    fin = None

        # Fin del bucle de eventos
    pygame.quit()

if __name__ == "__main__":
    main(VENTANA, ANCHO_VENTANA)