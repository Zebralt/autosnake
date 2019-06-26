import pygame
from pygame.locals import *
from random import randint

from mini_engine import MiniEngine
from mini_locals import *

# This is the bare class. To implement a game, you need to modify this class into your application. You also inherit 
# to benefit from the init and close functions.
    
class MiniApplication:
    def __init__(self, settings=None):
        self.state = State.RUNNING
        
        if settings:
            self.settings = settings
        
        self.init()
        pass
        
    # Operations at application start.
    def init(self):
        pass
    
    # Operations at application closure.
    def close(self):
        pass
        
    def set_settings(self, settings):
        self.settings = settings
        
    # This method must update the application (data structures, etc.)
    def update(self):
        pass
        
    # This method will draw content on the screen.
    def draw(self):
        pass
    
    # Here you will handle events.
    def handle_event(self, events):
        for event in events:
            if event.type == QUIT:
                self.state = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == MouseButton.left:
                    self.settings.mousepos = event.pos
            if event.type == MOUSEBUTTONUP:
                if event.button == MouseButton.left:
                    pass
            if event.type == MOUSEMOTION:
                self.settings.mousepos = event.pos
             
def run_application(miapp):
    miengine = MiniEngine()
    miengine.run_application(miapp)
    
if __name__ == '__main__':
    run_application(MiniApplication())