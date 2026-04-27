import pygame
from random import randint
import time 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
boundary = pygame.Rect(0, 0, 800, 600)

WHITE = (0, 0, 0)
BLACK = (86, 179, 20)
playerleft = True
playerdown = True
playerright = True
playerup = True
enemyleft = True
enemydown = True
enemyright = True
enemyup = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def drawGrid():
    blockSize = 50
    for x in range(0, SCREEN_WIDTH, blockSize):
        for y in range(0, SCREEN_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

player = pygame.Rect(500, 250, 50, 50)
gui = pygame.Rect(0, 600, 800, 200)
movegui = pygame.Rect(50, 650, 200, 100)
attackgui = pygame.Rect(300, 650, 200, 100)
othergui = pygame.Rect(550, 650, 200, 100)
move_dist = 50

enemy = pygame.Rect(50 * randint(0, 15), 50 * randint(0, 11), 50, 50)

def enemyMove():
    direction = randint(1, 4)
    if direction == 1 and enemyleft:
        enemy.move_ip(-50, 0)
    if direction == 2 and enemyright:
        enemy.move_ip(50, 0)
    if direction == 3 and enemyup:
        enemy.move_ip(0, -50)
    if direction == 4 and enemydown:
        enemy.move_ip(0, 50)
    time.sleep(0.1)
    
def playerCollide():
    global playerleft 
    global playerdown 
    global playerright 
    global playerup 
    player.move_ip(-move_dist, 0)
    if player.collidelist(stones)!= -1:
        playerleft = False
    else:
        playerleft = True
    player.move_ip(move_dist, 0)

    player.move_ip(move_dist, 0)
    if player.collidelist(stones)!= -1:
        playerdown = False
    else:
        playerdown = True
    player.move_ip(-move_dist, 0)

    player.move_ip(0, -move_dist)
    if player.collidelist(stones)!= -1:
        playerup = False
    else:
        playerup = True
    player.move_ip(0, move_dist)

    player.move_ip(0, move_dist)
    if player.collidelist(stones)!= -1:
        playerright = False
    else:
        playerright = True
    player.move_ip(0, -move_dist)

def enemyCollide():
    global enemyleft 
    global enemydown 
    global enemyright 
    global enemyup 
    
    enemy.move_ip(-move_dist, 0)
    if enemy.collidelist(stones)!= -1:
        enemyleft = False
    else:
        enemyleft = True
    enemy.move_ip(move_dist, 0)

    enemy.move_ip(move_dist, 0)
    if enemy.collidelist(stones)!= -1:
        enemyright = False
    else:
        enemyright = True
    enemy.move_ip(-move_dist, 0)

    enemy.move_ip(0, -move_dist)
    if enemy.collidelist(stones)!= -1:
        enemyup = False
    else:
        enemyup = True
    enemy.move_ip(0, move_dist)

    enemy.move_ip(0, move_dist)
    if enemy.collidelist(stones)!= -1:
        enemydown = False
    else:
        enemydown = True
    enemy.move_ip(0, -move_dist)

stones = []
for _ in range(randint(20,30)):
    x = 50 * randint(0, 15)
    y = 50 * randint(0, 11)
    stones.append(pygame.Rect(x, y, 50, 50))

run = True

while run:

    screen.fill(BLACK)
    playerCollide()
    enemyCollide()

    for stone in stones:
        pygame.draw.rect(screen, (159, 161, 159), stone)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and playerleft:
                player.move_ip(-move_dist, 0)
            if event.key == pygame.K_d and playerdown:
                player.move_ip(move_dist, 0)
            if event.key == pygame.K_w and playerup:
                player.move_ip(0, -move_dist)
            if event.key == pygame.K_s and playerright:
                player.move_ip(0, move_dist)
    enemyMove()
    
    player.clamp_ip(boundary)
    enemy.clamp_ip(boundary)

    pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.draw.rect(screen, (0, 255, 0), player)
    drawGrid()
    pygame.draw.rect(screen, (0, 0, 0), gui)
    pygame.draw.rect(screen, (159, 161, 159), movegui)
    pygame.draw.rect(screen, (159, 161, 159), attackgui)
    pygame.draw.rect(screen, (159, 161, 159), othergui)

    pygame.display.update()

pygame.quit()