import shortest_path as pf
import simple_grid as sg
from random import randint

UP, DOWN, LEFT, RIGHT = range(4)

class SnakeGame:
    # okay
    def __init__(self, width, height):
        self.grid = sg.Grid(width, height)
        self.extended_grid = sg.Grid(width * 3, height * 3)
        self.orientation = UP
        
        self.food = (0, 0)
        self.snake_length = 0
        self.snake = []
        self.path = []
        self.path_length = 0
        
        self.reset()
        
    # okay   
    def reset(self):
        self.food = (0, 0)
        self.snake_length = 0
        self.snake = []
        self.path = []
        self.path_length = 0
        
        self.grid.reset()
        self.generate_snake()
        self.generate_food()
        
        self.save = None
        
        #self.grid.print()
    # ?
    def go(self, o):
        if o in [UP, DOWN, LEFT, RIGHT]:
            self.orientation = o
       
    # okay
    def generate_food(self):
        while self.food in self.snake:
            self.food = (randint(0, self.grid.width - 1), randint(0, self.grid.height - 1))
        self.grid.set_from_tuple(self.food, sg.WATER)
        self.update_extended_grid(self.food, sg.WATER)
        
    # okay
    def generate_snake(self, length=3):
        self.snake_length = length
        initial_pos = (randint(0, self.grid.width - 1 - length), randint(0, self.grid.height - 1 - length))
        self.snake.append(initial_pos)
        for i in range(1, length):
            self.snake.append((initial_pos[0], initial_pos[1] + i))
        
        for s in self.snake:
            self.grid.set_from_tuple(s, sg.OBSTACLE)
            self.update_extended_grid(s, sg.OBSTACLE)
        
    # okay ?
    def end(self):
        return self.path == None or len(self.snake) != len(set(self.snake))# or len(self.snake) == self.grid.width * self.grid.height
       
    def run(self):
        if not self.end():
            self.next()    
        return self.grid
    # okay ?
    def next(self):
        it = 0
        it += 1
        ate = False
        if self.snake[0] == self.food:
            self.generate_food()
            ate = True
            #print(self.snake[0])
            self.find_path()
            #print("COMPUTED PATH:", self.path)
            if not self.path:
                print("No path found")
                self.path = None
                return
        
        # if no path or path is no longer working, recompute it
        elif not self.path or (self.path and [x for x in self.snake if x in self.path]):
            
            #print(self.snake[0])
            self.find_path()
            # print("COMPUTED PATH:", self.path)
            if not self.path:
                print("No path found")
                self.path = None
                return
        # cut first node of path, as it is the src node
        
        
        next_pos = self.path.pop(0)
        
        # check next_pos :
        # not equal to current head position
        # not too far away (distance=1)
        # compute the new pos if in an outer grid
        if next_pos == self.snake[0]:
            print("NASTY MESSAGE.EXE")
            return
        
        #print("NEXT POS", next_pos)
        self.snake.insert(0, next_pos)
        
        self.grid.set_from_tuple(next_pos, sg.OBSTACLE)
        self.update_extended_grid(next_pos, sg.OBSTACLE)
        
        if not ate:
            previous_pos = self.snake.pop()
            
            self.grid.set_from_tuple(previous_pos, sg.EMPTY)
            self.update_extended_grid(previous_pos, sg.EMPTY)
            
            if self.extended_grid.get_from_tuple(previous_pos):
                print("ASSAULT !")
            
        else:
            self.snake_length += 1
            #print("BIGGER SNAKE", self.snake_length, len(self.snake))
        
        #print("ITERATION", it)
        #print("SNAKE", self.snake, self.snake_length)
        #print("FOOD AT", self.food)
        #print("PATH", self.path)
        #self.grid.print(self.path)
            
    def update_extended_grid(self, pos, value):
        [self.extended_grid.set(pos[0] + i * self.grid.width, pos[1] + j * self.grid.height, value) for i in range(3) for j in range(3)]
        
    def find_path(self):
        # trying normal grid
        self.path, self.path_length = pf.shortest_path_in_grid(self.snake[0], self.food, self.grid, allowDiagonalMovement=False)
        
        if not self.path:
            
            self.extended_path = []
            for i in range(9):
                if self.extended_path:
                    break
                self.extended_path, _ = pf.shortest_path_in_grid(self.transpose_pos_to_extended(self.snake[0]), self.transpose_pos_to_extended(self.food, i%3, int(i/3)), self.extended_grid, allowDiagonalMovement=False)
            
            if self.extended_path:
                print("Found a path in extended grid instead")
                print(self.extended_path)
                self.reduce_path()
                
        self.path, self.path_length = self.path[1:], self.path_length - 1
        
    def transpose_pos_to_extended(self, tuple, x=1, y=1):
        return (tuple[0] + x * self.grid.width, tuple[1] + y * self.grid.height)
        
    def reduce_path(self):
        if not self.extended_path:
            return
        
        self.path = [(item[0]%self.grid.width, item[1]%self.grid.height) for item in self.extended_path]
        # for the grand grid
    
# So, a self-solving snake :
# Snake can move in the four directions, and can get from one side of the screen
# to the other. So this means that the pathfinding algorithm wil be use on the grid
# and on direction duplicates (4 or 9).
# Only recompute the path if the snake is on it. 
# And compare the remaining length of the
# serpent to the remaining length of the path.
# if path.length() - path.indexOf(case) <= snake.length() - snake.indexOf(case):
#   recompute the path


class AutosnakeRecord:
    def __init__(self):
        pass
        
    def load_from_file(self, filepath):
        pass
        
    def save_to_file(self, filepath):
        pass

"""
if snake head on food
	generate food
	compute path to food
	ate = true

elseif not path or path unsuitable
	compute path to food

next_pos = path.pop(0)
if ate:
	# grow the snake
	snake.insert(0, next_pos)
else:
	# move the snake
	snake.insert(0, next_pos)
	snake.pop()
"""
if __name__ == '__main__':
    ss = SnakeGame(10, 10)
    ss.run()