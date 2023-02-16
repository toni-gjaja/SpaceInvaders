import pygame
import random
import time

#inicijalizacija
pygame.init()

#sirina i visina ekrana, caption i ikona igre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space invaders")

icon = pygame.image.load('SpaceShip1.png')
pygame.display.set_icon(icon)

background = pygame.image.load('background.png')

#postavljanje igraca
playerImg = pygame.image.load('SpaceShip1.png')
playerX = 370
playerY = 480

#postavljanje meta
enemyImg1 = pygame.image.load('Enemy1.png')
enemyImg2 = pygame.image.load('Enemy2.png')

listOfEnemies = [enemyImg1, enemyImg2]

#varijabla za random biranje
a = random.randint(0,1)

enemyX = random.randint(0, 750)
enemyY = random.randint(50, 150)
enemyMovementX = 0.7
enemyMovementY = -30

#pucanje
bulletImg = pygame.image.load('Bullet.png')
bulletX = 0
bulletY = 480
bulletX_move = 0
bulletY_move = 10
bulletState = "ready"

#blit je funkcija za crtanje po ekranu
def player(x, y):
    screen.blit(playerImg,(x, y))

def enemy(x, y):
    screen.blit(listOfEnemies[a], (x,y))

def bullet_firing(x, y):
    global bulletState
    bulletState = "firing"
    screen.blit(bulletImg, (x, y))


#pocetak igre
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if playerX > 750:
                playerX = 750
            else:
                playerX += 1
        if event.key == pygame.K_LEFT:
            if playerX < 20:
                playerX = 20
            else:
                playerX -= 1
        if event.key == pygame.K_SPACE:
            bullet_firing(playerX, bulletY)


    if enemyX <= 0:
        enemyY -= enemyMovementY
        enemyMovementX = 0.7

    elif enemyX >= 770:
        enemyY -= enemyMovementY
        enemyMovementX = -0.7

    #ispaljivanje metka
    if bulletState == "firing":
        bullet_firing(playerX, bulletY)
        bulletY -= bulletY_move


    enemyX += enemyMovementX

    player(playerX, playerY)

    enemy(enemyX, enemyY)

    pygame.display.update()


