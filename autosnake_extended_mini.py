import pygame
from pygame.locals import *

import autosnake as asnake

import sys
sys.path.append('../mini_engine')
import mini_application as minapp
from mini_settings import MiniSettings
from mini_locals import *

def scale_rect(rect, scale):

    return rect

    pos = rect[0]
    size = rect[1]
    
    nsize = (round(size[0] * scale), round(size[1] * scale))
    
    sdiff_x = size[0] - nsize[0]
    sdiff_y = size[1] - nsize[1]
    
    npos = (pos[0] + sdiff_x/2, pos[1] + sdiff_y/2)
    
    return (npos, nsize)
    
def modulo_tuple(tuple, value):
    
    r = (tuple[0]%value[0], tuple[1]%value[1])
    
    return r
    
class SnakeGameApplication(minapp.MiniApplication):
    def __init__(self, settings, w=40, h=40):
        self.w = w
        self.h = h
        super().__init__(settings)
        settings.refresh_rate = 10
    
    def init(self):

        self.snake_game = asnake.SnakeGame(self.w, self.h)        
        self.rect_size = min(self.settings.window_rect)/max(self.snake_game.grid.width, self.snake_game.grid.height)
        self.rect_size = int(self.rect_size/3)
        self.margin = 1
        self.main_grid_pos = (0, 0)# (int(min(self.settings.window_rect)/3), int(min(self.settings.window_rect)/3))
        
        
        
    def close(self):
        print("What, you're leaving already ? how sad.")
        
    def update(self):
        # do something
        self.bg_rect = (self.main_grid_pos, ((self.rect_size + self.margin) * self.snake_game.grid.width, (self.rect_size + self.margin) * self.snake_game.grid.height))
        pygame.draw.rect(self.window, (40, 20, 30), scale_rect(self.bg_rect, 1.25))
        pygame.draw.rect(self.window, (20, 20, 30), self.bg_rect)
        self.grid = self.snake_game.run()
        self.extended_grid = self.snake_game.extended_grid
        
    def draw(self):
        # do smth
        if self.extended_grid:
            for i in range(self.extended_grid.width):
                for j in range(self.extended_grid.height):
                    rect = ((self.main_grid_pos[0] + (self.rect_size + self.margin) * i, self.main_grid_pos[1] + (self.rect_size + self.margin) * j ),(self.rect_size, self.rect_size))
                    #if (i, j) == modulo_tuple(self.snake_game.food, (self.grid.width, self.grid.height)):      
                    #    pygame.draw.rect(self.window, Color.orange, scale_rect(rect, 2))
                    #elif (i ,j) == modulo_tuple(self.snake_game.snake[0], (self.grid.width, self.grid.height)):      
                    #    pygame.draw.rect(self.window, Color.yellow,  scale_rect(rect, 1.5))
                    if self.extended_grid.get(i, j):
                        pygame.draw.rect(self.window, Color.white, rect)
                    #elif self.snake_game.path and (i, j) in self.snake_game.path:                        
                     #   pygame.draw.rect(self.window, (100, 100, 100),  scale_rect(rect, 0.5))
        
    def handle_event(self, events):
        for event in events:
            if event.type == QUIT:
                self.state = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == MouseButton.left:
                    self.snake_game.reset()
                    self.settings.mousepos = event.pos
            if event.type == MOUSEBUTTONUP:
                if event.button == MouseButton.right:
                    pass
            if event.type == MOUSEMOTION:
                self.settings.mousepos = event.pos
    
    
if __name__ == '__main__':    

    meng = SnakeGameApplication(h=40, w=40, settings=MiniSettings())
    minapp.run_application(meng)
            