# %%
import pygame
import random

# Dimensiones del juego
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE

# Colores
BACKGROUND_COLOR = (187, 173, 160)
GRID_COLOR = (205, 193, 180)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()

# Función para dibujar el fondo del juego
def draw_background():
    screen.fill(BACKGROUND_COLOR)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 3)

# Función para dibujar un número en una celda
def draw_number(number, x, y):
    font = pygame.font.Font(None, 36)
    text = font.render(str(number), True, (0, 0, 0))
    text_rect = text.get_rect(center=(x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2))
    screen.blit(text, text_rect)

# Función para generar un nuevo número en una celda vacía
def add_new_number():
    empty_cells = [(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE) if grid[x][y] == 0]
    if empty_cells:
        x, y = random.choice(empty_cells)
        grid[x][y] = 2 if random.random() < 0.9 else 4

# Función para mover las celdas hacia arriba
def move_up():
    global grid
    moved = False  # Bandera para verificar si se realizó algún movimiento
    for x in range(GRID_SIZE):
        for y in range(1, GRID_SIZE):
            if grid[x][y] != 0:
                for z in range(y, 0, -1):
                    if grid[x][z - 1] == 0:
                        grid[x][z - 1] = grid[x][z]
                        grid[x][z] = 0
                        moved = True  # Se realizó un movimiento
                    elif grid[x][z - 1] == grid[x][z]:
                        grid[x][z - 1] *= 2
                        grid[x][z] = 0
                        moved = True  # Se realizó un movimiento
                        break
                    else:
                        break
    if moved:  # Si se realizó algún movimiento, agregar un nuevo número
        add_new_number()

def move_down():
    global grid
    moved = False
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE - 2, -1, -1):
            if grid[x][y] != 0:
                for z in range(y, GRID_SIZE - 1):
                    if grid[x][z + 1] == 0:
                        grid[x][z + 1] = grid[x][z]
                        grid[x][z] = 0
                        moved = True
                    elif grid[x][z + 1] == grid[x][z]:
                        grid[x][z + 1] *= 2
                        grid[x][z] = 0
                        moved = True
                        break
                    else:
                        break
    if moved:  # Si se realizó algún movimiento, agregar un nuevo número
        add_new_number()

def move_left():
    global grid
    moved = False
    for y in range(GRID_SIZE):
        for x in range(1, GRID_SIZE):
            if grid[x][y] != 0:
                for z in range(x, 0, -1):
                    if grid[z - 1][y] == 0:
                        grid[z - 1][y] = grid[z][y]
                        grid[z][y] = 0
                        moved = True
                    elif grid[z - 1][y] == grid[z][y]:
                        grid[z - 1][y] *= 2
                        grid[z][y] = 0
                        moved = True
                        break
                    else:
                        break
    if moved:  # Si se realizó algún movimiento, agregar un nuevo número
        add_new_number()

def move_right():
    global grid
    moved = False
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE - 2, -1, -1):
            if grid[x][y] != 0:
                for z in range(x, GRID_SIZE - 1):
                    if grid[z + 1][y] == 0:
                        grid[z + 1][y] = grid[z][y]
                        grid[z][y] = 0
                        moved = True
                    elif grid[z + 1][y] == grid[z][y]:
                        grid[z + 1][y] *= 2
                        grid[z][y] = 0
                        moved = True
                        break
                    else:
                        break
    if moved:  # Si se realizó algún movimiento, agregar un nuevo número
        add_new_number()

