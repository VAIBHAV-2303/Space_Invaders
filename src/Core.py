import pygame
import sys
import os
import time
import random
import Classes

# initiation
pygame.init()
pygame.mixer.init()

shipimg = pygame.image.load("static/ship.png")
alieniimg = pygame.image.load("static/alieni.png")
alienlimg = pygame.image.load("static/alienl.png")
imissileimg = pygame.image.load("static/imissile.png")
lmissileimg = pygame.image.load("static/lmissile.png")
bg = pygame.image.load("static/Wiki-background.jpg")

# Instructions
os.system('clear')
print("-----Instructions-----")
print("Press A to move left")
print("Press D to move right")
print("Press Space to shoot i missile")
print("Press S to shoot l missile")
print("Score will be displayed in the end")

import functions


# Game Main loop
while True:
    functions.events()
    functions.checkcrash()
    if len(functions.alieniarr) == 0 and len(functions.alienlarr) == 0:
        alienx = Classes.alieni(
            random.randint(
                0,
                7) * 80,
            random.randint(
                0,
                1) * 80)
        functions.alieniarr.append(alienx)

    functions.screen.fill((10, 10, 10))
    functions.screen.blit(bg, (0, 0))
    text = functions.myfont.render('Score=' + str(functions.score), True, (255, 255, 255))
    functions.screen.blit(text, (0, 0))
    functions.screen.blit(shipimg, (functions.ship.posx, functions.ship.posy))
    for i in functions.alieniarr:
        functions.screen.blit(alieniimg, (i.posx, i.posy))

    for i in functions.alienlarr:
        functions.screen.blit(alienlimg, (i.posx, i.posy))

    for i in functions.imissarr:
        functions.screen.blit(imissileimg, (i.posx, i.posy))

    for i in functions.lmissarr:
        functions.screen.blit(lmissileimg, (i.posx, i.posy))

    pygame.display.flip()
