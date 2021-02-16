import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SPACE RIDER')
background = pygame.image.load("background.png")
mixer.music.load("bg.wav")
mixer.music.play(-1)

life = 5
font = pygame.font.Font('freesansbold.ttf', 33)


def dist(x1, y1, x2, y2):
    dista = math.sqrt((math.pow((x1 - x2), 2)) + (math.pow((y1 - y2), 2)))
    return dista


def show_life(x, y):
    val = font.render('LIFE :' + str(life), True, (255, 255, 255))
    screen.blit(val, (x, y))


over_font = pygame.font.Font('freesansbold.ttf', 77)


def game_over():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (150, 240))
    over_sound = mixer.Sound("game-over.wav")
    over_sound.play()


player_Img = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerXchange = 0
playerYchange = 0


def player(x, y):
    screen.blit(player_Img, (x, y))


enemyImg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
num_enemy = 6
for i in range(num_enemy):
    enemyImg.append(pygame.image.load("space-invaders.png"))
    enemyX.append(random.randint(10*(i+2), 100*(i+2)))
    enemyY.append(random.randint(5*(i), 6*(i+1)))
    enemyXchange.append(0)
    enemyYchange.append(11)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    dist = math.sqrt((math.pow(enemyX-bulletX, 2)) +
                     (math.pow(enemyY-bulletY, 2)))
    if dist < 38:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -5
            if event.key == pygame.K_RIGHT:
                playerXchange = 5
            if event.key == pygame.K_UP:
                playerYchange = -6
            if event.key == pygame.K_DOWN:
                playerYchange = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerXchange = 0
                playerYchange = 0

    playerX += playerXchange
    playerY += playerYchange

    if playerX <= 0:
        playerX = 370
        playerY = 480
        life += 1
    elif playerX >= 736:
        playerX = 736

    if playerY <= 0:
        playerX = 370
        playerY = 480
        life += 1
    elif playerY >= 536:
        playerY = 536

    for i in range(num_enemy):
        if life == 0:
            # for j in range(num_enemy):
                # enemyY[j] = 2000
            game_over()
            break
        enemyY[i] += enemyYchange[i]
        if enemyY[i] >= 600:
            enemyX[i] = random.randint(100*(i), 110*(i+1))
            enemyY[i] = random.randint(5*(i), 6*(i+1))
        collision = is_collision(enemyX[i], enemyY[i], playerX, playerY)
        if collision:
            explo_sound = mixer.Sound("explosion.wav")
            explo_sound.play()
            life -= 1
            playerX = 370
            playerY = 480
            enemyX[i] = random.randint(100*(i), 110*(i+2))
            enemyY[i] = random.randint(5*(i), 6*(i+1))
        enemy(enemyX[i], enemyY[i], i)
    show_life(10, 10)
    player(playerX, playerY)
    pygame.display.update()
