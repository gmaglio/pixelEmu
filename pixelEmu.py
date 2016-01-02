#!/usr/bin/python2.7
import sys
import pygame
import time
import random

pygame.init()

matrixArea = 64, 32
screenSize = 1024, 512 
scaleValue = screenSize[0]/matrixArea[0], screenSize[1]/matrixArea[1]
black = 0, 0, 0

def SetPixel(x,y,r,g,b):
    pygame.draw.rect(screen, (r,g,b), (x*scaleValue[0], y*scaleValue[1], scaleValue[0], scaleValue[1]) )

screen = pygame.display.set_mode(screenSize)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for a in range(64):
        for b in range(random.randint(0,31)):
            SetPixel(a, 32-b, b*8, b*4, 32-b)
    time.sleep(0.05)
    pygame.display.flip()
    screen.fill(black)

    
