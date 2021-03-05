import pygame
import math
import random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SPACE PONG')
background = pygame.image.load("background.png")
mixer.music.load("background.wav")
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


player_Img = pygame.image.load("minus-sign-of-horizontal-bar.png")
playerX = 370
playerY = 480
playerXchange = 0
playerYchange = 0


def player(x, y):
    screen.blit(player_Img, (x, y))

enemy_Img = pygame.image.load('football-ball.png')
enemyX = 370
enemyY = 16
enemyXchange = 5
enemyYchange = 5

def enemy(x,y):
    screen.blit(enemy_Img,(x,y))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    dist = math.sqrt((math.pow(enemyX-bulletX, 2)) +
                     (math.pow(enemyY-bulletY, 2)))
    if dist < 29 :
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
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -10
            if event.key == pygame.K_RIGHT:
                playerXchange = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0

    playerX+=playerXchange
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    
    
    enemyX+=enemyXchange
    enemyY+=enemyYchange
    if enemyX >= 780:
        enemyXchange = -5
        explo_sound = mixer.Sound("laser.wav")
        explo_sound.play()
    elif enemyX <= 0:
        enemyXchange = 5
        explo_sound = mixer.Sound("laser.wav")
        explo_sound.play()

    if enemyY <= 0:
        enemyYchange = 5
        explo_sound = mixer.Sound("laser.wav")
        explo_sound.play()
    elif enemyY >= 510 :
        enemyYchange = -5
        explo_sound = mixer.Sound("laser.wav")
        explo_sound.play()
        life-=1
  
    collision = is_collision(enemyX, enemyY, playerX, playerY)
    if collision:
        explo_sound = mixer.Sound("laser.wav")
        explo_sound.play()
        enemyYchange = -5

    enemy(enemyX,enemyY)
    player(playerX,playerY)
    show_life(10, 10)
    for i in range(10):
        if life == 0:
            game_over()
            over_font = pygame.font.Font('freesansbold.ttf', 77)
            over_text = over_font.render('GAME OVER', True, (255, 255, 255))
            screen.blit(over_text, (150, 240))
        break

    pygame.display.update()
