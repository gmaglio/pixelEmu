#!/usr/bin/python2.7
import sys
import pygame

pygame.init()

matrixArea = 64, 32
screenSize = 640, 320 
black = 0, 0, 0
red = 255, 0, 0
rect = 0, 0, 640/matrixArea[0], 480/matrixArea[1] 

def put_pixel((x, y),(r,g,b)):
    pygame.draw.rect(screen, (r,g,b), (x, y, 640/matrixArea[0], 480/matrixArea[1]) )
    pygame.display.flip()

screen = pygame.display.set_mode(screenSize)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for y in range(32):
        for x in range(64):
            put_pixel((x,y), (x, y, y))

    screen.fill(black)


    
