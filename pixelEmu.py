#!/usr/bin/python2.7
import sys
import pygame

pygame.init()

matrixArea = 64, 32
screenSize = 640, 320 
black = 0, 0, 0
red = 255, 0, 0
rect = 0, 0, 640/matrixArea[0], 480/matrixArea[1] 

screen = pygame.display.set_mode(screenSize)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    pygame.draw.rect(screen, red, rect)
    pygame.display.flip()
