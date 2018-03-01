import pygame, sys
from pygame.locals import *


#useful game dimensions
TILESIZE  = 40
MAPWIDTH  = 3
MAPHEIGHT = 5

#constants representing colours
BLACK = (0,   0,   0  )
BROWN = (153, 76,  0  )
GREEN = (0,   255, 0  )
BLUE  = (0,   0,   255)

#constants representing the different resources
DIRT  = 0
GRASS = 1
WATER = 2
COAL  = 3

#a dictionary linking resources to colours
colours =   {
                DIRT  : BROWN,
                GRASS : GREEN,
                WATER : BLUE,
                COAL  : BLACK
            }

#a list representing our tilemap
tilemap = [
            [GRASS, COAL,  DIRT ],
            [WATER, WATER, GRASS],
            [COAL,  GRASS, WATER],
            [DIRT,  GRASS, COAL ],
            [GRASS, WATER, DIRT ]
          ]

#useful game dimensions
TILESIZE  = 40
MAPWIDTH  = 3
MAPHEIGHT = 5

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

while True:

    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()

    #loop through each row
    for row in range(MAPHEIGHT):
        #loop through each column in the row
        for column in range(MAPWIDTH):
            #draw the resource at that position in the tilemap, using the correct colour
            pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))

    #update the display
    pygame.display.update()