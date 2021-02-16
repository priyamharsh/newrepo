import pygame
import random
import math
from pygame import mixer

pygame.init()  # allways has to be there
screen = pygame.display.set_mode((800, 600))  # width,height
pygame.display.set_caption("UFO BUSTER")
icon = pygame.image.load("rocket.png")  # icon in 32bit
pygame.display.set_icon(icon)
background = pygame.image.load("solar-system.png")
mixer.music.load("bg.wav")
mixer.music.play(-1)

score = 0
font = pygame.font.Font("freesansbold.ttf", 33)
textX = 10
textY = 10

over_font = pygame.font.Font("freesansbold.ttf", 77)


def show_score(x, y):
    val = font.render('THE SCORE : ' + str(score), True, (255, 255, 255))
    screen.blit(val, (x, y))


def game_over():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (150, 240))
    over_sound = mixer.Sound("game-over.wav")
    over_sound.play()


playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerXchange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


enemyImg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
num_enemy = 6
for i in range(num_enemy):
    enemyImg.append(pygame.image.load("space-invaders.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 160))
    enemyXchange.append(4)
    enemyYchange.append(40)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletXchange = 0
bulletYchange = 10
bullet_state = 'ready'


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    dist = math.sqrt((math.pow(enemyX-bulletX, 2)) +
                     (math.pow(enemyY-bulletY, 2)))
    if dist < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))
    # first is red,green,blue
    screen.blit(background, (140, 50))
    # playerX+=0.1
    # playerY-=0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -5

            if event.key == pygame.K_RIGHT:
                playerXchange = 5

            if event.key == pygame.K_UP:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0

    playerX += playerXchange
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_enemy):
        if enemyY[i] > 440:
            for j in range(num_enemy):
                enemyY[j] = 2000
            game_over()
            break
        enemyX[i] += enemyXchange[i]
        if enemyX[i] <= 0:
            enemyXchange[i] = 4
            enemyY[i] += enemyYchange[i]
        elif enemyX[i] >= 736:
            enemyXchange[i] = -4
            enemyY[i] += enemyYchange[i]
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explo_sound = mixer.Sound("explosion.wav")
            explo_sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 160)
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYchange

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()  # always has to be there
