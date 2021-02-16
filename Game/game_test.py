# import new_game
# abhi upar wale ko import kiye the to game chal gaya
import pygame
import random
import math
from pygame import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ARCADE')
font = pygame.font.Font('freesansbold.ttf', 30)
# message = 'FOR PLAYING UFO BUSTERS','\n\n','PRESS UP'


def show_info():
    info = font.render('FOR PLAYING UFO BUSTERS',
                       True, (25, 25, 255))
    screen.blit(info, (180, 140))
    info1 = font.render('PRESS 1',
                        True, (255, 0, 0))
    screen.blit(info1, (300, 200))

    info2 = font.render('FOR PLAYING SPACE RIDERS',
                        True, (25, 255, 25))
    screen.blit(info2, (180, 260))
    info3 = font.render('PRESS 2',
                        True, (255, 0, 0))
    screen.blit(info3, (300, 320))

    info4 = font.render('FOR PLAYING SPACE PONG',
                        True, (25, 255, 25))
    screen.blit(info4, (180, 380))
    info5 = font.render('PRESS 3',
                        True, (255, 0, 0))
    screen.blit(info5, (300, 440))


running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                import new_game
                running = False
            elif event.key == pygame.K_2:
                import new_game2
                running = False
            elif event.key == pygame.K_3:
                import new_game3
                running = False
        # if event.type == pygame.KEYUP:

    show_info()
    pygame.display.update()
