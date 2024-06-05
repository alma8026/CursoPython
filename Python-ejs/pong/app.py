import pygame
import sys
import time
import random
import ctypes

# Inicializar Pygame
pygame.init()

# Definir los valores numéricos correspondientes
WM_SETICON = 0x80
ICON_SMALL = 0x0
ICON_BIG = 0x1

# Definir la ruta del archivo de icono
ICON_PATH = 'C:\\codev\\CursoPython\\Python-ejs\\pong\\pong_icon.ico'

# Obtener el identificador de la ventana principal
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# Cargar el icono para la ventana
icon = ctypes.windll.user32.LoadImageW(None, ICON_PATH, 1, 0, 0, 0x10)

# Establecer el icono de la ventana
ctypes.windll.user32.SendMessageW(hwnd, WM_SETICON, ICON_BIG, icon)
ctypes.windll.user32.SendMessageW(hwnd, WM_SETICON, ICON_SMALL, icon)

# Definir el icono de la aplicación
app_id = 'MyPythonApp'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

# Obtener el identificador de la aplicación
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# Cargar el icono para la aplicación
icon = ctypes.windll.user32.LoadImageW(None, ICON_PATH, 1, 0, 0, 0x10)

# Establecer el icono de la aplicación en la barra de tareas
ctypes.windll.user32.SendMessageW(hwnd, 0x80, 0, icon)


# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
LIGHT_BLUE = (173, 216, 230)
LIGHT_RED = (255, 182, 193)

# Crear la pantalla en modo pantalla completa
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Pong")

# Establecer el icono de la ventana
icon = pygame.image.load("pong_icon.ico")
pygame.display.set_icon(icon)

# Velocidad del juego
FPS = 60

# Definir la velocidad del reloj
clock = pygame.time.Clock()

# Definir las dimensiones de las paletas y la pelota
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 200
BALL_SIZE = 40

# Velocidad máxima de las paletas
PADDLE_SPEED = 14

# Velocidades iniciales de las paletas y la pelota
left_paddle_speed = 0
right_paddle_speed = 0
ball_speed_x = 14
ball_speed_y = 14

# Posiciones iniciales de las paletas y la pelota
left_paddle = pygame.Rect(60, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 60 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Puntuaciones
left_score = 0
right_score = 0

# Fuentes de texto
font = pygame.font.Font(None, 148)
small_font = pygame.font.Font(None, 72)

# Sonidos
pong_sound = pygame.mixer.Sound('pong_hit.mp3')
score_sound = pygame.mixer.Sound('pong_score.mp3')

# Lista de partículas
particles = []

# Función para crear partículas
def create_particles(position):
    for _ in range(20):
        particle = [position[0], position[1], random.randint(1, 5), random.randint(-5, 5), random.randint(-5, 5)]
        particles.append(particle)

# Función para mostrar la pantalla de inicio
def show_start_screen():
    screen.fill(BLACK)
    title_text = font.render("¡Pong Game!", True, WHITE)
    instruction_text = small_font.render("Press SPACE to start", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - title_text.get_height() // 2 - 50))
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.flip()
    wait_for_key()

# Función para mostrar la pantalla de fin
def show_end_screen(winner):
    screen.fill(BLACK)
    end_text = font.render(f"{winner} Player Wins!", True, WHITE)
    instruction_text = small_font.render("Press SPACE to play again", True, WHITE)
    screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - end_text.get_height() // 2 - 50))
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.flip()
    wait_for_key()

# Función para esperar a que se presione una tecla
def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

# Bucle principal del juego
show_start_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle_speed = -PADDLE_SPEED
            if event.key == pygame.K_s:
                left_paddle_speed = PADDLE_SPEED
            if event.key == pygame.K_UP:
                right_paddle_speed = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                right_paddle_speed = PADDLE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_paddle_speed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle_speed = 0

    # Mover las paletas
    left_paddle.y += left_paddle_speed
    right_paddle.y += right_paddle_speed

    # Limitar las paletas para que no se salgan de la pantalla
    left_paddle.y = max(0, min(left_paddle.y, HEIGHT - PADDLE_HEIGHT))
    right_paddle.y = max(0, min(right_paddle.y, HEIGHT - PADDLE_HEIGHT))

    # Mover la pelota
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisiones con la parte superior e inferior de la pantalla
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
        pong_sound.play()

    # Colisiones con las paletas
    if ball.colliderect(left_paddle):
        ball_speed_x *= -1
        create_particles(ball.center)
        pong_sound.play()
    if ball.colliderect(right_paddle):
        ball_speed_x *= -1
        create_particles(ball.center)
        pong_sound.play()

    # Reiniciar la pelota si sale de la pantalla por la izquierda o la derecha
    if ball.left <= 0:
        right_score += 1
        ball_speed_x = 14
        ball_speed_y = 14
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        create_particles(ball.center)
        score_sound.play()
        time.sleep(1)
    if ball.right >= WIDTH:
        left_score += 1
        ball_speed_x = -14
        ball_speed_y = -14
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        create_particles(ball.center)
        score_sound.play()
        time.sleep(1)

    # Verificar si algún jugador ha ganado
    if left_score == 10:
        show_end_screen("Left")
        left_score = 0
        right_score = 0
        show_start_screen()
    if right_score == 10:
        show_end_screen("Right")
        left_score = 0
        right_score = 0
        show_start_screen()

    # Dibujar todo
    screen.fill(BLACK)
    pygame.draw.rect(screen, LIGHT_BLUE, left_paddle)
    pygame.draw.rect(screen, LIGHT_RED, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Mostrar puntuaciones
    left_score_text = font.render(str(left_score), True, BLUE)
    right_score_text = font.render(str(right_score), True, RED)
    screen.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 40))
    screen.blit(right_score_text, (WIDTH * 3 // 4 - right_score_text.get_width() // 2, 40))

    # Dibujar y actualizar partículas
    for particle in particles[:]:
        particle[0] += particle[3]
        particle[1] += particle[4]
        particle[2] -= 0.1
        if particle[2] <= 0:
            particles.remove(particle)
        else:
            pygame.draw.circle(screen, WHITE, (int(particle[0]), int(particle[1])), int(particle[2]))

    pygame.display.flip()
    clock.tick(FPS)