# Función para manejar los eventos de teclado
def handle_events():
    global running, grid, game_over, previous_grid, won
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up()
                previous_grid.append([row[:] for row in grid])  # Agregar la cuadrícula actual al historial
            elif event.key == pygame.K_DOWN:
                move_down()
                previous_grid.append([row[:] for row in grid])  # Agregar la cuadrícula actual al historial
            elif event.key == pygame.K_LEFT:
                move_left()
                previous_grid.append([row[:] for row in grid])  # Agregar la cuadrícula actual al historial
            elif event.key == pygame.K_RIGHT:
                move_right()
                previous_grid.append([row[:] for row in grid])  # Agregar la cuadrícula actual al historial
            elif event.key == pygame.K_r:
                if game_over or won:
                    reset_game()
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.key == pygame.K_u:
                if len(previous_grid) > 1:  # Verificar que haya al menos dos cuadrículas en el historial
                    previous_grid.pop()  # Eliminar la cuadrícula actual del historial
                    grid = [row[:] for row in previous_grid[-1]]  # Restaurar la cuadrícula al estado anterior en el historial

# Función para verificar si el juego ha terminado
def is_game_over():
    global grid
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x][y] == 0:
                return False
            if x < GRID_SIZE - 1 and grid[x][y] == grid[x + 1][y]:
                return False
            if y < GRID_SIZE - 1 and grid[x][y] == grid[x][y + 1]:
                return False
    return True

# Función para verificar si el jugador ha ganado el juego
def has_won():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x][y] == 2048:
                return True
    return False

# Función para mostrar la pantalla de perder
def show_game_over():
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, text_rect)
    font = pygame.font.Font(None, 36)
    text_restart = font.render("Press 'R' to restart", True, (255, 255, 255))
    text_quit = font.render("Press 'Q' to quit", True, (255, 255, 255))
    restart_rect = text_restart.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    quit_rect = text_quit.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(text_restart, restart_rect)
    screen.blit(text_quit, quit_rect)
    pygame.display.flip()

# Función para mostrar la pantalla de ganar
def show_win():
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.Font(None, 48)
    text = font.render("You Win!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, text_rect)
    font = pygame.font.Font(None, 36)
    text_restart = font.render("Press 'R' to restart", True, (255, 255, 255))
    text_quit = font.render("Press 'Q' to quit", True, (255, 255, 255))
    restart_rect = text_restart.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    quit_rect = text_quit.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(text_restart, restart_rect)
    screen.blit(text_quit, quit_rect)
    pygame.display.flip()

# Inicializar la cuadrícula
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
add_new_number()
add_new_number()

# Función para reiniciar el juego
def reset_game():
    global grid, game_over, previous_grid, won
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    add_new_number()
    add_new_number()
    game_over = False
    won = False
    previous_grid = [grid[:]]  # Reiniciar el historial con la cuadrícula inicial

# Inicializar la cuadrícula y el historial
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
add_new_number()
add_new_number()
previous_grid = [grid[:]]
won = False

# Diccionario de descripciones de los controles
CONTROL_TEXT = {
    pygame.K_UP: "↑",
    pygame.K_DOWN: "↓",
    pygame.K_LEFT: "←",
    pygame.K_RIGHT: "→",
    pygame.K_u: "U: Deshacer"
}

# Función para dibujar el texto de los controles
def draw_control_text():
    font = pygame.font.Font("Arial.ttf", 16)
    text_controls = font.render("Q: Salir   ←↑↓→: Mover   U: Deshacer", True, (0, 0, 0))
    text_rect = text_controls.get_rect(center=(WIDTH // 2, HEIGHT - 20))
    screen.blit(text_controls, text_rect)

# Bucle principal del juego
running = True
game_over = False
while running:
    screen.fill(BACKGROUND_COLOR)

    draw_background()
    
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[x][y] != 0:
                color = TILE_COLORS.get(grid[x][y], (255, 255, 255))
                pygame.draw.rect(screen, color, (x * TILE_SIZE + 5, y * TILE_SIZE + 5, TILE_SIZE - 10, TILE_SIZE - 10))
                draw_number(grid[x][y], x, y)

    # Dibujar el texto de los controles ENCIMA de todas las casillas
    draw_control_text()

    pygame.display.flip()
    handle_events()
    pygame.time.delay(100)

    if is_game_over():
        show_game_over()
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reset_game()
                        break
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
    elif has_won():
        show_win()
        won = True
        while won:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reset_game()
                        break
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
# %%