class Color:
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

class MouseButton:
    left = 1
    right = 2
    roll = 3
    roll_up = 4
    roll_down = 5
    
class State:
    RUNNING = 0b1
    PAUSED = 0b10
    

class ApplicationState(State):
    IN_MENU = 0b100