import pygame
from pygame.locals import *
from random import randint

# local imports
from mini_settings import MiniSettings
from mini_locals import *
        
class MiniEngine:
    def __init__(self, application=None, settings=None):
    
        self.settings = None
        
        if not settings:
            self.settings = MiniSettings()
        else:
            self.settings = settings
        
        self.application_state = ApplicationState.RUNNING
        self.inited = False
        
        #
        
        self.set_application(application)
        
        self.init()
        
    def init(self):
        self.inited = True
        pygame.init()
        pygame.key.set_repeat(self.settings.key_repeat['delay'], self.settings.key_repeat['frequency'])
        self.window = pygame.display.set_mode(self.settings.window_rect)
        pygame.display.flip()
    
    def handle_event(self, events):
        # what to do with events ?
        
        if self.application:
            self.application.handle_event(events)
        
        self.default_handle_event(events)
    
    def update(self):
        # what to update
        if self.application:
            self.application.update()
        
        self.default_update()
    
    def draw(self):
        
        if self.application:
            self.application.draw()
            
        self.default_draw()
        
    def default_draw(self):
        pass
    
    def default_handle_event(self, events):
        for event in events:
            if event.type == QUIT:
                self.application_state = 0
    
    def default_update(self):
        if self.application and not self.application.state:
            self.application_state = 0
        
    def set_application(self, app):
    
        if not self.inited:
            self.init()
    
        if app:
            self.application = app
            self.application.settings = self.settings
            self.application.window = self.window
    
    def run_application(self, application=None):
    
        if not self.inited:
            self.init()
    
        if application:
            self.set_application(application)
            
        # main loop
        while (self.application_state & ApplicationState.RUNNING):
            
            pygame.time.Clock().tick(self.settings.refresh_rate)
            
            self.handle_event(pygame.event.get())
            self.update()
            self.window.fill(Color.black)
            self.draw()
            pygame.display.flip()
            
        return self.application_state
        