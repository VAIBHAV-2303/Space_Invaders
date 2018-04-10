import pygame
import sys
import os
import time
import random
import Classes

pygame.init()
pygame.mixer.init()
pygame.font.init()


time.sleep(5)
Createalien = pygame.USEREVENT + 1
decreasetime = pygame.USEREVENT + 2
movemissile = pygame.USEREVENT + 3
alieniarr = []
alienlarr = []
imissarr = []
lmissarr = []
ship = Classes.Ship()
score = 0
size = width, height = 640, 640
myfont = pygame.font.Font('./Pixel-Miners.otf', 30)
screen = pygame.display.set_mode(size)
boom = pygame.mixer.Sound('Explosion+1.wav')
pui = pygame.mixer.Sound('shoo.wav')
alienx = Classes.alieni(random.randint(0, 7) * 80, random.randint(0, 1) * 80)
alieniarr.append(alienx)

# Perpetual events
pygame.time.set_timer(Createalien, 10000)
pygame.time.set_timer(decreasetime, 1000)
pygame.time.set_timer(movemissile, 10)


def events():
    for event in pygame.event.get():
        global alieniarr
        global alienlarr
        global imissarr
        global lmissarr
        global ship

        if event.type == pygame.QUIT:
            print("######## Final Score->" + str(score) + "#########")
            sys.exit()

        if event.type == movemissile:
            for i in imissarr:
                i.move()

            for i in lmissarr:
                i.move()

        if event.type == decreasetime:
            for i in alieniarr:
                i.dectime()
                if i.timer == 0:
                    alieniarr.remove(i)

            for i in alienlarr:
                i.dectime()
                if i.timer == 0:
                    alienlarr.remove(i)

        if event.type == Createalien:
            y = random.randint(0, 1) * 80
            x = random.randint(0, 7) * 80
            alienx = Classes.alieni(x, y)
            alieniarr.append(alienx)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.QUIT
                # print(alieniarr)
                print("######## Final Score->" + str(score) + "#########")
                sys.exit()

            if event.key == pygame.K_a:
                ship.mleft()

            if event.key == pygame.K_d:
                ship.mright()

            if event.key == pygame.K_SPACE:
                launchi()

            if event.key == pygame.K_s:
                launchl()


def launchi():
    global ship
    hui = pui.play()
    imissx = Classes.imiss(ship.posx + 31, ship.posy - 80)
    imissarr.append(imissx)


def launchl():
    global ship
    hui = pui.play()
    lmissx = Classes.lmiss(ship.posx + 31, ship.posy - 80)
    lmissarr.append(lmissx)


def checkcrash():
    global score
    for i in imissarr:
        for j in alieniarr:
            if (i.posx -
                j.posx) < 45 and (i.posx -
                                  j.posx) > 0 and (i.posy -
                                                   j.posy) < 60 and (i.posy -
                                                                     j.posy) > 0:
                score += 1
                tui = boom.play()
                alieniarr.remove(j)
                imissarr.remove(i)

    for i in lmissarr:
        for j in alieniarr:
            if (i.posx -
                j.posx) < 45 and (i.posy -
                                  j.posy) < 60 and (i.posx -
                                                    j.posx) > 0 and (i.posy -
                                                                     j.posy) > 0:
                tui = boom.play()
                alienx = Classes.alienl(j.posx, j.posy, j.timer + 5)
                alienlarr.append(alienx)
                alieniarr.remove(j)
                lmissarr.remove(i)

    for i in imissarr:
        for j in alienlarr:
            if (i.posx -
                j.posx) < 45 and (i.posy -
                                  j.posy) < 60 and (i.posx -
                                                    j.posx) > 0 and (i.posy -
                                                                     j.posy) > 0:
                score += 1
                tui = boom.play()
                alienlarr.remove(j)
                imissarr.remove(i)
