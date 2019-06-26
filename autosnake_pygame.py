import autosnake as asnake

import pygame
from pygame.locals import *
from random import randint

"""
Mouse buttons codes
"""

white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
lightblue = (100,150,255)
lightgreen = (100,255,150)
lightred = (255,100,100)
orange = (255,150,100)
yellow = (255,255,50)
black = (0,0,0)

class MOUSEBUTTONS:
    MOUSEBUTTON_LEFT        = 1
    MOUSEBUTTON_RIGHT       = 2
    MOUSEBUTTON_ROLL        = 3
    MOUSEBUTTON__ROLL_UP    = 4
    MOUSEBUTTON_ROLL_DOWN   = 5

class STATE:
    PLAYING, WON, LOST = range(3)
    
def scale_rect(rect, scale):
    pos = rect[0]
    size = rect[1]
    
    nsize = (round(size[0] * scale), round(size[1] * scale))
    
    sdiff_x = size[0] - nsize[0]
    sdiff_y = size[1] - nsize[1]
    
    npos = (pos[0] + sdiff_x/2, pos[1] + sdiff_y/2)
    
    return (npos, nsize)
    
if __name__ == '__main__':

    snake_game = asnake.SnakeGame(40, 40)
    
    WINDOW_RECT = (800, 600)
    
    rect_size = min(WINDOW_RECT)/min(snake_game.grid.width, snake_game.grid.height)
    rect_size = int(rect_size/3)
    margin = 1
    main_grid_pos = (int(min(WINDOW_RECT)/3), int(min(WINDOW_RECT)/3))

    """ PYGAME WINDOW INITIALIZATION """
    pygame.init()
    window = pygame.display.set_mode(WINDOW_RECT)
    pygame.display.flip()
    pygame.key.set_repeat(400,30)
    go_on = 1
    """  """

    while go_on:
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                go_on = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == MOUSEBUTTONS.MOUSEBUTTON_LEFT:
                    snake_game.reset()
                    mousepos = event.pos
            if event.type == MOUSEBUTTONUP:
                if event.button == MOUSEBUTTONS.MOUSEBUTTON_LEFT:
                    firing = False
            if event.type == MOUSEMOTION:
                mousepos = event.pos

        # drawing the grid
        bg_rect = (main_grid_pos, ((rect_size + margin) * snake_game.grid.width, (rect_size + margin) * snake_game.grid.height))
        pygame.draw.rect(window, (40, 20, 30), scale_rect(bg_rect, 1.25))
        pygame.draw.rect(window, (20, 20, 30), bg_rect)
        grid = snake_game.run()
        if grid:
            for i in range(grid.width):
                for j in range(grid.height):
                    rect = ((main_grid_pos[0] + (rect_size + margin) * i, main_grid_pos[1] + (rect_size + margin) * j ),(rect_size, rect_size))
                    if (i, j) == snake_game.food:      
                        pygame.draw.rect(window, orange, scale_rect(rect, 2))
                    elif (i ,j) == snake_game.snake[0]:      
                        pygame.draw.rect(window, yellow,  scale_rect(rect, 1.5))
                    elif grid.get(i, j):
                        pygame.draw.rect(window, white, rect)
                    elif snake_game.path and (i, j) in snake_game.path:                        
                        pygame.draw.rect(window, (100, 100, 100),  scale_rect(rect, 0.5))

        pygame.display.flip()
            