import pygame

# Configuraciones iniciales
ANCHO_VENTANA = 800
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ANCHO_VENTANA))
pygame.display.set_caption("Visualización de Nodos")

# Colores (RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NARANJA = (255, 165, 0)
PURPURA = (128, 0, 128)

class Nodo:
    def __init__(self, fila, col, ancho, total_filas):
        self.fila = fila
        self.col = col
        self.x = fila * ancho
        self.y = col * ancho
        self.color = BLANCO
        self.ancho = ancho
        self.total_filas = total_filas
        self.visitado = False  # Indica si el nodo ha sido visitado
        
        # Costos para el algoritmo A*
        self.g = float("inf")  # Costo acumulado (inicialmente infinito)
        self.h = 0             # Heurística
        self.f = float("inf")  # f = g + h

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
        self.visitado = False
        self.g = float("inf")
        self.h = 0
        self.f = float("inf")

    def hacer_inicio(self):
        self.color = NARANJA

    def hacer_pared(self):
        self.color = NEGRO

    def hacer_fin(self):
        self.color = PURPURA

    def marcar_visitado(self):
        self.visitado = True

    def dibujar(self, ventana):
        # Si ya fue visitado, se pinta de verde, salvo que sea inicio o fin.
        if self.visitado and not (self.es_inicio() or self.es_fin()):
            pygame.draw.rect(ventana, VERDE, (self.x, self.y, self.ancho, self.ancho))
        else:
            pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.ancho))

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

def explorar_nodos(grid, fila_inicio, col_inicio, fila_fin, col_fin):
    lista_abierta = []  # Nodos pendientes de explorar
    lista_cerrada = []  # Nodos ya explorados

    nodo_inicio = grid[fila_inicio][col_inicio]
    nodo_inicio.g = 0
    # Heurística: multiplicamos por 10 para representar el costo en puntos
    nodo_inicio.h = (abs(fila_inicio - fila_fin) + abs(col_inicio - col_fin)) * 10
    nodo_inicio.f = nodo_inicio.g + nodo_inicio.h

    nodo_fin = grid[fila_fin][col_fin]
    lista_abierta.append(nodo_inicio)

    while len(lista_abierta) > 0:
        # Ordena la lista abierta por el valor de f (menor costo total estimado)
        lista_abierta.sort(key=lambda nodo: nodo.f)
        nodo_actual = lista_abierta.pop(0)
        nodo_actual.marcar_visitado()
        print(f"Visitado: {nodo_actual.get_pos()} :: Calculos(G={nodo_actual.g}, H={nodo_actual.h}, F={nodo_actual.f})")
        lista_cerrada.append(nodo_actual)

        # Aquí se comenta/elimina la interrupción para seguir explorando
        # if nodo_actual == nodo_fin:
        #     print("¡Objetivo alcanzado!")
        #     break

        # Obtenemos los vecinos del nodo actual
        vecinos = obtener_vecinos(grid, nodo_actual)
        for vecino in vecinos:
            if not vecino.es_pared() and vecino not in lista_cerrada:
                # Determinar el costo de movimiento: 10 para horizontal/vertical, 14 para diagonal
                if vecino.fila == nodo_actual.fila or vecino.col == nodo_actual.col:
                    costo_movimiento = 10
                else:
                    costo_movimiento = 14

                temp_g = nodo_actual.g + costo_movimiento

                # Si encontramos un camino más corto, actualizamos el vecino
                if temp_g < vecino.g:
                    vecino.g = temp_g
                    vecino.h = (abs(vecino.fila - fila_fin) + abs(vecino.col - col_fin)) * 10
                    vecino.f = vecino.g + vecino.h
                    if vecino not in lista_abierta:
                        lista_abierta.append(vecino)
    print("Búsqueda completada: se exploraron todos los vecinos posibles.")
    return lista_cerrada

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
    dibujar_grid(ventana, filas, ancho)
    pygame.display.update()

def obtener_click_pos(pos, filas, ancho):
    ancho_nodo = ancho // filas
    y, x = pos
    fila = y // ancho_nodo
    col = x // ancho_nodo
    return fila, col

def main(ventana, ancho):
    FILAS = 10
    grid = crear_grid(FILAS, ancho)

    inicio = None
    fin = None

    corriendo = True

    while corriendo:
        dibujar(ventana, grid, FILAS, ancho)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

            # Clic izquierdo para definir inicio, fin y paredes
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

            # Clic derecho para restablecer la celda
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                fila, col = obtener_click_pos(pos, FILAS, ancho)
                nodo = grid[fila][col]
                nodo.restablecer()
                if nodo == inicio:
                    inicio = None
                elif nodo == fin:
                    fin = None

            # Presionar la barra espaciadora para iniciar la exploración (si se han definido inicio y fin)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and inicio and fin:
                    explorar_nodos(grid, inicio.fila, inicio.col, fin.fila, fin.col)
        # Fin del bucle de eventos
    pygame.quit()

main(VENTANA, ANCHO_VENTANA)
