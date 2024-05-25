import pygame, sys, random
from pygame.locals import *

# Configurando o pygame
pygame.init()
mainClock = pygame.time.Clock()

# Configurando a janela
WINDOWWIDTH = 1000
WINDOWHEIGHT = 1000
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# Definindo cores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

def centralizar_player():
    """Calcula e posiciona o player no centro da janela."""
    player.left = (WINDOWWIDTH - player.width) // 2  # Centraliza na posição X
    player.top  = (WINDOWHEIGHT - player.height) // 2  # Centraliza na posição Y

# Configurando o player e comida
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(500, 0, 20, 20)  # Placeholder, será atualizado pelo centralizar_player()
snake = [player]
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Chama centralizar_player() para posicionar o player no início
centralizar_player()  # Esta linha garante que o player comece centralizado

# Configurando e criando as variáveis de movimento
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Rodando o game em loop
while True:
    # Checando eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Checando a variável do teclado
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
                moveLeft = False
            if event.key == K_UP or event.key == K_w:
                moveUp = True
                moveDown = False
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Adicione a nova comida
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # Desenha o fundo branco na superfície
    windowSurface.fill(WHITE)

    # Movimentando o player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.bottom += MOVESPEED
    if moveDown and player.bottom >= WINDOWHEIGHT:
        player.bottom = 10 + player.height

    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveUp and player.top <= 0:
        player.top = WINDOWHEIGHT - player.height

    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveLeft and player.left <= 0:
        player.left = WINDOWWIDTH - player.width

    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    if moveRight and player.right >= WINDOWWIDTH:
        player.right = 10 + player.width

    # Atualiza segmentos do corpo
    for i in range(len(snake) - 1, 0, -1):
        snake[i].topleft = snake[i - 1].topleft

    # Desenha a cobra
    for segment in snake:
        pygame.draw.rect(windowSurface, BLACK, segment)

    # Checando se o player colidiu com algum quadrado de comida
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            # Adiciona um novo segmento à cobra
            new_segment = pygame.Rect(snake[-1].left, snake[-1].top, player.width, player.height)
            snake.append(new_segment)

    # Desenha a comida
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # Atualiza a janela na tela
    pygame.display.update()
    mainClock.tick(40)
