    

    
class MiniSettings:
    def __init__(self):
        # default settings
        self.settings = {}
        self.resolution = { 'width' : 800, 'height' : 600 }
        self.window_rect = (self.resolution['width'], self.resolution['height'])
        self.refresh_rate = 60
        self.key_repeat = {'delay' : 400, 'frequency' : 30}
        pass
        
    def loadFromFile(self, filepath):
        pass
