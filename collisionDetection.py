import pygame, sys, random
from pygame.locals import *

#Configurando o pygame
pygame.init()
mainClock = pygame.time.Clock()

# Configuring the window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 1000
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# Defining colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

def centralizar_player():
    """Calculates and sets the player's position to the center of the window."""
    player_x = (WINDOWWIDTH - player.width) // 2  # Center X position
    player_y = (WINDOWHEIGHT - player.height) // 2  # Center Y position
    player.left = player_x  # Update player's X coordinate
    player.top = player_y  # Update player's Y coordinate


# Configuring the player and food
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(500, 0, 50, 50)  # Placeholder, will be updated by centralizar_player()
foods = []
obstaculos = []
for i in range(20):
  foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Call centralizar_player() to position the player at the start
centralizar_player()  # This line ensures the player starts centered


#Configurando e criando as variaveis de movimento
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6


#Rodando o game em loop
while True:
    #Checando eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            #Checando a variavel do teclado
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
        #adicione a nova comida
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # Desenhe o fundo branco na superfície.
    windowSurface.fill(WHITE)

    #Movimentando o player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveDown and player.bottom > WINDOWHEIGHT:
        player.top = 0

    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveUp and player.top < 0:
        player.top = WINDOWHEIGHT 
    

    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveLeft and player.left < 0:
        player.left = WINDOWWIDTH

    if moveRight and player.right < WINDOWHEIGHT:
        player.right += MOVESPEED
    if moveRight and player.right > WINDOWHEIGHT:
        player.right = 0 + player.width
    

    #Desenhe o player na superficie
    pygame.draw.rect(windowSurface, BLACK, player)

    #Checando se o player colidiu com algum quadrado de comida
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            #Aumentando o tamanho do player a cada comida
            player.height += 5
            player.width += 5
            
    #Trazendo a comida
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    #Trazendo a janela para a tela
    pygame.display.update()
    mainClock.tick(40)